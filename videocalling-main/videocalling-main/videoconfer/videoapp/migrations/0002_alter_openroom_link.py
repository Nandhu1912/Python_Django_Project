# Generated by Django 4.2.3 on 2023-12-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openroom',
            name='link',
            field=models.CharField(max_length=155),
        ),
    ]