from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from app_1.models import salad_model
import pandas as pd    
import json

# Create your views here.


@csrf_exempt
def index(request):
    global res_filter
    if request.method == 'POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        fromdate = datetime.strptime(fromdate, '%Y-%m-%d')
        todate = datetime.strptime(todate, '%Y-%m-%d')
        print(fromdate,todate)
        res_filter = salad_model.objects.filter(Transaction_date__range =[fromdate,todate])
        context ={'results':res_filter}
        return render(request,'index.html',context)
    else:
        res_filter = salad_model.objects.all()
        context ={'results':res_filter}
        return render(request,'index.html',context)

@csrf_exempt
def aggegation(request):
    if request.method == 'GET':
        df = pd.DataFrame(list(res_filter.values())).fillna(0)
        df['Tot_with_GST'] = df["Total"] + (df["GST"] * df["Total"] )
        total_price  = df['Tot_with_GST'].sum()
        avgCostWoGst = df.groupby(df['Item_description'].str.lower())['Unitprice_SGD'].mean().reset_index().sort_values(by=['Unitprice_SGD'], ascending = False)
        big_qt = df.groupby(df['Country_of_origin'].str.lower())['Quantity'].sum().reset_index().sort_values(by=['Quantity'], ascending = False).reset_index().iloc[:1]['Country_of_origin'].values[0]

        avgCostWoGstdf = avgCostWoGst.to_json(orient = "records")
        data = []
        data = json.loads(avgCostWoGstdf)

        context = {'data':data,'big_qt':big_qt,'total_price':total_price}
    return render(request,'summary_saladstop.html',context)

