from django.http.response import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json
import logging
from .models import Product, ManufacturerInfo, User
# Create your views here.

logger = logging.getLogger('TagPrinter.printer.view')


@login_required(login_url="/login.html")
def index(request):
    """
    主页
    :param request:
    :return:render
    """
    return render(request, 'index.html')


def getinfo(request):
    """
    获取产品信息
    :param request:
    :return:Json
    """
    search_name = request.GET.get('name')
    product = Product.objects.filter(name=search_name)
    product_serial = serializers.serialize("json", product)
    logger.info('printer.view.getinfo.search_name={},product_serial={}'.format(search_name, product_serial))
    return JsonResponse(product_serial, safe=False)


def search(request):
    """
    查询产品信息
    :param request:
    :return:Json
    """
    product_list = []
    search_name = request.GET.get('name')
    if search_name:
        product = Product.objects.filter(Q(name__contains=search_name))
        for i in product:
            product_list.append(i.name)
        product_dict = {i: val for i, val in enumerate(product_list)}
        logger.info('printer.view.search.search_name={},product_dict={}'.format(search_name, product_dict))
        return JsonResponse(json.dumps(product_dict), safe=False)


def login_view(request):
    """
    登录
    :param request:
    :return:render
    """
    err_msg = '用户名或密码错误,请重试!'
    context = {'err_msg': err_msg}
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=user, password=password)
        if auth is not None:
            if auth.is_active:
                login(request, auth)
                request.session['is_login'] = True
                username = User.objects.filter(username=user).select_related()
                for user in username:  # 把用户关联的生产商写入session
                    request.session['manufacturer'] = user.user_info.manufacturer
                    request.session['address'] = user.user_info.address
                    request.session['production_origin'] = user.user_info.production_origin
                    request.session['phone'] = user.user_info.phone

                return redirect('/index.html')
            else:
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html', context)


def logout_view(request):
    """
    退出
    :param request:
    :return:redirect
    """
    user = request.user
    logout(request)
    return redirect('/login.html')
