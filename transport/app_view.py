#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q

from transport.forms import DriverForm,ClientForm,OrderForm
from transport.models import client,driver,order,offer,location,truck,online,push

import simplejson as json
from datetime import datetime,timedelta
from validator import *
from tools import *

#司机获取三个安全问题
def app_question(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'GET':
		dr_tel = request.GET.get('dr_tel','')
		#print dr_tel
		driver_objs = driver.objects.filter(dr_tel__exact = dr_tel)
		if driver_objs:
			context_dict['status'] = 1
			context_dict['dr_q1'] = driver_objs[0].dr_q1
			context_dict['dr_q2'] = driver_objs[0].dr_q2
			context_dict['dr_q3'] = driver_objs[0].dr_q3
		else:
			context_dict['status'] = 0

	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#验证司机安全问题是否正确
def app_conf_ans(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel','')
		dr_a1 = request.POST.get('dr_a1','')
		dr_a2 = request.POST.get('dr_a2','')
		dr_a3 = request.POST.get('dr_a3','')

		driver_objs = driver.objects.filter(dr_tel__exact = dr_tel)
		if driver_objs:
			if driver_objs[0].dr_a1 == dr_a1 and driver_objs[0].dr_a2 == dr_a2 and driver_objs[0].dr_a3 == dr_a3:
				context_dict['status'] = 1
			else:
				context_dict['status'] = 0
		else:
			context_dict['status'] = 0

	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#司机获取订单详细信息
def get_order_detail(request):
	context = []
	if request.method == 'GET':
		or_id = request.GET.get('or_id','')
		dr_tel = request.GET.get('dr_tel','')
		order_obj = order.objects.filter(or_id__exact = or_id)
		context = json.loads(serializers.serialize("json", order_obj))[0]['fields']
		order_obj = order.objects.get(or_id__exact = or_id)
		order_obj.or_view = order_obj.or_view+1
		order_obj.save()

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
		offer_objs = offer.objects.filter(of_order__exact = order_obj,of_driver__exact = driver_obj)
		#是否已经报价
		if offer_objs:
			context['has_offer'] = 1
		else:
			context['has_offer'] = 0

	#print context
	print '获取订单详细信息'
	return HttpResponse(json.dumps(context),content_type="application/json")

#用户确认后司机进行运送前的确认
def app_conf_order(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		or_id = request.POST.get('or_id','')

		order_objs = order.objects.filter(or_id__exact = or_id)
		if order_objs:
			if order_objs[0].or_status == 4:
				order_objs[0].or_status = 1
				order_objs[0].save()
				context_dict['status'] = 1
			else:
				context_dict['status'] = 2
		else:
			context_dict['status'] = 0

	return HttpResponse(json.dumps(context_dict),content_type="application/json")

