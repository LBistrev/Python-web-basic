# Generated by Django 4.0.2 on 2022-02-18 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='ast_name',
            new_name='last_name',
        ),
    ]
