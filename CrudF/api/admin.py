from django.contrib import admin

# Register your models here.
from .models import Student
@admin.register(Student)
class StudentA(admin.ModelAdmin):
    list_display = ['id','name'
                         '']

