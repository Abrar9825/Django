# Generated by Django 5.1 on 2024-10-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m1', models.CharField(max_length=5)),
                ('m3', models.CharField(max_length=5)),
                ('m4', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
