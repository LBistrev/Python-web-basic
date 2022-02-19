# Generated by Django 4.0.2 on 2022-02-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_egn_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA Engineer'), (3, 'DevOps Specialist')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, default='NO NAME', max_length=40, null=True),
        ),
    ]
