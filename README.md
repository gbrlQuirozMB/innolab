# INNOLAB backend

**Correr en ambiente de desarrollo**

    python manage.py runserver --settings=server.settings.dev

**Correr en ambiente de producción**

    python manage.py runserver --settings=server.settings.prod

**Archivo . env**

    DATABASE_ENGINE=django.db.backends.mysql
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_HOST=
    PORT=
    
    EMAIL_HOST=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    EMAIL_PORT=
    
    STATIC_URL=/static/
    STATIC_ROOT=./static/
    MEDIA_URL=/uploads/
    MEDIA_ROOT=./uploads/
    
    ALLOWED_HOSTS=
