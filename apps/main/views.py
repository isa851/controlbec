from django.shortcuts import render
from apps.main.models import SiteInfo
# Create your views here.

def index(request):
    siteInfo = SiteInfo.objects.last()
    return render(request,"index.html",locals())