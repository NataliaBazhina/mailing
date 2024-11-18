from django.contrib import admin
from mailing_app import models

admin.site.register(models.Mailing)
admin.site.register(models.Mail)
