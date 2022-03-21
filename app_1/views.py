from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from app_1.models import salad_model

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

