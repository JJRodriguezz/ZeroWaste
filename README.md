# 🛍️ Zero Waste - Plataforma de Moda Circular

**Zero Waste** es un marketplace web que promueve el consumo responsable a través de la venta y compra de prendas reutilizadas, gestionando logística, visibilidad y distribución desde una sola plataforma.

---

## 🌟 Funcionalidades principales

- 🎯 **Catálogo filtrado por grupo y subcategoría:** Mujer, Hombre, Niño, Bebé
- 👕 **Vista de productos aleatorios y recientes**
- 🛒 **Formulario para agregar prendas**
- 📊 **Panel de estadísticas y dashboard admin**
- 📦 **Control de ventas, inventario y ganancia**
- 📥 **Exportación a Excel**
- 📄 **Página 'Sobre nosotros'** con historia, misión, visión y servicios
- ☎️ **Página de contacto** con redes sociales

---


## 🛠️ Stack

Python · Django 5.2 · PostgreSQL · Chart.js · openpyxl

---

## 🚀 Correrlo localmente

```bash
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz con los datos de tu base PostgreSQL:

```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

Luego:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📁 Estructura

```
zero_waste_inventory/   configuración del proyecto Django
inventory/              prendas, catálogo, ventas, estadísticas y dashboard
users/                  inicio de sesión, perfil y cambio de contraseña
media/prendas/          imágenes de las prendas
```
