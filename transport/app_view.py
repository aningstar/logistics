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

#司机查看评价详情
def app_view_comment(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'GET':
		or_id = request.GET.get('or_id','')

		order_obj = order.objects.get(or_id__exact = or_id)

		if order_obj.or_ifComment == 1:
			context_dict['status'] = 1
			context_dict['or_com_take'] = order_obj.or_com_take
			context_dict['or_com_transport'] = order_obj.or_com_transport
			context_dict['or_com_server'] = order_obj.or_com_server
			context_dict['or_com_goods'] = order_obj.or_com_goods
			context_dict['or_com_reputation'] = order_obj.or_com_reputation
			context_dict['or_comment'] = order_obj.or_comment
		else:
			context_dict['status'] = 0

	return HttpResponse(json.dumps(context_dict),content_type="application/json")		

#手机端获取推送数据
def app_push(request):
	context_dict = []

	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel','')
		latitude = request.POST.get('latitude','')
		longitude = request.POST.get('longitude','')
		#print dr_tel,latitude,longitude

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
		online_obj = online.objects.filter(on_driver__exact = driver_obj)

		#保存司机的位置信息
		if online_obj:
			online_obj[0].on_longitude = longitude
			online_obj[0].on_latitude = latitude
			online_obj[0].on_update = datetime.now()
			online_obj[0].save()
			#context_dict['status']='1'
		else:
			online_new = online(on_driver = driver_obj,on_longitude = longitude,on_latitude = latitude,on_update = datetime.now())
			online_new.save()
			#context_dict['status']='1'

		#向司机推送订单数据
		order_objs = order.objects.filter(or_status__exact = 0);

		for order_obj in order_objs:
			#最首先，推送的时间小于某个固定值
			or_pushTime = order_obj.or_pushTime
			or_pushTime = or_pushTime.replace(tzinfo=None)
			#print or_pushTime
			#print datetime.now()
			diffDays = (datetime.now() - or_pushTime).days
			diffSeconds = (datetime.now() - or_pushTime).seconds
			#print '时间差'+str(diffSeconds)
			if  diffSeconds < 7200 and diffDays == 0:
				#距离要小于推送距离
				distance = GetDistance(float(latitude),float(longitude),float(order_obj.or_latitude),float(order_obj.or_longitude))
				#print distance,order_obj.or_push
				if distance <= order_obj.or_push:
					push_obj = push.objects.filter(pu_order__exact = order_obj,pu_driver__exact = driver_obj)
					#其次，没有给该司机push过数据
					if not push_obj:
						#如果没有选挂车类型，需要满足长度要求
						u_noSelect = u'未选择'
						u_noLimit = u'没有特殊要求'
						if (order_obj.or_truck).encode('UTF-8') == u_noSelect.encode('UTF-8') or (order_obj.or_truck).encode('UTF-8') == u_noLimit.encode('UTF-8'):
							if float(order_obj.or_length) <= float(driver_obj.dr_length):
								push_new = push(pu_order = order_obj,pu_driver = driver_obj,pu_count = 1)
								push_new.save()
								context = {}
								context['or_title'] = order_obj.or_title
								context['or_id'] = order_obj.or_id
								context_dict.append(context)
						#如果选择了车辆类型，需要车辆类型必须符合，长度范围1米内
						else:
							if order_obj.or_truck == driver_obj.dr_type:
								if abs(float(order_obj.or_length) - float(driver_obj.dr_length)) <= 1:
									push_new = push(pu_order = order_obj,pu_driver = driver_obj,pu_count = 1)
									push_new.save()
									context = {}
									context['or_title'] = order_obj.or_title
									context['or_id'] = order_obj.or_id
									context_dict.append(context)
								else:
									print order_obj,'车辆长度不符合'
							else:
								print order_obj,'车辆类型不符合'
					else:
						print order_obj,'已经给该司机推送过数据'
				else:
					print order_obj,'该订单距离太远，不推送'
			else:
				print order_obj,'推送时间已过期'
	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

