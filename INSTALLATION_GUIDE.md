DJANGO-EDITABLE INSTALLATION GUIDE
=====================

This document is going to try to explain the installation process in detail, however a general knowledge of Python and Django should be noted. For a quick run-through of either or, check http://docs.python.org/reference and http://djangobook.com

##Requirements

Required:
- Python 2.7+
- Django 1.4.1+ (w/ django.contrib.admin installed)

Optional:
- django-tinymce
How to install tinymce is out of the scope of this documentation but django-tinymce should have it's own documentations.


##Getting the app
- For right now, just fork/clone the repo on Github. I'll register with PyPI later.


##Getting Help
Should you run into trouble setting up django-editable, you can email me at ash.courchene@gmail.com & I will respond to you as soon as I can & try to help you to the best of my knowledge.


##Configuration

###Starting django project
If you haven't already, start a django project in your shell terminal & we'll assume your project is in ~/django/myproject/. Type the following:

    $cd ~/django
    $django-admin.py startproject myproject
    $cd myproject
    $python manage.py runserver

You should get a message that says:

    Validating models...

    0 errors found
    Django version 1.4, using settings 'myproject.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    [04/Aug/2012 21:57:52] "GET / HTTP/1.1" 200 1961
    
The date and time is unimportant, but if you open 127.0.0.1:8000 in your browser and get a "It worked!" message, you can be sure it worked.

###Installing django-editable
Next, what you'll want to do is to drop the editable folder into your project. In your settings.py file (probably under on of your myproject folder's) at least the following is needed in your INSTALLED_APPS list:

    INSTALLED_APPS = (
	    'editable',
        'django.contrib.auth',
        #
	    'django.contrib.admin',
	    #
    )'

Since we are already in the settings.py file, be sure to add your absolute path in the TEMPLATE_DIRS = () and  point it to your templates folder.


###Configuring your database
Installing and setting up your database is beyond the scope of this documentation, but once you do, you'll want to configure the DATABASES part in the same settings.py file. I'm going to assume we'll be using sqlite3, because its easiest for local setups.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'YOUR_DB_NAME',
        }
    }

At this point, I like to see if everything works. If your database is set up, and you've made the changes to your settings.py file, go to your shell terminal and get into your project directory (the one that has the manage.py file inside it). From there, run the syncdb command:

    $cd ~/django/myproject/
    $python manage.py syncdb
    
If you get the following, everything works!

    Creating tables ...
	Creating table editable_placeholder
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_user_permissions
    Creating table auth_user_groups
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    Creating table django_admin_log
    
You'll then be prompted to create a superuser, which i do at this point. Just follow the instructions.


###URL Configuration
Once youve installed all the database models, and created your superuser, you're going to want to configure your urls before anything else. Go to your urls.py file in your project and uncomment the django admin urls, and add a url for the django-editable app.
For example:

    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    admin.autodiscover()

    urlpatterns = patterns('', 
        url(r'^admin-edit/', include('editable.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
    
**NOTE**: the include('editable.urls') is vital in your url configuration; 'admin-edit' is just for demonstration purposes only. You can have it be anything you want. url(r'^poopshoots/', include('editable.urls')) works as well.

At this point you can add any other urls and views you need. However, just word of caution, which I think is **extremely** important: When you do create your views, be sure to add 'context_instance = RequestContext(request)' to your render function within your views.

The way django-editable is coded, the {% editable %} tag checks to see if the logged in user is authenticated through context['user']. So it needs that context_instance argument.
This is a simplistic example of how I use it (though I've gotten feedback saying I can do it differently):

    def index(request):
	    return render_to_response('test-page.html', locals(), context_instance = RequestContext(request))

If you know of any other methods, please let me know. I'm curious to find out.


##The Placeholder model & the {% editable %} tag.

###Placeholder
If you haven't guessed, the content of the {% editable %} is stored in a database. It needs data. That's why the Django Admin site is needed, albeit not for site authors.

To create new content data for the {%editable%} tag (or dummy text until the site author can change it), login to the Admin site with the superuser credentials you created earlier. In the main admin site, you will see a section called Editable where you can add, edit and delete new "Placeholders" (it was the best name I could think of at the time). Click 'Add'.

You will see two field forms. One called Location & the other called content.

Location must match the argument given in a {% editable %} if you've already created one. If not, just create a name for it. In this instance I gave it the name 'index_block_one'.
This is a slug field, so use only letters, numbers, underscores and hyphens.

The Content field can be anything you want -- HTML included. So go ahead, get creative.

Once you're done, press save.


###{% editable %}
Back to the templates. Remember 'index_block_one' in the Location field of the Placeholder model? You'll need that for the editable tag. Type in {% editable 'index_block_one' %} anywhere you'd like and save your template.

Check out your new content on your page.

**NOTE**: As of version 0.1.0, when you type in your {% editable %} arguments, use only single quotes. Its a minor (but major) bug that I need to fix.


###{%editable 'admin' %}
If you want a link to where your site author(s) can sign-up just type in {% editable 'admin' %} and it'll create a link to 'your-site.com/the_url_you_used/login'. You can create users through the Django admin site, and give them little to no permissions and will still be able to sign in this way and edit content.

When they do sign in, an "edit" link will appear under where you placed the {% editable %} tag. If they are not sign in, nobody will see it.


## Did I miss anything?
If you find anything, please let me know. Im still a new programmer, so I need all the help I can get. Email me, skype me, whatever. Just don't hate. Thanks.