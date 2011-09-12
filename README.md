Teachcork
==========
Here you will find technical documentation for the teachcork project.

## What we use
This is a brief list of what we use, for specific versions and details refer to the requirements.pip and requirements-dev.pip files

Single package website and installation command is supplied here for documentation purposes if you are setting up your
development environment you *MUST* perform a single: `pip install -r requirements-dev.pip`

First we need a virtual mahchine. We use [python2.7](http://www.python.org) -- `brew install python` or `whatever`
to handle pithon packages we use [pip](http://pypi.python.org/pypi/pip) -- `easy_install pip`
Then we need a way to isolate the project environment using [virtualenv](http://pypi.python.org/pypi/virtualenv) -- `pip install virtualenv`
and just because we are a bunch of lazy fat asses we use [virtualenvwraper](http://pypi.python.org/pypi/virtualenvwraper) -- `pip install virtualenvwrapper`

Teachcorck website is powered with a pony: [django1.3](http://www.djangoproject.com) -- `pip install django`

And thats pretty much what you have to know by now of what we use.


Layout
-------
The following documentation drives you trough the project code layout.
Basically its just another django project layout but may be you are not familiar
with some components like configuration files from nosetests, or tox.

In addition all is figured out to work on a Continious Integration multiple environments
this is why several settings.py files are present.

_Right now this section is under contruction so keep watching for changes._

*NOTE:* Should we wrap the code with an django package? (eg. setuptools stuff)
                                
    teachcork/
        settings.py             # Production settings
        settings-dev.py         # Development settings
        settings-testing.py     # Testing settings
        urls.py                 # Main url mapper. Acts as a router to inner url mappers
                                
        manage.py               # Django management script (we may add some commands here later)
                                
        tox.ini                 # Tox configuration (see http://pypi.python.org/pypi/tox)
                                
        setup.cfg               # Nose configuration
                                
        app/                    # Teach cork website (Should we rename it to 'website' or something more descriptive?)
            urls.py             # Url mapping for this specific app. (This is recomended so the app may live outside the project)
                                
            models/             # Models you know we <3 MVC strategy (really django force us, but still loving it)
            views/              # Views here are much like controllers in gae and with django1.3 we have class hineritance too (eg. AbstracController)

