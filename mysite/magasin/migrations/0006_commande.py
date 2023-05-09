# Generated by Django 4.1.7 on 2023-03-13 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_produitnc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCde', models.DateField(default=datetime.date.today, null=True)),
                ('totalCde', models.DecimalField(decimal_places=3, max_digits=10)),
                ('produits', models.ManyToManyField(to='magasin.produit')),
            ],
        ),
    ]
