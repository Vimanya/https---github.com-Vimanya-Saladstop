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
            fromdate = datetime.strptime(fromdate, '%Y-%m-%d') #change the String to date format
            todate = datetime.strptime(todate, '%Y-%m-%d')
            print(fromdate,todate)
            res_filter = salad_model.objects.filter(Transaction_date__range =[fromdate,todate]) #filter the data according to the dates input(range)
            context ={'results':res_filter} #return variables to html page
            return render(request,'index.html',context)
        except:
            messages.warning(request, 'Please Select From and to Dates') # Error message to dispaly not sected dates

    
    res_filter = salad_model.objects.all()
    context ={'results':res_filter}
    return render(request,'index.html',context)

@csrf_exempt
def aggegation(request):
    if request.method == 'GET':
        
        df = pd.DataFrame(list(res_filter.values())).fillna(0) #transform the queryset into pandas dataframe
        total_price  = df['Total_incl_GST'].sum()  #Sum the 'Total_incl_GST' column for Total

        avgCostWoGst = df.groupby(df['Item_description'].str.lower())['Unitprice_SGD'].mean().reset_index().sort_values(by=['Unitprice_SGD'], ascending = False) #Generate the average price per item table

        big_qt = df.groupby(df['Country_of_origin'].str.lower())['Quantity'].sum().reset_index().sort_values(by=['Quantity'], ascending = False).reset_index().iloc[:1]['Country_of_origin'].values[0] # Find Top supplier country

        avgCostWoGstdf = avgCostWoGst.to_json(orient = "records") # transform dataframe to json for display in html
        data = []
        data = json.loads(avgCostWoGstdf)

        context = {'data':data,'big_qt':big_qt,'total_price':total_price}
        return render(request,'summary_saladstop.html',context)

