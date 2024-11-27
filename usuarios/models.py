from django.db import models
import secrets

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

# class Guests(models.Model):
#     STATUS_CHOICES = [
#     ("AC", "Aguardando Confirmação"),
#     ("CO", "Confirmado"),
#     ("RE", "Recusado"),
#     ]
#     event = models.ForeignKey(Events, related_name="guests", on_delete=models.CASCADE)
#     name = models.CharField(max_length=150)
#     whatsapp = models.CharField(max_length=25, null=True, blank=True)
#     max_companion = models.PositiveIntegerField(default=0)
#     token = models.CharField(max_length=25)
#     status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="AC")

#     def save(self, *ars, **kwargs):
#         if not self.token:
#             self.token = secrets.token_urlsafe(16)
#         super(Guests, self).save(*ars, **kwargs)
