# Generated by Django 3.2.3 on 2021-05-15 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cliente_photos'),
        ),
    ]
