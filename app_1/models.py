from django.db import models

# Create your models here.
class salad_model(models.Model):
    Transaction_date = models.DateField(db_column='Transaction date')
    Supplier = models.CharField(max_length=20)
    Item_description = models.CharField(max_length=20, db_column='Item description')
    Country_of_origin = models.CharField(max_length=20, db_column='Country of origin')
    Quantity = models.IntegerField(db_column='Quantity')
    Unitprice_SGD = models.FloatField(db_column='Unitprice - SGD')
    Price_Incl_Tax = models.FloatField(db_column='Price Incl Tax')
    Discount = models.FloatField(db_column='Discount %')
    Total = models.FloatField(null=False)
    GST = models.FloatField(db_column='GST')
    Total_incl_GST = models.FloatField(db_column='Total incl GST')


    class Meta:
        db_table = 'stopsalad'