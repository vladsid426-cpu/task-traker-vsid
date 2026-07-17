from django.contrib import admin
from .models import Task,Comment
# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)

admin.site.register(Register)
admin.site.register(Login)