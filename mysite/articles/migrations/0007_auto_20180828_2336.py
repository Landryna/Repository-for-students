# Generated by Django 2.1 on 2018-08-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20180828_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ocena',
            field=models.CharField(default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
