import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

# 定义视图函数，业务逻辑
def fbv(request):
    # 返回一句话
    return HttpResponse(json.dumps('fbv!!!'))

class CbvView(View):

    def get(self,request,*args,**kwargs):
        return HttpResponse(json.dumps('cbv!!!'))







