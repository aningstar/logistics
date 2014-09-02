$(document).ready(function(){
	$.formValidator.initConfig({formID:"client_form",theme:"Default",submitOnce:true,
		onError:function(msg,obj,errorlist){
			$("#errorlist").empty();
			$.map(errorlist,function(msg){
				$("#errorlist").append("<li>" + msg + "</li>")
			});
			alert(msg);
		},
		ajaxPrompt : '有数据正在异步验证，请稍等...'
	});

	$("#clt_mail").formValidator({onFocus:"请务必填写有效的电邮地址",onCorrect:"&nbsp"})
				  .inputValidator({min:1,onError:"电邮地址不能为空"})
				  .regexValidator({regExp:"email",dataType:"enum",onError:"email格式不正确"})
				  .ajaxValidator({
				  	type:'get',
				  	dataType:'json',
				  	//async:true,
				  	url:'/t/reg_validator/',
				  	success:function(data){
				  		if(data.msg.indexOf('yes')>=0)
				  			return true;
				  		return false;
				  	},
				  	buttons:$("#submit"),
				  	error: function(jqXHR, textStatus, errorThrown){
				  		alert("服务器忙，请重试"+errorThrown);
				  	},
					onError: "该邮箱已被注册",
					onWait: "正在校验邮箱，请稍候..."
				  }).defaultPassed();
	$("#clt_pwd").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				 .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				 .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});
	$("#clt_pwd_a").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				   .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				   .compareValidator({desID:"clt_pwd",operateor:"=",onError:"2次密码不一致,请确认"})
				   .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});
	$("#clt_name").formValidator({onCorrect:"&nbsp"})
				  .inputValidator({min:1,onError:"称呼不能为空"});
	$("#clt_tel").formValidator({onFocus:"例如:010-88888888或手机号码",onCorrect:"&nbsp"})
				 .inputValidator({min:1,onError:"联系方式不能为空"})
				 .regexValidator({regExp:["tel","mobile"],dataType:"enum",onError:"手机或电话格式不正确"});
	$("#clt_company").formValidator({onCorrect:"&nbsp"})
					 .inputValidator({min:1,onError:"公司名称不能为空"});
	$("#confirm").inputValidator({min:1,onError:"公司名称不能为空"});		 
})