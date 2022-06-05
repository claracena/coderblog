## Bienvenido a CoderBlog

___

Este es el proyecto intermedio del curso de Python, camada 31075 de Coderhouse (dictado por Octavio Lafourcade), realizado por Orozco José, Orozco Esteban y Aracena César en Junio 2022.

Si no desea descargar este proyecto pero ver su funcionamiento, puede ver el siguiente video: https://youtu.be/72iiFTjUDTo

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
* En la base de datos ya existirá un super usuario para realizar pruebas con los siguientes datos:

   Nombre de usuario: admin

   Contraseña: admin

* Si desea puede crear otro super usuario ejecutando el comando `python manage.py createsuperuser`
* Debido a que el programa está configurado con `Debug = False` para manejar correctamente las páginas de error, se debe ejecutar `python manage.py runserver --insecure` para ejecutar el servidor
* Navegar a [http://127.0.0.1:8000](http://127.0.0.1:8000)

___

### Que probar

Actualmente se puede ver:

* Acerca de Nosotros: Nombres y fotos reales, traídos de la base de datos
* Contáctenos: Formulario habilitado, guardando cada contacto en la base de datos
* Registro / Inicio de Sesión
* Editar Perfil: Al estar registrado, se puede cambiar el perfil del usuario
* Configuración: Los super usuarios pueden cambiar la información visible en "Acerca de Nosotros"
* Búsqueda: Realiza búsqueda de usuarios por nombre de usuario, nombre y apellido
___

### To Do

* ~~Página de inicio temporal~~
* ~~Página de "Acerca de Nosotros"~~
* ~~Página de "Contáctenos"~~
* ~~Sistema de busqueda~~
* ~~Sistema de administracion personalizado~~
* ~~Revisar todos los url's y redirects~~
* ~~Hacer un loaddata on migrate~~
* ~~Paginas de error personalizadas~~
* ~~Edicion de perfiles con cambio de password~~
