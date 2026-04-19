import http.server
import socketserver
import os

PORT = 8080

class NexusHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
      
        if self.path == '/n.ps1':
            print("\n[!] ¡#! Download...")
  
            os.system("termux-vibrate -d 1000")
            os.system("termux-tts-speak 'Conexión exitosa. Nexus activo.'")
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
      
print(f"[*] Nexus Listener activo en el puerto {PORT}...")
with socketserver.TCPServer(("", PORT), NexusHandler) as httpd:
    httpd.serve_forever()
