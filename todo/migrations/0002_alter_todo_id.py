# Generated by Django 5.0.1 on 2024-01-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
