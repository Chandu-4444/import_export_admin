from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin

@admin.register(Student)
class StudentResources(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'age']

    class Meta:
        model = Student
        fields = ['name', 'age']