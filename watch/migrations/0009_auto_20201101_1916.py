# Generated by Django 2.0.2 on 2020-11-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0008_healthdepartment_policeauthorities'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthdepartment',
            name='contacts',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='policeauthorities',
            name='contacts',
            field=models.IntegerField(null=True),
        ),
    ]