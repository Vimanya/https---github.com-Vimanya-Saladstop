from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from app_1.models import salad_model

# Create your views here.


@csrf_exempt
def index(request):
    global res_filter

    res_filter = salad_model.objects.all()
    context ={'results':res_filter}
    return render(request,'index.html',context)

