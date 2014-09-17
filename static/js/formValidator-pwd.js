$(document).ready(function(){
	$.formValidator.initConfig({formID:"pwd",theme:"Default",submitOnce:true,
		onError:function(msg,obj,errorlist){
			$("#errorlist").empty();
			$.map(errorlist,function(msg){
				$("#errorlist").append("<li>" + msg + "</li>")
			});
			alert(msg);
		},
		ajaxPrompt : '有数据正在异步验证，请稍等...'
	});
	$("#o_pwd").formValidator({onCorrect:"&nbsp"})
			   .inputValidator({min:1,onError:"原始密码不能为空"});
	$("#new_pwd").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				 .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				 .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});
	$("#new_pwd_a").formValidator({onFocus:"6至15位数字或字母",onCorrect:"&nbsp"})
				   .inputValidator({min:6,max:15,empty:{leftEmpty:false,rightEmpty:false,emptyError:"密码两边不能有空符号"},onError:"密码长度不合法"})
				   .compareValidator({desID:"new_pwd",operateor:"=",onError:"2次密码不一致,请确认"})
				   .regexValidator({regExp:["num","letter"],dataType:"enum",onError:"只能包含数字或字母"});
})