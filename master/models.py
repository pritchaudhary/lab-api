from django.db import models

# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "departments"
        verbose_name="Departments"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name