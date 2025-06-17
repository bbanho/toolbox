#!/usr/bin/env python3
"""
Local development server for PYX Engenharia portfolio.
Provides a simple HTTP server with proper MIME types and error handling.
"""

import http.server
import socketserver
import os
import sys
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

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with proper MIME types and error handling."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DEFAULT_DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Add security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        super().end_headers()
    
    def log_message(self, format, *args):
        logger.info("%s - %s", self.address_string(), format % args)

def run_server(port: int = DEFAULT_PORT, directory: Optional[Path] = None) -> None:
    """Run the local development server."""
    if directory:
        os.chdir(str(directory))
    
    handler = CustomHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        logger.info(f"Serving at http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("\nShutting down server...")
            httpd.server_close()
            sys.exit(0)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Start local development server")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT,
                      help=f"Port to run the server on (default: {DEFAULT_PORT})")
    parser.add_argument("-d", "--directory", type=Path,
                      help="Directory to serve (default: project root)")
    
    args = parser.parse_args()
    run_server(args.port, args.directory) 