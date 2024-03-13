from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

host = "localhost"
port = 8000

def block_request(self):
    self.send_response(403)  # Send a Forbidden status code
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    self.wfile.write(b"Request blocked by firewall.")

def handle_request(self):
    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    self.end_headers()
    self.wfile.write(b'{"message": "Request allowed."}')

def is_suspicious(headers, path, body):
    # Check for specific exploit headers
    suspicious_headers = ["suffix", "c1", "c2"]
    for header in suspicious_headers:
        if header in headers:
            return True

    # Check for suspicious path or query parameters
    parsed_path = urlparse(path)
    if 'class.module.classLoader' in parsed_path.query:
        return True

    # Inspect the body for suspicious patterns
    if "class.module.classLoader" in body or "java.io.InputStream" in body:
        return True

    return False

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # For simplicity, we'll allow all GET requests
        handle_request(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length).decode('utf-8')

        if is_suspicious(self.headers, self.path, post_body):
            block_request(self)
        else:
            handle_request(self)

if __name__ == "__main__":
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
