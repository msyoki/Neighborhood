# Generated by Django 2.0.2 on 2020-11-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0020_business_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
