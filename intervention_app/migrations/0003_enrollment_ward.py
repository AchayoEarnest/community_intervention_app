# Generated by Django 5.1.7 on 2025-03-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervention_app', '0002_alter_enrollment_age_intervention'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='ward',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
