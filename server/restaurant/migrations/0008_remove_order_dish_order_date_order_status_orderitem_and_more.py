# Generated by Django 5.0.1 on 2024-02-14 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_remove_dishcategory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dish',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.dish')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_dish',
            field=models.ManyToManyField(null=True, to='restaurant.orderitem'),
        ),
    ]
