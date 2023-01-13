# Generated by Django 4.1.5 on 2023-01-13 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='customer',
            new_name='seller',
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='account_number',
            field=models.IntegerField(),
        ),
    ]