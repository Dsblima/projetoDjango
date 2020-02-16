from django.db import models

# Create your models here.
class Planilha(models.Model):
  nome = models.TextField(max_length=250)
  cliente = models.TextField(max_length=250)
  arquivo = models.FileField(upload_to='uploads/')
  
  def __str__(self):       
    return self.nome+'/'+self.cliente+'/'+self.arquivo