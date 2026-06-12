#!/usr/bin/env python3
"""Persistence API for World Cup Predictor.
   GET  /predictions.json  - retrieve saved predictions
   POST /save-predictions   - save predictions to file
   Runs on port 8082 by default."""
import http.server
import json
import os
import sys

DATA_FILE = os.environ.get('WCUP_DATA_FILE', '/opt/wcup-predictor/data/predictions.json')
PORT = int(os.environ.get('WCUP_PORT', '8082'))


class SyncHandler(http.server.BaseHTTPRequestHandler):
    """Simple REST handler for saving/loading predictions."""

    def do_OPTIONS(self):
        self._cors_headers()
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/predictions.json':
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as f:
                    data = f.read()
                self._respond(200, 'application/json', data.encode())
            else:
                self._respond(200, 'application/json',
                              json.dumps({'state': {}}).encode())
        else:
            self._respond(404, 'text/plain', b'Not found')

    def do_POST(self):
        if self.path == '/save-predictions':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            with open(DATA_FILE, 'w') as f:
                f.write(body.decode())
            print(f"[server] Saved {len(body)} bytes to {DATA_FILE}")
            self._respond(200, 'application/json',
                          json.dumps({'status': 'saved'}).encode())
        else:
            self._respond(404, 'text/plain', b'Not found')

    def _cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def _respond(self, code, content_type, body):
        self.send_response(code)
        self._cors_headers()
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"[server] {args[0]} {args[1]} {args[2]}")


if __name__ == '__main__':
    print(f"WCup Predictor Server — listening on :{PORT}")
    print(f"  Data file: {DATA_FILE}")
    server = http.server.HTTPServer(('0.0.0.0', PORT), SyncHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()
