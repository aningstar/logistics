#coding:utf-8
from django.db import models
import simplejson as json
# Create your models here.

'''
客户表 发布方
'''
class client(models.Model):
	clt_mail = models.EmailField(verbose_name='Email',unique=True)
	clt_pwd = models.CharField(max_length=20,verbose_name='密码')
	clt_name = models.CharField(max_length=50,verbose_name='称呼')
	clt_tel = models.CharField(max_length=30,verbose_name='联系电话')
	clt_company = models.CharField(max_length=50,verbose_name='公司名称')
	clt_position = models.CharField(max_length=30,verbose_name='职位')
	clt_industry = models.CharField(max_length=30,verbose_name='行业')
	clt_from = models.CharField(max_length=30,verbose_name='获知本网站途径')
	clt_conf_mail =models.IntegerField(verbose_name='邮箱确认',default=0,null=True)

	def __unicode__(self):
		return self.clt_name

	class Meta:
		verbose_name = '发货企业'
		verbose_name_plural = '发货企业'


'''
司机 driver
'''
class driver(models.Model):
	dr_name = models.CharField(max_length=50,verbose_name='姓名')
	dr_iden =  models.CharField(max_length=50,verbose_name='身份证号码')
	dr_tel = models.CharField(max_length=30,verbose_name='手机号码',unique=True)
	dr_number = models.CharField(max_length=50,verbose_name='车牌号码')
	dr_hand = models.CharField(max_length=50,verbose_name='挂车号码')
	dr_type = models.CharField(max_length=50,verbose_name='车辆类型')
	dr_length = models.CharField(max_length=50,verbose_name='车辆长度')
	dr_weight = models.CharField(max_length=50,verbose_name='最大载重')
	dr_pwd = models.CharField(max_length=20,verbose_name='密码')

	def toJSON(self):
		return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

	def __unicode__(self):
		return self.dr_name

	class Meta:
		verbose_name = '货车司机'
		verbose_name_plural = '货车司机'

'''
订单
'''
class order(models.Model):
	or_client = models.ForeignKey(client,verbose_name='发货人')

	or_id = models.CharField(max_length=50,verbose_name='订单编号',unique=True)
	or_update = models.DateTimeField(verbose_name='更新时间')
	or_start = models.CharField(max_length=500,verbose_name='装车地点')
	or_end = models.CharField(max_length=500,verbose_name='卸车地点')
	or_push = models.IntegerField(default = 0,verbose_name='推送半径')
	or_pushTime = models.DateTimeField(verbose_name='推送距离更新时间')
	or_startTime = models.DateTimeField(verbose_name='提货时间')
	or_endTime = models.DateTimeField(verbose_name='计划到达时间')
	or_title = models.CharField(max_length=200,verbose_name='标题')
	or_name = models.CharField(max_length=200,verbose_name='货品名称')
	or_price = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总价值')
	or_board = models.IntegerField(verbose_name='货板数量',default=0)
	or_number = models.IntegerField(verbose_name='数量',default=0)
	or_weight = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总重')
	#or_size = models.CharField(max_length=200,verbose_name='尺寸')
	or_size_l = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='尺寸:长')
	or_size_w = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='尺寸:宽')
	or_size_h = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='尺寸:高')
	or_volume = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总体积')
	or_truck = models.CharField(max_length=50,verbose_name='货车类型')
	or_length = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='车辆长度')
	or_isDanger = models.CharField(max_length=50,verbose_name='是否包含危险品',default=0)
	or_isHeap = models.CharField(max_length=50,verbose_name='是否可堆放',default=0)
	or_isHand = models.CharField(max_length=50,verbose_name='是否底板载荷',default=0)
	or_isAssist = models.CharField(max_length=50,verbose_name='是否需要司机协助装卸工作',default=0)
	or_isInsurance = models.CharField(max_length=50,verbose_name='是否购买货物保险',default=0)
	or_request = models.CharField(max_length=500,verbose_name='其他说明',null=True)
	#0 显示中的订单 1 进行中的订单 2 已完成的订单 3 关闭的订单
	or_status = models.IntegerField(verbose_name='订单状态',default=0)
	or_longitude = models.DecimalField(max_digits=15,decimal_places=8,verbose_name='经度')
	or_latitude = models.DecimalField(max_digits=15,decimal_places=8,verbose_name='纬度')
	or_view = models.IntegerField(verbose_name='浏览次数',default=0)

	def __unicode__(self):
		return self.or_title

	class Meta:
		verbose_name = '订单管理'
		verbose_name_plural = '订单管理'

'''
订单报价
'''
class offer(models.Model):
	of_order = models.ForeignKey(order,verbose_name="订单")
	of_driver = models.ForeignKey(driver,verbose_name="司机")
	of_price = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='价格')
	of_distance = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='距离')
	of_update = models.DateTimeField(verbose_name='更新时间')
	of_confirm = models.IntegerField(verbose_name='是否确认',default=0)

	def __unicode__(self):
		return self.of_order.or_name

	class Meta:
		verbose_name = '订单报价'
		verbose_name_plural = '订单报价'

'''
订单位置信息
'''
class location(models.Model):
	lo_order = models.ForeignKey(order,verbose_name='订单')
	lo_driver = models.ForeignKey(driver,verbose_name="司机")
	lo_longitude = models.DecimalField(max_digits=15,decimal_places=8,verbose_name='经度')
	lo_latitude = models.DecimalField(max_digits=15,decimal_places=8,verbose_name='纬度')
	lo_location = models.CharField(max_length=500,verbose_name='地址')
	lo_update = models.DateTimeField(verbose_name='更新时间')

	def __unicode__(self):
		return self.lo_order.or_title

	class Meta:
		verbose_name = '位置信息'
		verbose_name_plural = '位置信息'

'''
司机在线时的位置信息，一个司机最多只有一条数据
'''
class online(models.Model):
	on_driver = models.ForeignKey(driver,verbose_name="司机")
	on_longitude = models.DecimalField(max_digits=15,decimal_places=8,verbose_name='经度')
	on_latitude = models.DecimalField(max_digits=15,decimal_places=8,verbose_name='纬度')
	on_update = models.DateTimeField(verbose_name='更新时间')

	def __unicode__(self):
		return self.on_driver.dr_name

	class Meta:
		verbose_name = '司机在线位置'
		verbose_name_plural = '司机在线位置'

'''
push记录表，一个订单给一个司机只push一次
'''
class push(models.Model):
	pu_order = models.ForeignKey(order,verbose_name='订单')
	pu_driver = models.ForeignKey(driver,verbose_name='司机')
	pu_count = models.IntegerField(default=0,verbose_name='推送次数')

	def __unicode__(self):
		return self.pu_order.or_title

	class Meta:
		verbose_name = '推送记录'
		verbose_name_plural = '推送记录'

'''
货车类型管理
'''
class truck(models.Model):
	tr_type = models.CharField(max_length=100,verbose_name='货车类型')
	tr_sort = models.IntegerField(default=0,verbose_name='排序')

	def __unicode__(self):
		return self.tr_type

	class Meta:
		verbose_name = '货车类型管理'
		verbose_name_plural = '货车类型管理'