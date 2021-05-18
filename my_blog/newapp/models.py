from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=400)
    
    def __str__(self):
        return self.faculty_name

class CertificateType(models.Model):
    certificate_name = models.CharField(max_length=400)

    def __str__(self):
        return self.certificate_name
    
class Department(models.Model):
    department_name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

class Grade(models.Model):
    type = models.CharField(max_length=400)

    def __str__(self):
        return self.type

class Student(models.Model):
    full_name = models.CharField(max_length = 400)
    graduation_year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name