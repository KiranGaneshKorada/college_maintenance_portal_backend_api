# Generated by Django 4.2.7 on 2023-11-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('completed', 'completed'), ('under process', 'under process'), ('issue received', 'issue received')], default='issue received'),
        ),
    ]
