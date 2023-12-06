from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    name = models.CharField(max_length=256)
    guid = models.CharField(max_length=36, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.edited:
            self.edited = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Factory(BaseModel):
    long_name = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    f_address = models.CharField(max_length=256)


class DepartmentType(BaseModel):
    pass


class Department(BaseModel):
    factory = models.ForeignKey('Factory', on_delete=models.PROTECT)
    id_parent = models.IntegerField(blank=True)
    date_begin = models.DateField()
    date_end = models.DateField(blank=True)
    department_type = models.ForeignKey('DepartmentType', on_delete=models.PROTECT)
