from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Service)
admin.site.register(Aboutme)
admin.site.register(Feedback)
