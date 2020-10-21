# Generated by Django 3.1.2 on 2020-10-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(default='', max_length=300)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('severity', models.CharField(max_length=1000)),
                ('issues', models.CharField(max_length=1000)),
                ('date_admitted', models.DateField()),
                ('care_provided', models.CharField(max_length=1000)),
                ('care_needed', models.CharField(max_length=1000)),
                ('health_level', models.CharField(max_length=1000)),
            ],
        ),
    ]
