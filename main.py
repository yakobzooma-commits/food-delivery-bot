import threading
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

# Render Port Scan እንዳይዘጋው Dummy Server ማካሄጃ
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# ድረ-ገጹን በጀርባ (Background Thread) ማስነሳት
threading.Thread(target=run_dummy_server, daemon=True).start()
