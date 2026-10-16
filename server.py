from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()

        message = (
            f"Hello from Kubernetes!\n"
            f"Container hostname: {hostname}\n"
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

    def log_message(self, format, *args):
        print(format % args, flush=True)

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()