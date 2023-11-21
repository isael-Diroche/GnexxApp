from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Configuraciones del Gmail
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "isaeldiroche00@gmail.com"
EMAIL_HOST_PASSWORD = "mmhxgqexbxslhnuf"

# Otras configuraciones específicas del entorno de desarrollo...