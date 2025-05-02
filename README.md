# 🛒 Página Kiosko - Django

Proyecto creado con Django para la entrega final del curso Python Flex de CoderHouse. Desarrollado por Facundo Bustos Bean.

Este proyecto es una aplicación web desarrollada con Django para la gestión básica de un kiosko. Permite administrar productos, clientes, ventas y mensajería entre clientes y administradores.

Incluye gestión de productos (nombre, precio, categoría y stock), gestión de clientes (nombre, email, teléfono, vinculados a un usuario), ventas (producto, cliente, cantidad y fecha), y un sistema de mensajería funcional donde los clientes pueden enviar mensajes al kiosko, y los superusuarios pueden responder desde un chat compartido entre ellos.

Tecnologías utilizadas: Python 3.12, Django 5.2, SQLite, HTML, CSS, y Bootstrap en algunas vistas. El proyecto está organizado en una app principal llamada `Kiosko`, y otra app llamada `mensajeria`.

Para usar la aplicación: clonar el repositorio, crear y activar un entorno virtual, instalar las dependencias con `pip install -r requirements.txt`, aplicar las migraciones con `python manage.py makemigrations` y `python manage.py migrate`, crear un superusuario con `python manage.py createsuperuser`, y correr el servidor con `python manage.py runserver`. Luego, se puede acceder al sitio desde `http://127.0.0.1:8000/` y al panel de administración desde `http://127.0.0.1:8000/admin/`.

Este proyecto fue creado por **Facundo Bustos Bean** como parte del curso **Python Flex - CoderHouse**.

Estado actual del proyecto:

- ✅ Productos: completado  
- ✅ Clientes: completado  
- 🕓 Ventas: en pausa  
- ✅ Mensajería: completado

¡Gracias por visitar el repositorio!
