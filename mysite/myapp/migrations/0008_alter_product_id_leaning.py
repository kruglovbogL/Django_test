# Generated by Django 4.2.5 on 2023-09-21 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id_leaning',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.leaning'),
            preserve_default=False,
        ),
    ]
