from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question

admin.site.register(User, UserAdmin)
admin.site.register(Question)