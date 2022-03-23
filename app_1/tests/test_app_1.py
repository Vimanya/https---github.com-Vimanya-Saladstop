import pytest
from django import urls
from app_1.models import salad_model

@pytest.mark.parametrize('param', [
	('index'),
	('aggegation')
])

@pytest.mark.django_db
def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200

@pytest.mark.django_db
def test_get_trans_details(client):
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

    response = client.get("/")

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