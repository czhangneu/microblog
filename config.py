# cross-site request forgery prevention, which makes your app more secure
CSRF_ENABLED = True
#only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate
# a form.
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name' : 'Google', 'url' : 'https://www.google.com/accounts/o8/id' },
    {'name' : 'Yahoo', 'url' : 'https://me.yahoo.com'},
    {'name' : 'Flickr', 'url': 'http://www.flickr.com/<username>'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
