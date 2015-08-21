=====
Accounts
=====

A custom email auth for Django

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'accounts',
	'django_forms_bootstrap',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^accounts/', include('accounts.urls')),

3. Run `python manage.py migrate` to create the accounts models.

4. user the 'login' and 'register' url names to create links from your home page
