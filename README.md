django-editable
===============

* Version: 0.1.0
* Source: http://github.com/Acour83/django-editable
* Full Documentation: https://github.com/Acour83/django-editable/blob/master/INSTALLATION_GUIDE.md
* Creates blocks of content that is editable through the front-end with the use of an {% editable %} template tag.

This app was created for site administrators/authors who don't want to deal with a bulky CMS, or anyone who doesn't want
to give authors back-end access to the Django admin sections. It is fully customizable, and comes with an optional login/
logout page that allows site authors to change semi-static content with a click of a link.


##Requirements

Required:
- Python 2.7+
- Django 1.4.1+ (w/ django.contrib.admin installed)

Optional:
- django-tinymce


##Quick Setup
- Add the editable folder to your project
- Add 'editable' to your INSTALLED_APPS (django.contrib.auth & django.contrib.admin, if not already)
- Configure your database & run manage.py syncdb
- Add **url(r'^any_url_you_like/', include('editable.urls'))** to your urlpatterns
- Sign in to Django Admin Site, create new "Placeholders". (You'll know when you see it)
- Add {% editable 'LOCATION_OF_PLACEHOLDER' %} to your templates. Single quotes for now, please.

##Other Notes
- LOCATION_OF_PLACEHOLDER can be any name as long as it matches the Location field of the Placeholder model in the
Djano admin site. For instance: if you type {% editable 'index_block_one' %}, use 'index_block_one' when creating
a new Placeholder model.
- You will need use RequestContext in your views. This enables the app to check if the site author/administrator is
logged in and/or authenticated. See how to use RequestContext in django documentations.'
- There is a built-in {% editable 'admin' %} tag that gives a link to a login page, if you so should choose to use it.


##Contributing
- If you'd like to contribute, feel free to fork and/or clone.