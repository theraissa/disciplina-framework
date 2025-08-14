# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'f-azul',
        'USER': 'root',
        'PASSWORD': 'admin',
        'PORT': '3306',
        'HOST': 'localhost',        
    }
}
