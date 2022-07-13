from django.db import models

# Create your models here.
class EmployeRegister(models.Model):
    full_name = models.CharField(max_length = 69)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name