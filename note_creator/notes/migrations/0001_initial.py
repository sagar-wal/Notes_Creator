# Generated by Django 2.2.7 on 2019-11-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.CharField(max_length=500)),
                ('moment', models.DateTimeField(verbose_name='Note Created at')),
            ],
        ),
    ]
