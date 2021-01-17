from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import clientprofile, Qphoto, Qstripe, QregStr

# Register your models here.
admin.site.register(clientprofile)
admin.site.register(Qstripe)
admin.site.register(Qphoto)
admin.site.register(QregStr)

