## Bienvenido a CoderBlog

___

Este será un blog completo creado con Python y Django. Actualmente falta el sistema de blog, el cual se implementará en las próximas semanas para completar la entrega del proyecto final del curso de Python de Coderhouse, comisión 31075.

___

### Autores

<dl>
    <dt>Cesar Aracena</dt>
    <dd>Sistema de login</dd>
    <dd>Paginas de error</dd>
    <dd>Sistema de búsqueda</dd>
    <dd>Area de admin personalizada</dd>
    <dt>Jose Orozco</dt>
    <dd>Sistema de formato HTML</dd>
    <dd>Sistema de búsqueda</dd>
    <dd>Area de admin personalizada</dd>
    <dt>Esteban Orozco</dt>
    <dd>Sistema de registro</dd>
    <dd>Acerca de nosotros</dd>
    <dd>Sistema de Contáctenos</dd>
</dl>

___

### Como probar

* Clonar o descargar
* En la ruta del proyecto, ejecutar `pip install -r requirements.txt`
* Ejecutar `python manage.py makemigrations`
* Ejecutar `python manage.py migrate`
* Si quiere crear un usuario administrador, ejecutar `python manage.py createsuperuser` y seguir las instrucciones (va a necesitar un super usuario para probar el panel de administracion custom)
* Ejecutar `python manage.py runserver` para ejecutar el servidor
* Navegar a [http://127.0.0.1:8000](http://127.0.0.1:8000)

___

### To Do

* ~~Página de inicio temporal~~
* Página de "Acerca de Nosotros"
* ~~Página de "Contáctenos"~~
* Sistema de busqueda
* ~~Sistema de administracion personalizado~~
* Revisar todos los url's y redirects
* Hacer un loaddata on migrate
