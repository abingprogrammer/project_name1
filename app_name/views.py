from django.shortcuts import render
# Create your views here.

# coding:utf-8
from django.http import HttpResponse
# from .form import AddForm
import json
import qrcode
from django.utils.six import BytesIO


def home(request):
    List = ['a', 'b', 'c']
    Dict = {'age': '11', 'name': '小红'}
    return render(request, 'home.html', {
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    })


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def hello(request):
    return render(request,'test.html')

def index(request):
    return render(request, 'index.html')


# def index(request):
#     if request.method == 'post':#提交
#         form = AddForm(request.POST)
#
#         if form.is_valid():
#             a = form.cleaned_data['a']
#             b = form.cleaned_data['b']
#             return HttpResponse(str(int(a)+int(b)))
#
#     else:#正常访问
#         form = AddForm()
#         return render(request,'form.html',{'form':form})
# def division(x,y):
#     return x/y
#
#
# if __name__ == '__main__':
#     print(division(4,2))


def generate_qrcode(request, data):
    img = qrcode.make(data) #把数据制作成二维码图片

    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    return response
