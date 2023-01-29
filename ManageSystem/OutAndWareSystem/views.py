from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from .models import Prices
from .models import Specifications
from .models import Warehouse
from .models import Issue
import json


# Create your views here.

def index(request):
    return render(request, 'OutAndWareSystem/index.html')


def get_price(request):
    all_goods = Prices.objects.all()
    return render(request, 'OutAndWareSystem/prices.html',
                  {
                      'goods': all_goods
                  })


def wx_price(request):
    all_goods = Prices.objects.all()
    return HttpResponse(all_goods)


def get_ware(request):
    all_goods = Warehouse.objects.all()
    return render(request, 'OutAndWareSystem/warehouse.html',
                  {
                      'goods': all_goods
                  })


def get_issue(request):
    all_order = Issue.objects.all()
    return render(request, 'OutAndWareSystem/issue.html',
                  {
                      'orders': all_order
                  })


def get_stocks(request):
    all_stock = Prices.objects.all()
    return render(request, 'OutAndWareSystem/stocks.html',
                  {
                      'goods': all_stock
                  })


def add_price(request):
    all_specifications = Specifications.objects.all()
    try:
        flange_model = request.POST.get('flange_model')
        flange_var = request.POST.get('flange_var')
        single_price = request.POST.get('single_price')
        stock_nums = request.POST.get('stock_nums')
        is_exist = Prices.objects.filter(flange_varieties=flange_var, flange_specifications=flange_model)
        if len(is_exist) == 0:
            flange = Prices(flange_specifications=flange_model, flange_varieties=flange_var,
                            flange_single_price=single_price, stocks_nums=stock_nums)
            flange.save()
            return render(request, 'OutAndWareSystem/jump.html')
        else:
            return render(request, 'OutAndWareSystem/add_prices.html',
                          {
                              'flanges': all_specifications,
                              'err_msg': '已添加过，请确认型号+规格'
                          })
    except Exception:
        return render(request, 'OutAndWareSystem/add_prices.html',
                      {
                          'flanges': all_specifications
                      })
        pass


def add_ware(request):
    try:
        data = json.loads(request.body)
        ware_date = data['ware_date']
        flange_model = data['flange_model']
        flange_var = data['varieties']
        single_price = data['single_price']
        goods_nums = data['nums']
        provider = data['provider']
        for i in range(len(flange_model)):
            spec = flange_model[i]
            vari = flange_var[i]
            flange = Warehouse(date=ware_date, flange_specifications=spec, flange_varieties=vari,
                               flange_single_price=single_price[i], order_nums=int(goods_nums[i]),
                               order_sum=int(goods_nums[i]) * float(single_price[i]),
                               provider=provider)
            flange.save()
            if len(Prices.objects.filter(flange_specifications=spec, flange_varieties=vari)) > 0:
                cur_nums = \
                    Warehouse.objects.filter(flange_specifications=spec, flange_varieties=vari).values_list(
                        'order_nums',
                        flat=True)[0]
                pri_nums = \
                    Prices.objects.filter(flange_specifications=spec, flange_varieties=vari).values_list('stocks_nums',
                                                                                                         flat=True)[0]
                Prices.objects.filter(flange_specifications=flange_model[i], flange_varieties=flange_var[i]).update(
                    stocks_nums=pri_nums + int(goods_nums[i]))
        return render(request, 'OutAndWareSystem/jump_ware.html')
    except Exception:
        all_specifications = Specifications.objects.all()
        cur_day = datetime.strftime(date.today(), '%y-%m-%d')
        return render(request, 'OutAndWareSystem/add_warehouse.html',
                      {
                          'flanges': all_specifications,
                          'cur_day': cur_day
                      })
        pass


