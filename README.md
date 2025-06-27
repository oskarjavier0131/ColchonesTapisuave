# Colchones TapiSuave 🛏️

Una tienda en línea moderna y responsiva para la venta de colchones, desarrollada con Django y tecnologías web modernas.

## 🌟 Características

- **Catálogo de productos**: Navegación por categorías de colchones
- **Detalles de producto**: Información completa con imágenes y especificaciones
- **Diseño responsivo**: Optimizado para dispositivos móviles y escritorio
- **Interfaz moderna**: UI limpia y atractiva con gradientes y efectos visuales
- **Gestión de inventario**: Panel de administración integrado

## 🛠️ Tecnologías

- **Backend**: Django 5.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Deployment**: Railway

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/colchonesTapiSuave.git
cd colchonesTapiSuave
```

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta las migraciones:
```bash
python manage.py migrate
```

5. Carga datos de ejemplo:
```bash
python manage.py load_sample_data
```

6. Inicia el servidor:
```bash
python manage.py runserver
```

## 📱 Uso

Visita `http://localhost:8000` para ver la tienda en funcionamiento.

### Panel de Administración
Accede a `http://localhost:8000/admin/` para gestionar productos y categorías.

## 🌐 Demo en Vivo

Visita la demo: [TapiSuave Store](https://tu-proyecto.railway.app)

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

---

Desarrollado con ❤️ para brindar el mejor descanso