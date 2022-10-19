from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)

    def get_admin(self):
        admin = None
        if hasattr(self, 'admin'):
            admin = self.admin
        return admin

    def get_customer(self):
        customer = None
        if hasattr(self, 'customer'):
            customer = self.customer
        return customer

    def get_employee(self):
        employee = None
        if hasattr(self, 'employee'):
            employee = self.employee
        return employee

    class Meta:
            db_table = 'auth_user'

class Unidad(models.Model):
    Nombre_U = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_U

class Rol(models.Model):
    Nombre_R = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_R

class Jerarquia(models.Model):
    Nombre_J = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_J

class Usuario(models.Model):
    ADMIN = 1
    CUSTOMER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (CUSTOMER, 'customer'),
        (EMPLOYEE, 'employee')
    )

    Unidad_1 = 1
    Unidad_2 = 2
    Unidad_3 = 3

    ROLE_CHOICES2 = (
        (Unidad_1, 'Unidad 1'),
        (Unidad_2, 'Unidad 2'),
        (Unidad_3, 'Unidad 3')
    )

    Nombre = models.OneToOneField(User, on_delete=models.CASCADE)
    Rol = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=0)
    Unidad = models.PositiveSmallIntegerField(choices=ROLE_CHOICES2, blank=True, null=True, default=0)

class Tarea(models.Model):
    Nombre_Tarea = models.CharField(max_length=50)
    Responsable = models.OneToOneField(User, on_delete=models.CASCADE)
    Fecha_desde = models.DateField()
    Fecha_hasta = models.DateField()
    Descripcion = models.TextField()

    def __str__(self):
        return self.Nombre_Tarea

class TareaSub(models.Model):
    Nombre_TareaS = models.CharField(max_length=50)
    ResponsableS = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    TareaMadreS = models.ForeignKey(Tarea, on_delete=models.PROTECT)
    Fecha_desdeS = models.DateField()
    Fecha_hastaS = models.DateField()
    DescripcionS = models.TextField()

    def __str__(self):
        return self.Nombre_TareaS