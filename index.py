import subprocess
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Get the port from environment variables, default to 8000
PORT = int(os.getenv("PORT", 8000))

# Command to run the Streamlit app
# We use 'app.py' as the source file for streamlit
command = f"streamlit run app.py --server.port $PORT --server.headless true"

process = subprocess.Popen(command, shell=True)

# Start a simple HTTP server to satisfy Vercel's health checks
class HealthCheckHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Streamlit is running")

with HTTPServer(("", PORT), HealthCheckHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
