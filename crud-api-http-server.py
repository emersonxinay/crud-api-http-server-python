from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Datos de ejemplo (simulando una base de datos)
database = [
    {"id": 1, "name": "Producto 1"},
    {"id": 2, "name": "Producto 2"},
    {"id": 3, "name": "Producto 3"}
]

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/products':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Retorna la lista de productos
            response = json.dumps(database)
            self.wfile.write(response.encode('utf-8'))
        elif self.path.startswith('/products/'):
            # Extrae el ID del producto de la ruta
            product_id = int(self.path.split('/')[-1])
            
            # Busca el producto en la base de datos
            product = next((item for item in database if item["id"] == product_id), None)
            
            if product:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                # Retorna el producto encontrado
                response = json.dumps(product)
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                # Retorna un mensaje de error si el producto no existe
                message = "Producto no encontrado."
                self.wfile.write(message.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # Retorna un mensaje de error si la ruta no es válida
            message = "Ruta no encontrada."
            self.wfile.write(message.encode('utf-8'))

    def do_POST(self):
        if self.path == '/products':
            # Lee el cuerpo de la solicitud
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            product = json.loads(post_data)
            
            # Genera un nuevo ID para el producto
            product_id = len(database) + 1
            product["id"] = product_id
            
            # Agrega el producto a la base de datos
            database.append(product)
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Retorna el producto creado con su ID
            response = json.dumps(product)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # Retorna un mensaje de error si la ruta no es válida
            message = "Ruta no encontrada."
            self.wfile.write(message.encode('utf-8'))

    def do_PUT(self):
        if self.path.startswith('/products/'):
            # Extrae el ID del producto de la ruta
            product_id = int(self.path.split('/')[-1])
            
            # Lee el cuerpo de la solicitud
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length).decode('utf-8')
            updated_product = json.loads(put_data)
            
            # Busca el producto en la base de datos
            product_index = next((index for (index, item) in enumerate(database) if item["id"] == product_id), None)
            
            if product_index is not None:
                # Actualiza el producto en la base de datos
                database[product_index] = updated_product
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                # Retorna el producto actualizado
                response = json.dumps(updated_product)
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                # Retorna un mensaje de error si el producto no existe
                message = "Producto no encontrado."
                self.wfile.write(message.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # Retorna un mensaje de error si la ruta no es válida
            message = "Ruta no encontrada."
            self.wfile.write(message.encode('utf-8'))

    def do_DELETE(self):
        if self.path.startswith('/products/'):
            # Extrae el ID del producto de la ruta
            product_id = int(self.path.split('/')[-1])
            
            # Busca el producto en la base de datos
            product_index = next((index for (index, item) in enumerate(database) if item["id"] == product_id), None)
            
            if product_index is not None:
                # Elimina el producto de la base de datos
                deleted_product = database.pop(product_index)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                # Retorna el producto eliminado
                response = json.dumps(deleted_product)
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                # Retorna un mensaje de error si el producto no existe
                message = "Producto no encontrado."
                self.wfile.write(message.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # Retorna un mensaje de error si la ruta no es válida
            message = "Ruta no encontrada."
            self.wfile.write(message.encode('utf-8'))


def run(server_class, handler_class, port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor API ejecutándose en el puerto {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run(HTTPServer, SimpleAPIHandler, 8000)
