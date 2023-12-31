from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Factory(BaseModel):
    long_name = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    f_address = models.CharField(max_length=256, null=True)

    class Meta:
        verbose_name_plural = 'Factories'


class DepartmentType(BaseModel):
    pass


class Department(BaseModel):
    factory = models.ForeignKey('Factory', on_delete=models.PROTECT)
    id_parent = models.IntegerField(null=True)
    date_begin = models.DateField()
    date_end = models.DateField(null=True)
    department_type = models.ForeignKey('DepartmentType', on_delete=models.PROTECT)
