#!/usr/bin/env python3
"""
Простой HTTP сервер для раздачи статических файлов книги OASIC
"""
import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://0.0.0.0:{PORT}/")
        httpd.serve_forever()
