from django.db import models
from django.utils import timezone

# Create your models here.
class Conteudo(models.Model):
    titulo = models.CharField(max_length=60)
    texto1 = models.TextField()
    foto1 = models.ImageField(upload_to="imagens-eventos")
    texto2 = models.TextField()
    foto2 = models.ImageField(upload_to="imagens-eventos")
    destaque = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if self.destaque:
            count_destaque = Conteudo.objects.filter(destaque=True)
            if count_destaque == 2:
                evento_antigo = Conteudo.objects.filter(destaque=True).order_by('id').first()
                evento_antigo.destaque = False
                evento_antigo.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        
        return self.titulo
    
    
class Evento(models.Model):
    data = models.DateField()
    evento = models.CharField(max_length=60)
    local = models.CharField(max_length=50)
    
    def __str__(self):
        return self.evento