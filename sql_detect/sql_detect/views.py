#import sys
#sys.path.insert(1,'/home/yanqisen/Documents/GraduateDesign/CNN-SQL')
from test import init, check,convert2label
import os
import json
from django.http import HttpResponse
from django.shortcuts import render
import urllib.parse
import keras

def index(request):
    context={}
    test=request.POST.get('test')
    test2=request.POST.get('test2')
    print(test)
    print(test2)
    if test:
        urlcodestr=urllib.parse.quote(str(test))
        keras.backend.clear_session()
        model,w_model=init()
        checked=check(model,w_model,urlcodestr)
        result=convert2label(checked)
        print(result)
        context['res']=result
    else:
        context={}
    return render(request, 'index.html', context)

