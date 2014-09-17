#coding:utf8
from django import forms
from transport.models import client,driver,order

class ClientForm(forms.ModelForm):

	clt_mail = forms.EmailField()
	clt_pwd = forms.CharField()
	clt_name = forms.CharField()
	clt_tel = forms.CharField()
	clt_company = forms.CharField()
	clt_position = forms.CharField()
	clt_industry = forms.CharField()
	clt_from = forms.CharField()

	class Meta:
		model = client
		fields = ['clt_name','clt_pwd','clt_mail','clt_tel','clt_company','clt_position','clt_industry','clt_from']

class DriverForm(forms.ModelForm):
	dr_name = forms.CharField(label='姓名：')
	dr_iden =  forms.CharField(label='身份证号码：')
	dr_tel = forms.CharField(label='手机号码：')
	dr_number = forms.CharField(label='车牌号码：')
	dr_hand = forms.CharField(label='挂车号码：')
	dr_type = forms.CharField(label='车辆类型：')
	dr_length = forms.CharField(label='车辆长度：')
	dr_weight = forms.CharField(label='最大载重：')
	dr_pwd = forms.CharField(label='设置密码：')

	class Meta:
		model = driver
		fields = ['dr_name','dr_iden','dr_tel','dr_number','dr_hand','dr_type','dr_length','dr_weight','dr_pwd']

class OrderForm(forms.ModelForm):

	class Meta:
		model = order