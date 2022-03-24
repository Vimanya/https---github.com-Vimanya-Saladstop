from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from app_1.models import salad_model
import pandas as pd    
import json
from django.contrib import messages
# Create your views here.

@csrf_exempt
def index(request):
    global res_filter
    if request.method == 'POST':
        try:
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            #change the String to date format
            fromdate = datetime.strptime(fromdate, '%Y-%m-%d') 
            todate = datetime.strptime(todate, '%Y-%m-%d')

            #filter the data according to the dates input(range)
            res_filter = salad_model.objects.filter(Transaction_date__range =[fromdate,todate]) 
            #return variables to html page
            context ={'results':res_filter} 
            return render(request,'index.html',context)
        except:
            # Error message to dispaly not selected dates
            messages.warning(request, 'Please Select From and to Dates') 

    
    res_filter = salad_model.objects.all()
    context ={'results':res_filter}
    return render(request,'index.html',context)

@csrf_exempt
def aggregation(request):
    if request.method == 'GET':
        #transform the queryset into pandas dataframe
        df = pd.DataFrame(list(res_filter.values())).fillna(0) 

        #Sum the 'Total_incl_GST' column for Total
        totalCost  = df['Total_incl_GST'].sum()  
        print(totalCost)

        # Find Top supplier country
        topSupplierCountry = df.groupby(df['Country_of_origin'].str.lower())['Quantity'].sum().reset_index().sort_values(by=['Quantity'], ascending = False).reset_index().iloc[:1]['Country_of_origin'].values[0] # Find Top supplier country

        #Generate the average price per item table
        avgCostWoGst = df.groupby(df['Item_description'].str.lower())['Unitprice_SGD'].mean().reset_index().sort_values(by=['Unitprice_SGD'], ascending = False) 
        # transform dataframe to json for display in html
        avgCostWoGstdf = avgCostWoGst.to_json(orient = "records") 
        data = []
        data = json.loads(avgCostWoGstdf)

        context = {'data':data,'big_qt':topSupplierCountry,'total_price':totalCost}
        return render(request,'summary_saladstop.html',context)

