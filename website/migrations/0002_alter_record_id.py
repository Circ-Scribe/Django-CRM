# Generated by Django 5.1.5 on 2025-02-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
