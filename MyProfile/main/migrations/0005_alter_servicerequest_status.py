# Generated by Django 4.2.4 on 2023-09-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in_progress', 'in_progress'), ('Done', 'done'), ('canceled', 'canceled')], default='pending', max_length=32),
        ),
    ]
