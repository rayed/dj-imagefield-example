# ImageField Sample Application 

This an implementation of a tiny image gallery site with single Django application "gallery".

It is meant as an example for my blog post:
[Django Image and File Field Caveats](https://rayed.com/posts/2015/04/django-image-and-file-field-caveats/)

## Setup and Run

    python3 -m venv venv             # Create new virtual environment
    . venv/bin/activate              # Activate the new environment
    pip install -r requirements.txt  # Install required packages
    cd apps
    ./manage.py migrate              # Create DB tables
    ./manage.py runserver            # Run development server

You can access the gallery application on the following URL: <http://localhost:8000/>


## Gallery application
Most of the code exists under "apps/gallery", including the model, views, url routing (urls.py), and templates.


## settings.py changes

Changes in "apps/apps/settings.py":

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, '..','www','media')


## urls.py changes

    from django.conf import settings
    from django.conf.urls.static import static
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


