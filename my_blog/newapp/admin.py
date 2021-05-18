from django.contrib import admin
from .models import CertificateType, Department, Faculty, School, Student, Grade

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(CertificateType)
admin.site.register(Department)
admin.site.register(Grade)