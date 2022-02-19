# Generated by Django 4.0.2 on 2022-02-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_alter_employee_month_of_employment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('company', 'first_name')},
        ),
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-19'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]