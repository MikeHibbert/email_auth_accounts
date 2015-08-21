=====
Accounts
=====

A custom email auth for Django

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "accounts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'accounts',
	'bootstrapform',
    )

2. Add this to your settings.py::

	AUTH_USER_MODEL = 'accounts.User'
	
	AUTHENTICATION_BACKENDS = (
	    'django.contrib.auth.backends.ModelBackend',
	    'accounts.backends.EmailAuth',
	)

2. Include the accounts URLconf in your project urls.py like this::

    url(r'^accounts/', include('accounts.urls')),

3. Run `python manage.py migrate` to create the accounts models.

4. user the 'login' and 'register' url names to create links from your home page

EXTRAS

Alternative Login Success URL
-----------------------------

If you want to change the login success url change your urls.py like so::

	...
	from accounts.views import login
	...
	# add a new success url to the account login
	url(r'^accounts/login/$', login, { 'success_url': 'name of view to go to when using resolve()' }, name='login'),
	# import the rest of the accounts urls after so the override is
	# processed first by the urls system
	url(r'^accounts/', include('accounts.urls')),


Alternative Registration Form
-----------------------------

If you want to change the Form object used to display registrations do the following::

	...
	from accounts.views import register
	...
	# add a new success url to the account login
	url(r'^accounts/register/$', register, { 'register_form': MyRegisterFormClass }, name='register'),
	# import the rest of the accounts urls after so the override is
	# processed first by the urls system
	url(r'^accounts/', include('accounts.urls')),
