# Generated by Django 4.2.7 on 2023-12-10 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_issue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='category',
            field=models.CharField(choices=[('classroom', 'classroom'), ('laboratories', 'laboratories'), ('restrooms', 'restrooms'), ('library', 'library'), ('common areas', 'common areas'), ('cafeteria', 'cafeteria'), ('outdoor', 'outdoor'), ('transport', 'transport'), ('halls', 'halls')], default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='images',
            field=models.ImageField(blank=True, upload_to='complaint_images/'),
        ),
    ]