#!/usr/bin/env python3
"""Minimal static server for WoW Portal."""
import http.server
import os

PORT = int(os.environ.get("PORT", 8080))

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({".html": "text/html; charset=utf-8"})

with http.server.HTTPServer(("0.0.0.0", PORT), handler) as httpd:
    print(f"Serving WoW Portal on port {PORT}")
    httpd.serve_forever()
