# Generated by Django 3.1.4 on 2020-12-29 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201229_1208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caracteristicas',
            new_name='Features',
        ),
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name': 'Feature', 'verbose_name_plural': 'Features'},
        ),
        migrations.RenameField(
            model_name='features',
            old_name='nome',
            new_name='titulo',
        ),
    ]
