#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from transport.models import client,driver,order,offer,location,truck

def chart(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('admin/chart.html',context_dict,context)


def location_new(request,or_id):
	context = RequestContext(request)
	context_dict = {}
	print or_id
	order_obj = order.objects.get(or_id__exact = or_id)

	location_objs = location.objects.filter(lo_order__exact = order_obj).order_by('lo_update')

	offer_obj = offer.objects.get(of_order__exact = order_obj,of_confirm__exact = 1)

	address_objs = location.objects.filter(lo_order__exact = order_obj).order_by('-lo_update')
	if address_objs:
		context_dict['address'] = address_objs[0]

	context_dict['order'] = order_obj
	if location_objs:
	 	context_dict['locations'] = location_objs

	return render_to_response('admin/map_new.html',context_dict,context)

def location_his(request,or_id):
	context = RequestContext(request)
	context_dict = {}
	print or_id
	return render_to_response('admin/chart.html',context_dict,context)