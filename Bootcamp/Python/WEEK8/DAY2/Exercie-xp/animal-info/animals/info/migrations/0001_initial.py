# Generated by Django 4.1.4 on 2022-12-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('legs', models.CharField(max_length=200, null=True)),
                ('family', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Familles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]