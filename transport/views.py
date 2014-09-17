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

def index(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/index.html',context_dict,context)

def download(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/download.html',context_dict,context)

def about(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/about.html',context_dict,context)


def f_pwd_1(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		pwd_code = request.session.get('pwd_code',False)
		get_code = request.POST.get('code','')
		mail = request.session.get('pwd_mail',False)
		if pwd_code == get_code :
			context_dict['mail'] = mail
			del request.session['pwd_code'] 
			del request.session['pwd_mail'] 
			return render_to_response('transport/pwd-forget2.html',context_dict,context)
		else:
			context_dict['error'] = '验证码输入错误'
			if mail:
				context_dict['mail'] = mail
			return render_to_response('transport/pwd-forget1.html',context_dict,context)

	return render_to_response('transport/pwd-forget1.html',context_dict,context)

def f_pwd_2(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == "POST":
		#print request.POST
		clt_mail = request.POST.get('clt_mail','')
		clt_pwd = request.POST.get('clt_pwd','')
		client_obj = client.objects.get(clt_mail__exact = clt_mail)
		client_obj.clt_pwd = clt_pwd
		client_obj.save()
		return render_to_response('transport/pwd-forget3.html',context_dict,context)

	return render_to_response('transport/pwd-forget2.html',context_dict,context)

def f_pwd_3(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('transport/pwd-forget3.html',context_dict,context)

def f_pwd_code(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'GET':
		mail = request.GET.get('mail','')
		#print mail
		if not ProcessMail(mail):
			context_dict['msg'] = 0
			return HttpResponse(json.dumps(context_dict),content_type="application/json")
		client_obj =client.objects.filter(clt_mail__exact = mail)
		if not client_obj:
			context_dict['msg'] = 1
			return HttpResponse(json.dumps(context_dict),content_type="application/json")
		else:
			code = RandCode()
			SendMailCode(code,mail)
			request.session['pwd_code'] = code
			request.session['pwd_mail'] = mail
			context_dict['msg'] = 2
			return HttpResponse(json.dumps(context_dict),content_type="application/json")

	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#个人中心
def ind_select(request,status):
	context = RequestContext(request)
	context_dict = {}
	
	offer_objs = []

	session = request.session.get('username',False)
	if not session:
		return render_to_response('transport/login.html',context_dict,context)

	_id =request.session.get('user_id',False)

	if status != 'all':
		order_objs = order.objects.filter(or_status__exact = status,or_client__exact = _id).order_by('-or_update')
	else:
		order_objs = order.objects.filter(or_client__exact = _id).order_by('-or_update')

	for order_obj in order_objs:
		offer_objs_nums = offer.objects.filter(of_order__exact = order_obj).count()
		offer_obj = {}
		offer_obj['or_id'] = order_obj.or_id
		offer_obj['offer_nums'] = offer_objs_nums
		offer_objs.append(offer_obj)
		
	context_dict['orders'] = order_objs
	context_dict['offers'] = offer_objs

	#print context_dict
	#download = request.session.get('download',False)
	if status == '1':
		context_dict['download'] = True
	return render_to_response('transport/individual.html',context_dict,context)

#个人资料修改
def info(request):
	context = RequestContext(request)
	context_dict = {}

	_id =request.session.get('user_id',False)
	client_obj = client.objects.get(id__exact = _id)

	if request.method == 'POST':
		#print request.POST

		clt_name = request.POST.get('clt_name','')
		clt_tel = request.POST.get('clt_tel','')
		clt_company = request.POST.get('clt_company','')
		clt_position = request.POST.get('clt_position','')
		clt_industry = request.POST.get('clt_industry','')
		#clt_from = request.POST.get('clt_from','')

		client_obj.clt_name = clt_name
		client_obj.clt_tel = clt_tel
		client_obj.clt_company = clt_company
		client_obj.clt_position = clt_position
		client_obj.clt_industry = clt_industry

		client_obj.save()

		context_dict['error'] = "信息修改成功"

	context_dict['client'] = client_obj


	return render_to_response('transport/individual-info.html',context_dict,context)

#修改密码
def pwd(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		o_pwd = request.POST.get('o_pwd','')
		new_pwd = request.POST.get('new_pwd','')

		_id =request.session.get('user_id',False)
		client_obj = client.objects.get(id__exact = _id)

		if o_pwd != client_obj.clt_pwd:
			context_dict['error'] = '原始密码输入错误'
			return render_to_response('transport/individual-pwd.html',context_dict,context)
		else:
			client_obj.clt_pwd = new_pwd
			client_obj.save()
			context_dict['error'] = '密码修改成功，下次登录生效'
			return render_to_response('transport/individual-pwd.html',context_dict,context)

	return render_to_response('transport/individual-pwd.html',context_dict,context)

def individual(request):
	context = RequestContext(request)
	context_dict = {}

	session = request.session.get('username',False)
	if not session:
		return render_to_response('transport/login.html',context_dict,context)
	order_objs = order.objects.all()
	
	context_dict['orders'] = order_objs
	return render_to_response('transport/individual.html',context_dict,context)


#订单列表
def orderlist(request):
	context = RequestContext(request)
	context_dict = {}	
	return HttpResponseRedirect('/t/i/psall')

#订单详情
def orderdetail(request,or_id):
	context = RequestContext(request)
	context_dict = {}
	#print or_id
	order_obj = order.objects.get(or_id__exact = or_id)

	location_objs = location.objects.filter(lo_order__exact = order_obj).order_by('lo_update')
	#print location_objs.exists()

	offer_obj = offer.objects.get(of_order__exact = order_obj,of_confirm__exact = 1)

	address_objs = location.objects.filter(lo_order__exact = order_obj).order_by('-lo_update')
	#print location_objs
	if address_objs:
		context_dict['address'] = address_objs[0]

	context_dict['order'] = order_obj
	if location_objs:
	 	context_dict['locations'] = location_objs
	context_dict['offer_obj'] = offer_obj
	#print context_dict
	return render_to_response('transport/individual-orderdetail.html',context_dict,context)

def orderedit(request,or_id):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'POST':
		#print request.POST
		order_obj = order.objects.get(or_id__exact = or_id)
		order_obj.or_update = datetime.now()
		order_obj.or_pushTime = datetime.now()
		order_obj.or_title = request.POST.get('or_title','')
		order_obj.or_start = request.POST.get('or_start','')
		order_obj.or_longitude = request.POST.get('or_longitude','')
		order_obj.or_latitude = request.POST.get('or_latitude','')
		order_obj.or_end = request.POST.get('or_end','')
		order_obj.or_push = request.POST.get('or_push','')
		order_obj.or_startTime = request.POST.get('or_startTime','')
		order_obj.or_endTime = request.POST.get('or_endTime','')
		order_obj.or_name = request.POST.get('or_name','')
		order_obj.or_price = request.POST.get('or_price','')
		order_obj.or_board = request.POST.get('or_board','')
		order_obj.or_number = request.POST.get('or_number','')
		order_obj.or_weight = request.POST.get('or_weight','')
		order_obj.or_size_l = request.POST.get('or_size_l','')
		order_obj.or_size_w = request.POST.get('or_size_w','')
		order_obj.or_size_h = request.POST.get('or_size_h','')
		order_obj.or_volume = request.POST.get('or_volume','')
		order_obj.or_length = request.POST.get('or_length','')
		order_obj.or_truck = request.POST.get('or_truck','')
		order_obj.or_isDanger = request.POST.get('or_isDanger','')
		order_obj.or_isHeap = request.POST.get('or_isHeap','')
		order_obj.or_isHand = request.POST.get('or_isHand','')
		order_obj.or_isAssist = request.POST.get('or_isAssist','')
		order_obj.or_isInsurance = request.POST.get('or_isInsurance','')
		order_obj.or_request = request.POST.get('or_request','')
		order_obj.save()
		return HttpResponseRedirect('/t/i/psall')
	else:
		order_obj = order.objects.get(or_id__exact = or_id)
		context_dict['order'] = order_obj
		truck_objs = truck.objects.all().order_by('tr_sort')
		context_dict['trucks'] = truck_objs;

	#print context_dict
	return render_to_response('transport/individual-orderedit.html',context_dict,context)

#关闭订单
def orderclose(request,or_id):
	#print or_id
	order_obj = order.objects.get(or_id__exact = or_id)
	order_obj.or_status = 3
	order_obj.save()
	return HttpResponseRedirect('/t/i/psall')

#订单发布
def	orderpublish(request):
	context = RequestContext(request)
	context_dict = {}

	truck_objs = truck.objects.all().order_by('tr_sort')
	context_dict['trucks'] = truck_objs;

	if request.method == 'POST':
		orderData = request.POST

		orderData.appendlist('or_status',0)
		orderData.appendlist('or_view',0)
		orderData.appendlist('or_update',datetime.now())
		orderData.appendlist('or_pushTime',datetime.now())
		_id = request.session.get('user_id',False)
		orderData.appendlist('or_client',_id)
		orderData.appendlist('or_id',getOrderId())
		#print getOrderId()
		#print datetime.now().strftime('%Y%m%d')[2:]
		#print getOrderId()

		orderForm = OrderForm(data=orderData)

		if orderForm.is_valid():
			orderForm.save()
			#print '订单发布成功'
			return HttpResponseRedirect('/t/i/psall/')
		else:
			print orderForm.errors

	return render_to_response('transport/individual-orderpublish.html',context_dict,context)

#计算下一个订单编号
def getOrderId():

	first = datetime.now().strftime('%Y%m%d')[2:]
	count = order.objects.filter(or_id__startswith = first).count()
	last = '%d'%(100000+count)	
	return first+last


#展示报价列表
def orderreceive(request,or_id,sort):
	context = RequestContext(request)
	context_dict = {}
	#print	or_id,sort
	order_obj = order.objects.get(or_id__exact = or_id)

	if sort == '1':
		offer_objs = offer.objects.filter(of_order__exact = order_obj).order_by('of_price')
	elif sort == '2':
		offer_objs = offer.objects.filter(of_order__exact = order_obj).order_by('of_distance')
	elif sort == '3':
		offer_objs = offer.objects.filter(of_order__exact = order_obj).order_by('of_update')
	else:
		offer_objs = offer.objects.filter(of_order__exact = order_obj)

	context_dict['offer_objs_nums'] = offer_objs.count()
	context_dict['offer_objs'] = offer_objs
	context_dict['or_id'] = or_id
	
	print context_dict
	return render_to_response('transport/individual-orderreceive.html',context_dict,context)

#确认报价
def offer_confirm(request,of_id):
	context = RequestContext(request)
	context_dict = {}
	#print of_id
	offer_obj = offer.objects.get(id__exact = of_id)
	offer_obj.of_order.or_status = 1
	offer_obj.of_order.save()
	offer_obj.of_confirm = 1
	offer_obj.save()
	#request.session['download'] = True
	return HttpResponseRedirect('/t/i/ps1/')
	

def question(request):
	context = ''
	return render(request,'transport/question.html',context)

@csrf_exempt
def login(request):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'POST':
		mail = request.POST.get('name')
		password = request.POST.get('pwd')
		if not mail or not password:
			context_dict['error'] = '用户名或者密码不能为空'
			return render_to_response('transport/login.html',context_dict,context)
		if ProcessMail(mail) == False:
			context_dict['error'] = '邮箱格式不正确'
			return render_to_response('transport/login.html',context_dict,context)

		client_obj = client.objects.filter(clt_mail__exact = mail,clt_pwd__exact = password)
		if client_obj:
			if client_obj[0].clt_conf_mail == 1:
				request.session['username'] = client_obj[0].clt_name
				request.session['user_id'] = client_obj[0].id
				#print '用户登录成功'
				return HttpResponseRedirect('/t/i/psall')
			else:
				#print '用户邮箱未验证'
				context_dict['error'] = '邮箱未验证'
				context_dict['mail'] = client_obj[0].clt_mail
				return render_to_response('transport/login.html',context_dict,context)
		else:
			#print '用户登录失败'
			context_dict['error'] = '用户名或者密码错误'
			return render_to_response('transport/login.html',context_dict,context)
	return render_to_response('transport/login.html',context_dict,context)

#再次发送验证邮箱
def send_mail(request):
	context = RequestContext(request)
	context_dict = {}
	mail = request.GET.get('mail')
	SendMailConfirm(mail)
	context_dict['error'] = '已发送确认邮件，请确认后再登录'
	return render_to_response('transport/login.html',context_dict,context)

@csrf_exempt 
def reg(request):
	context = RequestContext(request)
	context_dict = {}
	registered = False

	if request.method == 'POST':
		#print request.POST
		mail = request.POST.get('clt_mail')

		clientForm = ClientForm(data=request.POST)

		if clientForm.is_valid():
			#print '注册成功'
			registered = True
			clientForm.save()
			#调用发送邮件接口，进行邮箱确认
			SendMailConfirm(mail)
			context_dict['error'] = '已发送确认邮件，请确认后再登录'
			return render_to_response('transport/login.html',context_dict,context)
		else:
			print clientForm.errors
		
	context_dict['registered'] = registered
	return render_to_response('transport/reg.html',context_dict,context)

#注册校验
def reg_validator(request):
	context_dict = {}
	clt_mail =  request.GET.get('clt_mail','null');
	client_objs = client.objects.filter(clt_mail__exact = clt_mail)
	if client_objs:
		context_dict['msg'] = 'no';
	else:
		context_dict['msg'] = 'yes';
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#确认邮箱
def conf_mail(request):
	context = RequestContext(request)
	context_dict = {}
	#print request.GET
	
	mail = request.GET.get('mail','')
	client_obj = client.objects.get(clt_mail__exact = mail)
	if client_obj:
		client_obj.clt_conf_mail = 1
		client_obj.save();
		context_dict['error'] = '邮箱已确认，请登录'
	else:
		context_dict['error'] = '请先注册再登录'
	return render_to_response('transport/login.html',context_dict,context)

def logout(request):
	context = RequestContext(request)
	context_dict = {}

	session = request.session.get('username',False)
	if session:
		del request.session['username']
		del request.session['user_id']
		return render_to_response('transport/login.html',context_dict,context)
	else:
		return HttpResponse('请先登录')

#司机获取固定范围内订单信息，包括车辆的经度维度,货物名称，装车地点，卸车地点
def get_order(request):
	context_list = []

	longitude = request.GET.get('longitude','')
	latitude = request.GET.get('latitude','')
	#print longitude,latitude
	order_objs = order.objects.filter(or_status__exact = 0)[:100]
	#print order_objs
	for order_obj in order_objs:
		context = {}
		context['or_id'] = order_obj.or_id
		context['or_title'] = order_obj.or_title
		context['or_longitude'] = order_obj.or_longitude
		context['or_latitude'] = order_obj.or_latitude
		context['or_start'] = order_obj.or_start
		context['or_end'] = order_obj.or_end
		context_list.append(context)
	#print context_list
	#print '司机获取范围内车辆坐标'
	return HttpResponse(json.dumps(context_list),content_type="application/json")

#司机通过查询获取固定范围内订单信息
def	get_order_search(request):
	context_list = []

	longitude = request.GET.get('longitude','')
	latitude = request.GET.get('latitude','')
	or_start = request.GET.get('or_start','')
	or_end = request.GET.get('or_end','')
	#print longitude,latitude,or_start,or_end

	order_objs = order.objects.filter(Q(or_start__icontains=or_start)|Q(or_end__icontains=or_end))
	#print order_objs
	for order_obj in order_objs:
		context = {}
		context['or_id'] = order_obj.or_id
		context['or_title'] = order_obj.or_title
		context['or_longitude'] = order_obj.or_longitude
		context['or_latitude'] = order_obj.or_latitude
		context['or_start'] = order_obj.or_start
		context['or_end'] = order_obj.or_end
		context_list.append(context)
	#print context_list
	#print '司机查询范围内信息'
	return HttpResponse(json.dumps(context_list),content_type="application/json")

#司机获取与他报价的订单信息
def get_order_offer(request):
	context_list = []
	dr_tel = request.GET.get('dr_tel','')
	#driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
	offer_objs = offer.objects.filter(of_driver__dr_tel__exact = dr_tel)
	#print offer_objs
	for offer_obj in offer_objs:
		order_obj = order.objects.get(or_id__exact = offer_obj.of_order.or_id)
		context = {}
		context['or_id'] = order_obj.or_id
		context['or_title'] = order_obj.or_title
		context['or_start'] = order_obj.or_start
		context['or_end'] = order_obj.or_end
		context['or_status'] = order_obj.or_status
		context['of_confirm'] = offer_obj.of_confirm
		context_list.append(context)
	#print '司机获取报价过的订单'
	#print context_list
	return HttpResponse(json.dumps(context_list),content_type="application/json")


#获取订单详细信息
def get_order_detail(request):
	context = []
	if request.method == 'GET':
		or_id = request.GET.get('or_id','')
		order_obj = order.objects.filter(or_id__exact = or_id)
		context = json.loads(serializers.serialize("json", order_obj))[0]['fields']
		order_obj = order.objects.get(or_id__exact = or_id)
		order_obj.or_view = order_obj.or_view+1
		order_obj.save()
	#print context
	print '获取订单详细信息'
	return HttpResponse(json.dumps(context),content_type="application/json")

#货车司机注册
@csrf_exempt 
def driver_reg(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		#print request.POST
		driverForm = DriverForm(data=request.POST)

		if driverForm.is_valid():
			#print '司机注册成功'
			driverForm.save()
			context_dict['status']='1'
		else:
			print driverForm.errors
			context_dict['status']='0'

	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车司机注册 WEB端
@csrf_exempt 
def dreg(request):
	context = RequestContext(request)
	context_dict = {}

	registered = False

	if request.method == 'POST':

		#print request.POST
		driverForm = DriverForm(data=request.POST)


		if driverForm.is_valid():
			#print '司机注册成功'
			driverForm.save()
			registered = True
		else:
			print driverForm.errors

	else:
		driverForm = DriverForm()

	context_dict['driverForm'] = driverForm
	context_dict['registered'] = registered

	return	render_to_response('transport/driver_reg.html',context_dict,context)

#货车司机登录
@csrf_exempt
def driver_login(request):
	context = RequestContext(request)
	context_dict = {}

	if request.method == 'POST':
		telphone = request.POST.get('dr_tel')
		password = request.POST.get('dr_pwd')
		#print	telphone,password
		driver_obj = driver.objects.filter(dr_tel__exact = telphone,dr_pwd__exact = password)
		if driver_obj:
			#print	'司机登录成功'
			context_dict['status']='1'
			context_dict['data']=json.loads(serializers.serialize("json", driver_obj))[0]['fields']
		else:
			#print	'司机登录失败'
			context_dict['status']='0'
	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车司机修改密码
@csrf_exempt
def driver_pwd(request):
	context_dict = {}
	
	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel')
		dr_pwd = request.POST.get('dr_pwd')

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
		if driver_obj:
			driver_obj.dr_pwd = dr_pwd
			driver_obj.save()
			context_dict['status']='1'
			#print '司机密码修改成功'
		else:
			context_dict['status']='0'
			#print '司机密码修改失败'
	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车信息修改
@csrf_exempt
def driver_update(request):
	context_dict = {}

	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel')
		dr_number = request.POST.get('dr_number')
		dr_hand = request.POST.get('dr_hand')
		dr_type = request.POST.get('dr_type')
		dr_length = request.POST.get('dr_length')
		dr_weight = request.POST.get('dr_weight')

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)

		if driver_obj:
			driver_obj.dr_number = dr_number
			driver_obj.dr_hand = dr_hand
			driver_obj.dr_type = dr_type
			driver_obj.dr_length = dr_length
			driver_obj.dr_weight = dr_weight
			driver_obj.save()
			context_dict['status']='1'
			#print '车辆信息修改成功'
		else:
			context_dict['status']='0'
			#print '车辆信息修改失败'

	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#货车司机报价
@csrf_exempt
def driver_offer(request):
	context_dict = {}
	if request.method == 'POST':
		dr_tel = request.POST.get('dr_tel')
		or_id = request.POST.get('or_id')
		or_price = request.POST.get('or_price')
		latitude = request.POST.get('latitude','')
		longitude = request.POST.get('longitude','')
		#print dr_tel,or_id,or_price,latitude,longitude
		#distance = 0

		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
		order_obj = order.objects.get(or_id__exact = or_id)

		distance = GetDistance(float(latitude),float(longitude),float(order_obj.or_latitude),float(order_obj.or_longitude))
		#print	distance
		if order_obj.or_status == 0:
			if driver_obj and order_obj:
				offer_obj = offer.objects.filter(of_order__exact = order_obj, of_driver__exact = driver_obj)
				if offer_obj:
					offer_obj = offer.objects.get(of_order__exact = order_obj, of_driver__exact = driver_obj)
					offer_obj.of_price = or_price
					offer_obj.of_update = datetime.now()
					offer_obj.of_distance = str(distance)
					offer_obj.save()
					context_dict['status']='2'
					#print '报价修改成功'
				else:
					offer_obj_new = offer(of_order = order_obj, of_driver = driver_obj,of_price = or_price,of_distance = str(distance),of_update = datetime.now(),of_confirm = 0)
					offer_obj_new.save()
					context_dict['status']='1'
					#print '报价成功'
			else:
				context_dict['status']='0'
				#print '报价失败'
		else:
			context_dict['status']='3'

	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#获取订单的位置信息
def set_location(request):
	context_dict = {}

	if request.method == 'POST':
		or_id = request.POST.get('or_id','')
		dr_tel = request.POST.get('dr_tel','')
		latitude = request.POST.get('latitude','')
		longitude = request.POST.get('longitude','')
		address = request.POST.get('address','')

		#print or_id,dr_tel,longitude,latitude,address
		order_obj = order.objects.get(or_id__exact = or_id)
		driver_obj = driver.objects.get(dr_tel__exact = dr_tel)
		if order_obj and driver_obj:
			location_obj = location(lo_order = order_obj,lo_driver = driver_obj,lo_longitude=longitude,lo_latitude=latitude,lo_location=address,lo_update = datetime.now())
			location_obj.save()
			context_dict['status']='1'
			#print '插入位置信息成功'
		else:
			context_dict['status']='0'
			#print '插入位置信息失败'

	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#设置订单完成，订单进入完成状态
def set_order_finish(request):
	context_dict = {}

	if request.method == 'POST':
		or_id = request.POST.get('or_id','')
		#print or_id
		order_obj = order.objects.get(or_id__exact = or_id)

		if order_obj:
			if order_obj.or_status == 1:
				order_obj.or_status = 2
				order_obj.save()
				context_dict['status']='1'
				#print '设置订单完成成功'
			else:
				context_dict['status']='2'
				#print '设置订单完成失败,订单不是进行状态'

		else:
			context_dict['status']='0'
			#print '设置订单完成失败,订单不存在'

	#print context_dict
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
						push_new = push(pu_order = order_obj,pu_driver = driver_obj,pu_count = 1)
						push_new.save()
						context = {}
						context['or_title'] = order_obj.or_title
						context['or_id'] = order_obj.or_id
						context_dict.append(context)
					else:
						print '已经给该司机推送过数据'
				else:
					print '该订单距离太远，不推送'
			else:
				print '推送时间已过期'
	#print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#手机端获取卡车类型
def truck_type(request):
	response_data = []
	truck_objs = truck.objects.all().order_by('tr_sort')
	for truck_obj in truck_objs:
		context = {}
		context['type'] = truck_obj.tr_type
		response_data.append(context)
	print response_data
	return HttpResponse(json.dumps(response_data),content_type="application/json")

#APP端获取版本信息
def app_update(request):
	context_dict = {}
	version = request.GET.get('version','')
	if version == '1.3':
		context_dict['status']='0'
	else:
		context_dict['status']='1'
	print context_dict
	return HttpResponse(json.dumps(context_dict),content_type="application/json")

#订单柱状图
def order_column(request):
	response_data = []
	order_objs = order.objects.all()
	count_all = order_objs.count()
	order_objs_0 = order_objs.filter(or_status__exact = 0).count()
	order_objs_1 = order_objs.filter(or_status__exact = 1).count()
	order_objs_2 = order_objs.filter(or_status__exact = 2).count()
	order_objs_3 = order_objs.filter(or_status__exact = 3).count()
	#print count_all,order_objs_1,order_objs_2,order_objs_3
	response_data = [['交易总数',count_all],['显示中',order_objs_0],['进行中',order_objs_1],['已完成',order_objs_2],['已关闭',order_objs_3]]
	print response_data
	return HttpResponse(json.dumps(response_data),content_type="application/json")

#订单饼状图
def order_pie(request):
	response_data = []
	order_objs = order.objects.all()
	count_all = order_objs.count()
	order_objs_0 = order_objs.filter(or_status__exact = 0).count()
	order_objs_1 = order_objs.filter(or_status__exact = 1).count()
	order_objs_2 = order_objs.filter(or_status__exact = 2).count()
	order_objs_3 = order_objs.filter(or_status__exact = 3).count()
	#print count_all,order_objs_1,order_objs_2,order_objs_3
	response_data = [['显示中',order_objs_0],['进行中',order_objs_1],['已完成',order_objs_2],['已关闭',order_objs_3]]
	print response_data
	return HttpResponse(json.dumps(response_data),content_type="application/json")

#获取范围内车辆的数量
def around(request,latitude,longitude,distance):
	response_data = {}
	#print latitude,longitude,distance
	count = 0
	online_objs = online.objects.filter(on_update__range=(datetime.now()-timedelta(seconds=7200),datetime.now()))
	#print online_objs
	for online_obj in online_objs:
		dis = GetDistance(float(latitude),float(longitude),float(online_obj.on_latitude),float(online_obj.on_longitude))
		#print dis
		if dis < float(distance):
			count = count +1
	response_data['num'] = count
	#print response_data
	return HttpResponse(json.dumps(response_data),content_type="application/json")

def around_rec(request,or_id,distance):
	response_data = {}
	#print or_id,distance
	count =0
	order_obj = order.objects.get(or_id__exact = or_id)

	online_objs = online.objects.filter(on_update__range=(datetime.now()-timedelta(seconds=7200),datetime.now()))
	#print online_objs
	for online_obj in online_objs:
		dis = GetDistance(float(order_obj.or_latitude),float(order_obj.or_longitude),float(online_obj.on_latitude),float(online_obj.on_longitude))
		if dis < float(distance):
			count = count +1
	response_data['num'] = count

	order_obj.or_push = distance
	order_obj.save()
	#print response_data
	return HttpResponse(json.dumps(response_data),content_type="application/json")