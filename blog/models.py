from django.conf import settings
from django.db import models
from django.utils import timezone


class Dados(models.Model):
    atendente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    contatar = models.CharField(max_length=200)
    assunto = models.TextField()
    horário = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome