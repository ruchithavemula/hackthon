# Generated by Django 5.1.3 on 2024-12-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_remove_session_date_remove_session_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
