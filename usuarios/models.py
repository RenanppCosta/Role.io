from django.db import models

# Create your models here.
class Events(models.Model):
    STATUS_CHOICES = [
    ("Planejando", "Planejando"),
    ("Ativo", "Ativo"),
    ("Cancelado", "Cancelado"),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Planejando")

    def __str__(self):
        return self.title

