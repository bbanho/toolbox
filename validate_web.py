#!/usr/bin/env python3
"""
Web validation script for PYX Engenharia portfolio.
Validates HTML, accessibility, and performance metrics.
"""

import os
from pathlib import Path
import logging
import argparse
import json
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from dataclasses import dataclass
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ValidationResult:
    """Results from web validation."""
    url: str
    status_code: int
    load_time: float
    issues: List[str]
    warnings: List[str]

class WebValidator:
    """Validates web pages for various aspects."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; PYX-Validator/1.0)'
        })
    
    def validate_page(self, path: str = "/") -> ValidationResult:
        """Validate a single page."""
        url = urljoin(self.base_url, path)
        issues = []
        warnings = []
        
        try:
            # Measure load time
            start_time = requests.utils.time()
            response = self.session.get(url)
            load_time = requests.utils.time() - start_time
            
            # Basic checks
            if response.status_code != 200:
                issues.append(f"HTTP {response.status_code}")
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check meta tags
            if not soup.find('meta', attrs={'name': 'description'}):
                warnings.append("Missing meta description")
            
            # Check images
            for img in soup.find_all('img'):
                if not img.get('alt'):
                    issues.append(f"Image missing alt text: {img.get('src', 'unknown')}")
                if not img.get('loading'):
                    warnings.append(f"Image missing loading attribute: {img.get('src', 'unknown')}")
            
            # Check links
            for link in soup.find_all('a'):
                if not link.get('href'):
                    issues.append("Link missing href attribute")
                elif link['href'].startswith('#'):
                    if not soup.find(id=link['href'][1:]):
                        issues.append(f"Broken anchor link: {link['href']}")
            
            # Check performance
            if load_time > 3.0:
                warnings.append(f"Slow page load: {load_time:.2f}s")
            
            return ValidationResult(
                url=url,
                status_code=response.status_code,
                load_time=load_time,
                issues=issues,
                warnings=warnings
            )
            
        except Exception as e:
            logger.error(f"Error validating {url}: {e}")
            return ValidationResult(
                url=url,
                status_code=0,
                load_time=0,
                issues=[f"Validation error: {str(e)}"],
                warnings=[]
            )

def validate_site(base_url: str, paths: List[str]) -> Dict[str, ValidationResult]:
    """Validate multiple pages of the site."""
    validator = WebValidator(base_url)
    results = {}
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_path = {
            executor.submit(validator.validate_page, path): path
            for path in paths
        }
        
        for future in concurrent.futures.as_completed(future_to_path):
            path = future_to_path[future]
            try:
                result = future.result()
                results[path] = result
                
                # Log results
                if result.issues:
                    logger.error(f"\nIssues found in {path}:")
                    for issue in result.issues:
                        logger.error(f"  - {issue}")
                
                if result.warnings:
                    logger.warning(f"\nWarnings for {path}:")
                    for warning in result.warnings:
                        logger.warning(f"  - {warning}")
                
                logger.info(f"Validated {path} in {result.load_time:.2f}s")
                
            except Exception as e:
                logger.error(f"Failed to validate {path}: {e}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Validate web pages")
    parser.add_argument(
        "-u", "--url",
        default="http://localhost:8000",
        help="Base URL to validate (default: http://localhost:8000)"
    )
    parser.add_argument(
        "-p", "--paths",
        nargs="+",
        default=["/"],
        help="Paths to validate (default: /)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output JSON file for results"
    )
    
    args = parser.parse_args()
    
    try:
        results = validate_site(args.url, args.paths)
        
        # Print summary
        total_issues = sum(len(r.issues) for r in results.values())
        total_warnings = sum(len(r.warnings) for r in results.values())
        
        logger.info("\nValidation Summary:")
        logger.info(f"Pages validated: {len(results)}")
        logger.info(f"Total issues: {total_issues}")
        logger.info(f"Total warnings: {total_warnings}")
        
        # Save results if output file specified
        if args.output:
            output_data = {
                path: {
                    "url": result.url,
                    "status_code": result.status_code,
                    "load_time": result.load_time,
                    "issues": result.issues,
                    "warnings": result.warnings
                }
                for path, result in results.items()
            }
            
            args.output.write_text(json.dumps(output_data, indent=2))
            logger.info(f"Results saved to {args.output}")
        
        return 1 if total_issues > 0 else 0
        
    except Exception as e:
        logger.error(f"Error during validation: {e}")
        return 1

if __name__ == "__main__":
    exit(main()) 