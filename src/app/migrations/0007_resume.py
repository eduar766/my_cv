# Generated by Django 3.0.6 on 2020-06-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_description_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('fecha_inicio', models.CharField(max_length=20)),
                ('fecha_final', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=20)),
            ],
        ),
    ]
