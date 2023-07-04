# Apis con http-server de Python 

## CRUD básico para usar localmente API de productos
### Los endpoints - rutas para que puebas una vez corras el programa.
```bash
python3 crud-api-http-server.py
```

### GET /products: Obtiene la lista de todos los productos.
```link
http://127.0.0.1:8000/products
```
### GET /products/{id}: Obtiene los detalles de un producto específico por su ID.
```link
http://127.0.0.1:8000/products/{id}
```
### POST /products: Crea un nuevo producto.
```link
http://127.0.0.1:8000/products
```
### PUT /products/{id}: Actualiza un producto existente por su ID.
```link
http://127.0.0.1:8000/products/{id}
```
### DELETE /products/{id}: Elimina un producto por su ID.
```link
http://127.0.0.1:8000/products/{id}
```
## img del API
<img src="json-productos.png">
