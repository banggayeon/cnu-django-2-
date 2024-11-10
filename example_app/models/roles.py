from django.db import models
from example_app.models.user import User

class Module(models.Model):
    name = models.CharField(max_length=50)

class Permission(models.Model):
    name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)