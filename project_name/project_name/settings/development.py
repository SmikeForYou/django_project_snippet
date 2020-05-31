from .production import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = "%5_=+^yqrtb=1h(g(ztq7s6mk$d@fpzd_&52kr*6qx^o=*4^x7"
SUPERADMINS = [("superadmin@email.com", "superadmin", "superadminpassword")]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "project_name",
        "USER": "project_name",
        "PASSWORD": "project_name",
        "HOST": "postgres",
        "PORT": 5432,
    }
}
