from django.db import models

# Create your models here.
class Goals(models.Model):

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