from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        payload = json.loads(body or "{}")

        print("Received event:")
        print(json.dumps(payload, indent=2))

        self.send_response(202)
        self.end_headers()
        self.wfile.write(b'{"accepted":true}')


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), Handler)
    print("Listening on http://127.0.0.1:8080")
    server.serve_forever()
