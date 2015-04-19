# ImageField Sample Application 

This an implemention of a tiny image gallery site with single Django application "gallery".

It is meant as an example for my blog post:
[Django Image and File Field Caveats](https://rayed.com/wordpress/?p=1773)

## Setup and Run

Run migrate command to create the database, then run the development server:

    ./manage.py migrate
    ./manage.py runserver

You can access the gallery application on the following URL: [http://localhost:8000/](http://localhost:8000/)


## Galelry application
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


