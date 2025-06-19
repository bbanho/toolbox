#!/usr/bin/env python3
"""
Local development server for PYX Engenharia portfolio.
Provides a simple HTTP server with proper MIME types and error handling.

Known Issues:
- Different Python versions may require different server commands
- Port conflicts are common - try different ports if default is busy
- Some systems might need 'python' instead of 'python3'
"""

import http.server
import socketserver
import os
import sys
import socket
from pathlib import Path
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Default configuration
DEFAULT_PORT = 8000
DEFAULT_DIRECTORY = Path(__file__).parent.parent
MAX_PORT_ATTEMPTS = 5

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with proper MIME types and error handling."""
    
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, directory=str(DEFAULT_DIRECTORY), **kwargs)
        except Exception as e:
            logger.error(f"Error initializing server: {e}")
            raise
    
    def end_headers(self):
        # Add security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        super().end_headers()
    
    def log_message(self, format, *args):
        if "404" in format % args:
            logger.warning("%s - %s", self.address_string(), format % args)
        else:
            logger.info("%s - %s", self.address_string(), format % args)

    def log_error(self, format, *args):
        logger.error("%s - %s", self.address_string(), format % args)

def find_available_port(start_port: int) -> int:
    """Find an available port starting from start_port."""
    for port in range(start_port, start_port + MAX_PORT_ATTEMPTS):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except socket.error:
            continue
    raise RuntimeError(f"No available ports found between {start_port} and {start_port + MAX_PORT_ATTEMPTS - 1}")

def run_server(port: int = DEFAULT_PORT, directory: Optional[Path] = None) -> None:
    """Run the local development server."""
    try:
        if directory:
            if not directory.exists():
                logger.error(f"Directory not found: {directory}")
                sys.exit(1)
            os.chdir(str(directory))
            logger.info(f"Serving directory: {directory.absolute()}")
        
        # Try to find an available port
        try:
            port = find_available_port(port)
        except RuntimeError as e:
            logger.error(str(e))
            logger.info("Try using a different port with: python local_server.py -p <port>")
            sys.exit(1)
        
        handler = CustomHTTPRequestHandler
        
        with socketserver.TCPServer(("", port), handler) as httpd:
            logger.info(f"Server started successfully!")
            logger.info(f"Access your site at: http://localhost:{port}")
            logger.info("Press Ctrl+C to stop the server")
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                logger.info("\nShutting down server...")
                httpd.server_close()
                sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        logger.info("\nTroubleshooting tips:")
        logger.info("1. Make sure no other service is using the port")
        logger.info("2. Check if you have permissions to access the directory")
        logger.info("3. Try running with 'python' instead of 'python3'")
        logger.info("4. Verify your Python version with 'python --version'")
        sys.exit(1)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Start local development server",
        epilog="For more information, visit: https://github.com/your-org/toolbox"
    )
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT,
                      help=f"Port to run the server on (default: {DEFAULT_PORT})")
    parser.add_argument("-d", "--directory", type=Path,
                      help="Directory to serve (default: project root)")
    parser.add_argument("-v", "--verbose", action="store_true",
                      help="Enable verbose logging")
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    run_server(args.port, args.directory) 