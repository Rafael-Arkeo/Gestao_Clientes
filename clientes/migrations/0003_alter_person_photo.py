# Generated by Django 3.2.3 on 2021-05-15 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to='cliente_photos', width_field=100),
        ),
    ]
