# Generated by Django 2.2.7 on 2019-12-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0004_auto_20191206_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'В работе'), (3, 'Выполено')], default=1),
        ),
    ]
