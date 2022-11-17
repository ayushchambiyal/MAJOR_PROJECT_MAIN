# Generated by Django 4.1.2 on 2022-11-01 12:50

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191)),
                ('price', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.models.filepath)),
            ],
        ),
    ]