#coding:utf-8
from django.contrib import admin
from transport.models import client,driver,order,offer,location,truck,online

# Register your models here.

class OrderListFilter(admin.SimpleListFilter):
	title = '订单状态'
	parameter_name = 'or_status'

	def lookups(self, request, model_admin):
		return((0, '显示中'),(1, '进行中'),(2, '已完成'),(3, '已关闭'),)
	def queryset(self, request, queryset):
		if self.value():
			if int(self.value()) == 0:
				return queryset.filter(or_status=0)
			if int(self.value()) == 1:
				return queryset.filter(or_status=1)
			if int(self.value()) == 2:
				return queryset.filter(or_status=2)
			if int(self.value()) == 3:
				return queryset.filter(or_status=3)

class ClientAdmin(admin.ModelAdmin):
	fields = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from','clt_conf_mail']
	list_display = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from','clt_conf_mail']
	search_fields = ['clt_name']

class DriverAdmin(admin.ModelAdmin):
	fields = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']
	list_display = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']
	search_fields = ['dr_name']

class OrderAdmin(admin.ModelAdmin):
	def get_status(self,obj):
		if obj.or_status == 0:
			return '显示中'
		elif obj.or_status == 1:
			return '进行中'
		elif obj.or_status == 2:
			return '已完成'
		elif obj.or_status == 3:
			return '已关闭'
	def get_location(self,obj):
		if obj.or_status == 1:
			return "<a href='/admin/location_new/"+str(obj.or_id)+"''>物流信息</a>"
		elif obj.or_status == 2:
			return "<a href='/admin/location_new/"+str(obj.or_id)+"''>物流信息</a>"
		else:
			return "暂无记录"

	get_status.short_description = '订单状态'
	get_status.allow_tags = True
	get_location.short_description = '位置查看'
	get_location.allow_tags = True
    #get_status.allow_tags = True

	#fields = ['or_title','or_client','or_id','get_status','or_update','or_start','or_end','or_startTime','or_endTime','or_name','or_price','or_board','or_number','or_weight','or_size_l','or_size_w','or_size_h','or_volume','or_truck','or_length','or_isDanger','or_isHeap','or_isHand','or_isAssist','or_isInsurance','or_request','or_longitude','or_latitude','or_view']
	list_display = ['or_id','or_title','get_location','or_client','get_status','or_update','or_start','or_end','or_startTime','or_endTime','or_name','or_price','or_board','or_number','or_weight','or_size_l','or_size_w','or_size_h','or_volume','or_truck','or_length','or_isDanger','or_isHeap','or_isHand','or_isAssist','or_isInsurance','or_request','or_longitude','or_latitude','or_view']
	search_fields = ['or_id','or_title']
	list_filter = (OrderListFilter,)
	
class OfferAdmin(admin.ModelAdmin):
	fields = ['of_order','of_driver','of_price','of_distance','of_update','of_confirm']
	list_display = ['of_order','of_driver','of_price','of_distance','of_update','of_confirm']
	search_fields = ['of_order']

class LocationAdmin(admin.ModelAdmin):
	fields = ['lo_order','lo_driver','lo_longitude','lo_latitude','lo_location','lo_update']
	list_display = ['lo_order','lo_driver','lo_longitude','lo_latitude','lo_location','lo_update']

class TruckAdmin(admin.ModelAdmin):
	fields = ['tr_type','tr_sort']
	list_display = ['tr_type','tr_sort']

class OnlineAdmin(admin.ModelAdmin):
	fields = ['on_driver','on_longitude','on_latitude','on_update']
	list_display = ['on_driver','on_longitude','on_latitude','on_update']

admin.site.register(client,ClientAdmin)
admin.site.register(driver,DriverAdmin)
admin.site.register(order,OrderAdmin)
admin.site.register(truck,TruckAdmin)

#admin.site.register(online,OnlineAdmin)
#admin.site.register(offer,OfferAdmin)
#admin.site.register(location,LocationAdmin)