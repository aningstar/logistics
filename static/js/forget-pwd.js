$(document).ready(function(){
	$.formValidator.initConfig({formID:"f_pwd",theme:"Default",submitOnce:true,
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
				  			return false;
				  		return true;
				  	},
				  	buttons:$("#submit"),
				  	error: function(jqXHR, textStatus, errorThrown){
				  		alert("服务器忙，请重试"+errorThrown);
				  	},
					onError: "登录邮箱不存在",
					onWait: "正在校验邮箱，请稍候..."
				  }).defaultPassed();
	$("#code").formValidator({onCorrect:"&nbsp"})
			  .inputValidator({min:1,onError:"验证码不能为空"});
	$("#clt_pwd").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				 .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				 .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});
	$("#clt_pwd_a").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				   .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				   .compareValidator({desID:"clt_pwd",operateor:"=",onError:"2次密码不一致,请确认"})
				   .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});

	$("#send").click(function(){
		$.ajax({
			url:'/t/f_pwd_code/?mail='+$("#clt_mail").val(),
			method:'get',
			dataType:'json',
			success:function(data){
            	if (data.msg == 0 || data.msg == 1){
            		alert('您邮箱输入不正确');
            	}else if (data.msg == 2){
            		//alert('邮件已发送,请查收');
            		$("#sendTip").text('邮件已发送,请查收');
            	}
			},
			error:function(data){

			}
		});
	});


	$.formValidator.initConfig({formID:"f_pwd_2",theme:"Default",submitOnce:true,
		onError:function(msg,obj,errorlist){
			$("#errorlist").empty();
			$.map(errorlist,function(msg){
				$("#errorlist").append("<li>" + msg + "</li>")
			});
			alert(msg);
		},
		ajaxPrompt : '有数据正在异步验证，请稍等...'
	});

	$("#clt_pwd").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				 .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				 .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});
	$("#clt_pwd_a").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				   .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				   .compareValidator({desID:"clt_pwd",operateor:"=",onError:"2次密码不一致,请确认"})
				   .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});

})