def add_issue(request):
    try:
        data = json.loads(request.body)
        ware_date = data['out_date']
        flange_model = data['flange_model']
        flange_var = data['varieties']
        single_price = data['single_price']
        goods_nums = data['nums']
        customer = data['customer']
        for i in range(len(flange_model)):
            spec = flange_model[i]
            vari = flange_var[i]
            flange = Issue(date=ware_date, flange_specifications=flange_model[i], flange_varieties=flange_var[i],
                           flange_single_price=single_price[i], order_nums=int(goods_nums[i]),
                           order_sum=int(goods_nums[i]) * float(single_price[i]),
                           customer=customer)
            flange.save()
            if len(Prices.objects.filter(flange_specifications=spec, flange_varieties=vari)) > 0:
                print('>0>0')
                pri_nums = \
                    Prices.objects.filter(flange_specifications=spec, flange_varieties=vari).values_list('stocks_nums',
                                                                                                         flat=True)[0]
                print(pri_nums)
                print(goods_nums)
                Prices.objects.filter(flange_specifications=flange_model[i], flange_varieties=flange_var[i]).update(
                    stocks_nums=pri_nums - int(goods_nums[i]))
        return render(request, 'OutAndWareSystem/jump_issue.html')
    except Exception:
        all_specifications = Specifications.objects.all()
        cur_day = datetime.strftime(date.today(), '%y-%m-%d')
        return render(request, 'OutAndWareSystem/add_issue.html',
                      {
                          'flanges': all_specifications,
                          'cur_day': cur_day
                      })
        pass


def prices_search(request):
    all_goods = Prices.objects.all()
    q = request.GET.get('search_model')
    if not q:
        return render(request, 'OutAndWareSystem/prices.html',
                      {
                          'goods': all_goods,
                          'err_msg': '请输入搜素内容'
                      })
    else:
        goods = Prices.objects.filter(flange_varieties=q)
        return render(request, 'OutAndWareSystem/prices_search_result.html',
                      {
                          'vari': q,
                          'goods': goods
                      })


def ware_search(request):
    all_ware = Warehouse.objects.all()
    q = request.GET.get('search_model')
    if not q:
        return render(request, 'OutAndWareSystem/warehouse.html',
                      {
                          'goods': all_ware,
                          'err_msg': '请输入供货商'
                      })
    else:
        goods = Warehouse.objects.filter(provider=q)
        return render(request, 'OutAndWareSystem/ware_search_result.html',
                      {
                          'provider': q,
                          'goods': goods
                      })


def out_search(request):
    all_ware = Issue.objects.all()
    q = request.GET.get('search_model')
    if not q:
        return render(request, 'OutAndWareSystem/issue.html',
                      {
                          'goods': all_ware,
                          'err_msg': '请输入客户'
                      })
    else:
        goods = Issue.objects.filter(customer=q)
        return render(request, 'OutAndWareSystem/issue_search_result.html',
                      {
                          'customer': q,
                          'goods': goods
                      })


def delete_price(request, good_id):
    Prices.objects.all().get(flange_id=good_id).delete()
    return render(request, 'OutAndWareSystem/jump.html')


def delete_ware(request, ware_id):
    Warehouse.objects.all().get(order_id=ware_id).delete()
    return render(request, 'OutAndWareSystem/jump_ware.html')


def jump_update_price(request, good_id):
    good = Prices.objects.get(flange_id=good_id)
    return render(request, 'OutAndWareSystem/update_prices.html',
                  {
                      'good': good
                  })


def jump_update_ware(request, good_id):
    good = Warehouse.objects.get(order_id=good_id)
    return render(request, 'OutAndWareSystem/update_ware.html',
                  {
                      'good': good
                  })


def update_price(request):
    single_price = request.POST.get('single_price')
    flange_id = request.POST.get('flange_id')
    Prices.objects.filter(flange_id=flange_id).update(flange_single_price=single_price,
                                                      date=datetime.strftime(date.today(), '%y-%m-%d'))
    return render(request, 'OutAndWareSystem/jump.html')


def update_ware(request):
    single_price = request.POST.get('single_price')
    order_nums = request.POST.get('order_nums')
    flange_id = request.POST.get('flange_id')
    Warehouse.objects.filter(order_id=flange_id).update(flange_single_price=single_price, order_nums=order_nums,
                                                        order_sum=int(single_price) * int(order_nums))
    return render(request, 'OutAndWareSystem/jump_ware.html')


def calculate(request):
    formula = request.GET.get('formula')
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'

    return HttpResponse(result)
