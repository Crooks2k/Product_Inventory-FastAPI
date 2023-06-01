# Proyecto de CRUD de inventario - FastAPI

## Descripción

Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de inventariado

## Funcionalidades

- Obtener los datos de los productos
- Obtener un producto por su ID
- Crear una nuevo producto en el inventario
- Actualizar una producto existente
- Eliminar un item del inventario

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Crooks2k/Product_Inventory-FastAPI.git
```

2. Navega al directorio del proyecto:
```bash
cd Product_Inventory-FastAPI
```
3. Cambiar el origen del repositorio para conectarlo a un repositorio propio
```bash
git remote -v
```
```bash
git remote remove origin
```
```bash
git remote add origin <nueva_url_del_repositorio>
```
4. Inicializa venv
```bash
python -m venv venv
```
```bash
 python venv/scripts/activate
```
5. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Uso

1. Inicia la aplicación:
```bash
uvicorn main:app --reload
```

2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/docs


3. Prueba las diferentes rutas disponibles para realizar operaciones CRUD en el inventario.


