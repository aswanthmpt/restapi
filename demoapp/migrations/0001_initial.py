# Generated by Django 5.0.6 on 2024-06-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('age', models.IntegerField()),
                ('place', models.TextField()),
            ],
        ),
    ]
