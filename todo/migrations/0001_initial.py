# Generated by Django 5.0.1 on 2024-01-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('TD', 'Todo'), ('IN', 'In Progress'), ('CD', 'Completed')], max_length=2)),
            ],
        ),
    ]
