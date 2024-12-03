# Generated by Django 5.1.2 on 2024-12-02 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('whatsapp', models.CharField(blank=True, max_length=25, null=True)),
                ('max_companion', models.PositiveIntegerField(default=0)),
                ('token', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('AC', 'Aguardando Confirmação'), ('CO', 'Confirmado'), ('RE', 'Recusado')], default='AC', max_length=2)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='usuarios.events')),
            ],
        ),
    ]
