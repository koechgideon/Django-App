# Generated by Django 3.0.4 on 2020-03-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200307_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]
