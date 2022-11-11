from django.db import models

# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=2000, null=True) #because certain links may not have a working address
    name = models.CharField(max_length=2000, null=True)

    def __str__(self) -> str:
        return self.name