# Generated by Django 4.1.4 on 2022-12-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locataire',
            name='adress',
            field=models.TextField(),
        ),
    ]