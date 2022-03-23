# Generated by Django 4.0.3 on 2022-03-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='salad_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_date', models.DateField(db_column='Transaction date')),
                ('Supplier', models.CharField(max_length=20)),
                ('Item_description', models.CharField(db_column='Item description', max_length=20)),
                ('Country_of_origin', models.CharField(db_column='Country of origin', max_length=20)),
                ('Quantity', models.IntegerField(db_column='Quantity')),
                ('Unitprice_SGD', models.FloatField(db_column='Unitprice - SGD')),
                ('Price_Incl_Tax', models.FloatField(db_column='Price Incl Tax')),
                ('Discount', models.FloatField(db_column='Discount %')),
                ('Total', models.FloatField(db_column='Total')),
                ('GST', models.FloatField(db_column='GST')),
                ('Total_incl_GST', models.FloatField(db_column='Total incl GST')),
            ],
            options={
                'db_table': 'stopsalad',
            },
        ),
    ]
