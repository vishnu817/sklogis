#!/usr/bin/env python3
"""
SK Logistics — Local HTTPS Server
Run this on your PC to serve the app over HTTPS on your WiFi network.
"""
import http.server, ssl, os, socket, sys

PORT = 8443
FOLDER = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FOLDER, **kwargs)
    def log_message(self, fmt, *args):
        print(f"  [{self.address_string()}] {fmt % args}")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "YOUR_PC_IP"

cert = os.path.join(FOLDER, "cert.pem")
key  = os.path.join(FOLDER, "key.pem")

if not os.path.exists(cert):
    print("ERROR: cert.pem not found. Run setup first.")
    sys.exit(1)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(cert, key)

server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
server.socket = ctx.wrap_socket(server.socket, server_side=True)

ip = get_local_ip()
print()
print("=" * 52)
print("  SK LOGISTICS — Local HTTPS Server Running")
print("=" * 52)
print()
print(f"  Open on your PHONE (same WiFi):")
print(f"  https://{ip}:{PORT}/SKL_Mobile_App.html")
print()
print(f"  Open on this PC:")
print(f"  https://localhost:{PORT}/SKL_Mobile_App.html")
print()
print("  NOTE: Phone will show a security warning.")
print("  Tap 'Advanced' → 'Proceed anyway' to open.")
print()
print("  Press Ctrl+C to stop the server.")
print("=" * 52)
print()

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n  Server stopped.")
