DATABASES = {
    'default': {
        'NAME': 'myDB',
        'USER': 'Chencho',
        'PASSWORD': 'Admin@123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}