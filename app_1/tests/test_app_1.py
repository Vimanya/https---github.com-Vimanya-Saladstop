from datetime import datetime
import json
import pandas as pd
import pytest
from django import urls
from app_1.models import salad_model



@pytest.mark.django_db
def test_get_homepage(client):
    transaction = salad_model.objects.create(
        Transaction_date = "2021-1-1", 
        Supplier = "Eat Wide Awake FOOD", 
        Item_description = "[DRESSING] Mixed Berries Vinaigrette", 
        Country_of_origin = "Singapore", 
        Quantity = 2, 
        Unitprice_SGD = 7.17, 
        Price_Incl_Tax = 7.67, 
        Discount = 0.00, 
        Total = 14.34, 
        GST = 15.34, 
        Total_incl_GST = 29.68
    )

    response = client.get('/')

    assert response.status_code == 200
    assert transaction.Transaction_date == "2021-1-1"
    assert transaction.Supplier == "Eat Wide Awake FOOD"
    assert transaction.Item_description == "[DRESSING] Mixed Berries Vinaigrette"
    assert transaction.Country_of_origin == "Singapore"
    assert transaction.Quantity == 2
    assert transaction.Unitprice_SGD == 7.17
    assert transaction.Price_Incl_Tax == 7.67
    assert transaction.Discount == 0.00
    assert transaction.Total == 14.34
    assert transaction.GST == 15.34
    assert transaction.Total_incl_GST == 29.68


@pytest.mark.django_db
def test_get_createpage(client):
    transaction = salad_model.objects.create(
        Transaction_date = "2021-1-1", 
        Supplier = "Eat Wide Awake FOOD", 
        Item_description = "[DRESSING] Mixed Berries Vinaigrette", 
        Country_of_origin = "Singapore", 
        Quantity = 2, 
        Unitprice_SGD = 7.17, 
        Price_Incl_Tax = 7.67, 
        Discount = 0.00, 
        Total = 14.34, 
        GST = 15.34, 
        Total_incl_GST = 29.68
    )
    response = client.get('/summary_saladstop/')
    assert response.status_code == 200



@pytest.mark.django_db
def test_Data_summary(client):
    salad_model.objects.create(
        Transaction_date = "2021-2-2", 
        Supplier = "new", 
        Item_description = "apple", 
        Country_of_origin = "China", 
        Quantity = 10, 
        Unitprice_SGD = 3.5, 
        Price_Incl_Tax = 5.5, 
        Discount = 0.00, 
        Total = 88.7, 
        GST = 67.15, 
        Total_incl_GST = 90
    )
    salad_model.objects.create(
        Transaction_date = "2021-3-4", 
        Supplier = "Eat Wide Awake FOOD", 
        Item_description = "[DRESSING] Mixed Berries Vinaigrette", 
        Country_of_origin = "Singapore", 
        Quantity = 2, 
        Unitprice_SGD = 7.17, 
        Price_Incl_Tax = 7.67, 
        Discount = 0.00, 
        Total = 14.34, 
        GST = 15, 
        Total_incl_GST = 40
    )

    fromdate ='2021-2-1'
    todate = '2021-3-6'
    fromdate = datetime.strptime(fromdate, '%Y-%m-%d') 
    todate = datetime.strptime(todate, '%Y-%m-%d')
    newdata = salad_model.objects.filter(Transaction_date__range =[fromdate,todate])
    df = pd.DataFrame(list(newdata.values())).fillna(0) 
    avgCostWoGst = df.groupby(df['Item_description'].str.lower())['Unitprice_SGD'].mean().reset_index().sort_values(by=['Unitprice_SGD'], ascending = False) 
    avgCostWoGstdf = avgCostWoGst.to_json(orient = "records") 
    test_data = []
    test_data = json.loads(avgCostWoGstdf)
  
    response = client.get('/summary_saladstop/',params=newdata)

    assert response.status_code == 200
    assert response.context['total_price'] == 130
    assert response.context['big_qt'] == 'china'
    assert response.context['data'] == test_data
     
@pytest.mark.django_db
def test_submit_btn(client):
    salad_model.objects.create(
        Transaction_date = "2020-2-7", 
        Supplier = "new", 
        Item_description = "apple", 
        Country_of_origin = "China", 
        Quantity = 10, 
        Unitprice_SGD = 3.5, 
        Price_Incl_Tax = 5.5, 
        Discount = 0.00, 
        Total = 88.7, 
        GST = 67.15, 
        Total_incl_GST = 98.68
    )
    salad_model.objects.create(
        Transaction_date = "2020-2-11", 
        Supplier = "Eat Wide Awake FOOD", 
        Item_description = "[DRESSING] Mixed Berries Vinaigrette", 
        Country_of_origin = "Singapore", 
        Quantity = 2, 
        Unitprice_SGD = 7.17, 
        Price_Incl_Tax = 7.67, 
        Discount = 0.00, 
        Total = 14.34, 
        GST = 15.34, 
        Total_incl_GST = 29.68
    )
    salad_model.objects.create(
        Transaction_date = "2019-2-12", 
        Supplier = "Eat Wide Awake FOOD", 
        Item_description = "[DRESSING] Mixed Berries Vinaigrette", 
        Country_of_origin = "Singapore", 
        Quantity = 2, 
        Unitprice_SGD = 7.17, 
        Price_Incl_Tax = 7.67, 
        Discount = 0.00, 
        Total = 14.34, 
        GST = 15.34, 
        Total_incl_GST = 29.68
    )
    a ={'fromdate' :'2020-2-10',
    'todate' : '2020-6-30'}

    fromdate = datetime.strptime(a['fromdate'], '%Y-%m-%d') 
    todate = datetime.strptime(a['todate'], '%Y-%m-%d')
    newdata = salad_model.objects.filter(Transaction_date__range =[fromdate,todate]) 
    response = client.post('/',data=a)
    assert response.status_code == 200
    assert len(response.context['results'])== len(newdata)

