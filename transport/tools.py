#coding:utf-8
import random,math,os
import string
from django.core.mail import send_mail

FullPath = 'http://localhost:8080/t/conf_mail'

#发送邮箱确认邮件
def SendMailConfirm(mail_address):
	mail_address = str(mail_address)
	print '已经向'+mail_address+'发送确认邮件'
	send_mail('至诚迅达邮箱确认','请点击以下连接进行确认\n'+FullPath+'?mail='+mail_address,'zhichengxunda@163.com',[mail_address],fail_silently=True)


#发送找回密码验证码
def SendMailCode(code,mail_address):
	code = str(code)
	mail_address = str(mail_address)
	print '已经向'+mail_address+'发送确认邮件'
	send_mail('至诚迅达密码修改','请在密码修改页面输入以下验证码:'+code,'zhichengxunda@163.com',[mail_address],fail_silently=True)

#随机产生六个字符
def RandCode():
	return string.join(random.sample(['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A','1','2','3','4','5','6','7','8','9','0'], 6)).replace(' ','')

#根据经度 纬度计算两点之间的距离
def rad(d):
	return d*3.1415927/180.0

def GetDistance(lat1,lng1,lat2,lng2):
    radlat1=rad(lat1)
    radlat2=rad(lat2)
    a=radlat1-radlat2
    b=rad(lng1)-rad(lng2)
    s=2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    earth_radius=6378.137
    s=s*earth_radius
    s = round(s,2)
    if s<0:
        return -s
    else:
        return s