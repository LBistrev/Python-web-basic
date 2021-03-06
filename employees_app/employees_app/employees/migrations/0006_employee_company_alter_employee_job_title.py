# Generated by Django 4.0.2 on 2022-02-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_job_title_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.CharField(choices=[('SoftUni', 'SoftUni'), ('Google', 'Google'), ('Facebook', 'Facebook')], default='SoftUni', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA Engineer'), (3, 'DevOps Specialist')]),
        ),
    ]
