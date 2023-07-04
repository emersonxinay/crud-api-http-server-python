from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configura la respuesta de la API
        self.send_response(200)  # Código de estado HTTP 200 OK
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Envía la respuesta
        message = "¡Hola  desde la API básica!"
        self.wfile.write(message.encode('utf-8'))

        
def run(server_class, handler_class, port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor API ejecutándose en el puerto {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    # Ejecuta el servidor en el puerto 8000
    run(HTTPServer, SimpleAPIHandler, 8000)
