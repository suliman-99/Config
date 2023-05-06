# Generated by Django 4.2.1 on 2023-05-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0002_alter_config_force_update_alter_config_need_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='backup_domain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='deep_update_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='force_update',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='config',
            name='need_update',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='config',
            name='normal_update_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
