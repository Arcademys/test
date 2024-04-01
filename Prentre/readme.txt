# Proyecto Django: Administración de Libros

Este proyecto Django implementa un sistema de administración de libros con las siguientes funcionalidades:

1. **Crear Autor**: Permite ingresar un nuevo autor con su nombre y apellidos.
2. **Crear Editorial**: Permite ingresar una nueva editorial con su nombre y dirección.
3. **Crear Libro**: Permite ingresar un nuevo libro con su título, autor y editorial.
4. **Buscar Libro**: Permite buscar libros por título y muestra los resultados con información del autor y editorial.

## Orden de prueba

1. Ejecuta el servidor Django: `python manage.py runserver`
2. Accede a la URL `http://localhost:8000/` en tu navegador.
3. Crea algunos autores y editoriales utilizando los enlaces correspondientes en la navegación.
4. Crea algunos libros utilizando el formulario correspondiente.
5. Prueba la funcionalidad de búsqueda de libros ingresando un título (parcial o completo) en el formulario de búsqueda.

## Estructura del proyecto

- `administracion/models.py`: Contiene las clases modelo `Autor`, `Editorial` y `Libro`.
- `administracion/forms.py`: Contiene los formularios `AutorForm`, `EditorialForm`, `LibroForm` y `BuscarLibroForm`.
- `administracion/views.py`: Contiene las vistas para crear autores, editoriales, libros y buscar libros.
- `administracion/templates/administracion`: Contiene las plantillas HTML para renderizar los formularios y mostrar los resultados.