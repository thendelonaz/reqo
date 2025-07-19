from django.contrib import admin
from .models import Users, jobs, Services
# Register your models here.
admin.site.register(Users)
admin.site.register(jobs)
admin.site.register(Services)