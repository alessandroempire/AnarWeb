1) Instalar postgresql

2) convertirse en usuario postgres: sudo -i -u postgres

3) crear usuario anar: createuser -s -P anar

4) introducir password anarpass

5) Crear base de datos: createdb anardb

6) volver a ser superusuario

7) instalar libpq-dev

8) instalar requirements.pip (sudo pip install -vr requirements.pip)

9) En caso que psycopg2 no se instale correctamente haga lo siguiente:

9.1) Es necesario instalar psycopg2 sin la herramienta pip, de la siguiente manera: sudo apt-get install python-psycopg2

9.2) Ejecutar de nuevo el comando sudo pip install -r requirements.pip para terminar de instalar los paquetes restantes

-- En caso que ejecute el comando y ya esten instalados todo los paquetes, saldra el mensaje "Requirement already satisfied)

10) Instalar el modulo nested_inlines: pip install git+git://github.com/Soaa-/django-nested-inlines.git#egg=django-nested-inlines

-- A ese nivel, ya se deberia poder ver la interfaz del sistema. Probar con: python manage.py runserver y visitando: localhost:8000--

11) En la carpeta del proyecto sincronizar la base de datos python manage.py syncdb (si pide usuario y password, puede usar usuario: anar y password: anarpass, igual como esta estipulado en el settings.py)

12) Migrar la base de datos python manage.py migrate

13) Convertirse en usuario postgres, accesar a la base de datos asi: psql anardb y luego ejecutar inserts.sql asi: \i inserts.sql

13) Reconstruir indice de busqueda python manage.py rebuild_index

14) Ejecutar el siguiente caso de prueba: En la seccion de busqueda escribir la palabra Yacimiento y hacer click en el boton buscar. El sistema deberia mostrar varios elementos en la pagina de resultados
