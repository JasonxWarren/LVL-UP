from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=40)
    description= models.CharField(max_length=144)
    dailyz= models.IntegerField()
    duration= models.IntegerField(default="30")
    redeemed= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['dailyz']