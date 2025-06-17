#!/usr/bin/env python3
"""
Image optimization script for PYX Engenharia portfolio.
Optimizes images for web use while maintaining quality.
"""

import os
from pathlib import Path
import logging
from typing import List, Tuple
from PIL import Image
import argparse
import concurrent.futures
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ImageStats:
    """Statistics for image optimization."""
    original_size: int
    optimized_size: int
    format: str
    dimensions: Tuple[int, int]

class ImageOptimizer:
    """Handles image optimization with various quality settings."""
    
    def __init__(self, quality: int = 85, max_width: int = 1920):
        self.quality = quality
        self.max_width = max_width
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.webp'}
    
    def should_optimize(self, file_path: Path) -> bool:
        """Check if file should be optimized."""
        return (
            file_path.suffix.lower() in self.supported_formats
            and file_path.is_file()
        )
    
    def get_output_path(self, file_path: Path) -> Path:
        """Get the output path for the optimized image."""
        return file_path.parent / f"{file_path.stem}_optimized{file_path.suffix}"
    
    def optimize_image(self, file_path: Path) -> ImageStats:
        """Optimize a single image."""
        try:
            with Image.open(file_path) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Calculate new dimensions
                width, height = img.size
                if width > self.max_width:
                    ratio = self.max_width / width
                    new_size = (self.max_width, int(height * ratio))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Prepare output path
                output_path = self.get_output_path(file_path)
                
                # Save optimized image
                img.save(
                    output_path,
                    quality=self.quality,
                    optimize=True
                )
                
                return ImageStats(
                    original_size=file_path.stat().st_size,
                    optimized_size=output_path.stat().st_size,
                    format=img.format,
                    dimensions=img.size
                )
                
        except Exception as e:
            logger.error(f"Error optimizing {file_path}: {e}")
            raise

def process_directory(directory: Path, quality: int = 85, max_width: int = 1920) -> List[ImageStats]:
    """Process all images in a directory."""
    optimizer = ImageOptimizer(quality=quality, max_width=max_width)
    stats = []
    
    # Find all image files
    image_files = [
        f for f in directory.rglob("*")
        if optimizer.should_optimize(f)
    ]
    
    # Process images in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {
            executor.submit(optimizer.optimize_image, f): f
            for f in image_files
        }
        
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                stat = future.result()
                stats.append(stat)
                logger.info(
                    f"Optimized {file_path.name}: "
                    f"{stat.original_size/1024:.1f}KB -> {stat.optimized_size/1024:.1f}KB "
                    f"({(1 - stat.optimized_size/stat.original_size)*100:.1f}% reduction)"
                )
            except Exception as e:
                logger.error(f"Failed to process {file_path}: {e}")
    
    return stats

def main():
    parser = argparse.ArgumentParser(description="Optimize images for web use")
    parser.add_argument(
        "directory",
        type=Path,
        help="Directory containing images to optimize"
    )
    parser.add_argument(
        "-q", "--quality",
        type=int,
        default=85,
        help="JPEG quality (0-100, default: 85)"
    )
    parser.add_argument(
        "-w", "--max-width",
        type=int,
        default=1920,
        help="Maximum image width in pixels (default: 1920)"
    )
    
    args = parser.parse_args()
    
    if not args.directory.exists():
        logger.error(f"Directory not found: {args.directory}")
        return
    
    try:
        stats = process_directory(
            args.directory,
            quality=args.quality,
            max_width=args.max_width
        )
        
        if stats:
            total_original = sum(s.original_size for s in stats)
            total_optimized = sum(s.optimized_size for s in stats)
            reduction = (1 - total_optimized/total_original) * 100
            
            logger.info("\nOptimization Summary:")
            logger.info(f"Total images processed: {len(stats)}")
            logger.info(f"Total size reduction: {reduction:.1f}%")
            logger.info(f"Original size: {total_original/1024/1024:.1f}MB")
            logger.info(f"Optimized size: {total_optimized/1024/1024:.1f}MB")
        else:
            logger.info("No images found to optimize")
            
    except Exception as e:
        logger.error(f"Error during optimization: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 