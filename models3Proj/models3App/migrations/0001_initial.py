# Generated by Django 2.0.6 on 2019-02-21 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pageNumber', models.IntegerField()),
                ('publishDate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
