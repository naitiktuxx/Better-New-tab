#!/usr/bin/env python3
"""
ThinkPage Self-Hosting Server
A simple, fast, and multi-threaded Python HTTP server for hosting ThinkPage locally.

Usage:
    python3 server.py [--port 8000] [--host 0.0.0.0]
"""

import argparse
import http.server
import os
import socket
import sys
from http.server import SimpleHTTPRequestHandler

DEFAULT_PORT = 8000
DEFAULT_HOST = "0.0.0.0"

class ThinkPageHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Custom HTTP Request Handler with correct MIME types and PWA headers."""

    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '.webmanifest': 'application/manifest+json',
        '.json': 'application/json',
        '.svg': 'image/svg+xml',
        '.js': 'application/javascript; charset=utf-8',
        '.css': 'text/css; charset=utf-8',
        '.html': 'text/html; charset=utf-8',
        '.wasm': 'application/wasm',
    })

    def end_headers(self):
        # Disable aggressive caching for development / local self-hosting
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        # Clean logging output
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stdout.flush()

def get_lan_ip():
    """Retrieve the local network IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def run_server(host=DEFAULT_HOST, port=DEFAULT_PORT):
    # Ensure current directory is repository root
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    # Use ThreadingHTTPServer if available (Python 3.7+)
    if hasattr(http.server, 'ThreadingHTTPServer'):
        server_class = http.server.ThreadingHTTPServer
    else:
        server_class = http.server.HTTPServer

    try:
        httpd = server_class((host, port), ThinkPageHTTPRequestHandler)
    except OSError as e:
        print(f"Error: Could not bind to port {port}: {e}")
        sys.exit(1)

    lan_ip = get_lan_ip()

    print("=" * 60)
    print("  🚀 ThinkPage Self-Hosting Server")
    print("=" * 60)
    print(f"  • Local URL:   http://localhost:{port}")
    if lan_ip != "127.0.0.1":
        print(f"  • Network URL: http://{lan_ip}:{port}")
    print(f"  • Host:        {host}")
    print(f"  • Serving from: {web_dir}")
    print("=" * 60)
    print("  Press Ctrl+C to stop the server.\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping ThinkPage server...")
        httpd.server_close()
        print("Server stopped gracefully. Goodbye!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ThinkPage Local Self-Hosting Server")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT, help="Port to listen on (default: 8000)")
    parser.add_argument("-H", "--host", type=str, default=DEFAULT_HOST, help="Host address to bind to (default: 0.0.0.0)")
    args = parser.parse_args()

    run_server(host=args.host, port=args.port)
