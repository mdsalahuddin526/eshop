# Generated by Django 3.1.1 on 2020-09-26 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
                ('price', models.TextField()),
                ('pr_desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductName', to='sales.productname')),
            ],
        ),
    ]
