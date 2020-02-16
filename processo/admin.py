from django.contrib import admin
from . models import Processo

admin.site.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
  list_display = ('pasta','comarca','uf')
  ordering = ('comarca', 'pasta','uf')
# Register your models here.
