from django.db import models

# Create your models here.

class Processo(models.Model):
  pasta = models.TextField(max_length=250)
  comarca = models.TextField(max_length=250)
  uf = models.CharField(max_length=2)
  
  def __str__(self):       
    return self.pasta+'/'+self.comarca+'/'+self.uf