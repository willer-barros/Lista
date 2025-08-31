from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    nome = models.CharField(max_length=255, null=False, blank=False)
    celular = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return f"Nome: {self.nome}"


class Task(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    PRIORIDADE_CHOICES = [
        ("BAIXA", "Baixa"),
        ("MEDIA", "Media"),
        ("ALTA", "Alta"),
        ("URGENTE", "Urgente"),
    ]
    titulo = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default="MEDIA"
    )
    
    data_estimada = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo} ({self.usuario})"
    