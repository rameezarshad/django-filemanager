=====
Django Filemanager
=====

A simple and standalone file manager and browser for django projects. Supports multiple instances which can be used within the admin area or for the frontend as well. Its a django app and can be used in multiple projects.

Make sure to have ``base.html`` file and add two blocks ``head`` and ``body`` as described in 6th step. And in your project make sure to have uploads folder inside the MEDIA_ROOT path.

Key features
------------

Standalone file browser and manager
No external dependencies except django
Create Directory to the current path
Upload files to the current path
Download files into zip
Delete any file or directory
Rename them
Search on the basis of filter

Quick start
-----------

1. Download it using pip::
	
	pip install django-webfilemanager
	
2. Add ``filemanager`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'filemanager',
    ]

3. Include the filemanager URLconf in your project urls.py like this::

    url(r'^your-url/', include('filemanager.urls', namespace='filemanager')),


4. Add ``MEDIA_URL`` and ``MEDIA_ROOT`` to the settings.

5. Make sure the base folder defined in your settings for filemanager does exist. By default it is located at ``MEDIA_ROOT/uploads``.

6. If you have 'base.html' in your project then add::
	
	<html>
  		<head>
			{% block head%}{% endblock %}
		</head>
  		<body>
    			{% block content %}{% endblock %}
  		</body>
	</html>

7. If you have problem accessing media files, make sure to these lines only in Debug mode at the end of the URLConf (urls.py) file::
	
	if settings.DEBUG:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
