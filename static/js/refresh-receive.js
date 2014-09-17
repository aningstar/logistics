var refresh_time = 120;
$(document).ready(function(){
	var times = $.cookie('times');
	if(times == null){
		$.cookie('times',0);
	}
	
	var load_timeout = $.cookie('load_timeout');
	if(load_timeout != 0 && load_timeout != null){
		$('#span_refresh').attr('disabled', 'disabled');
		btn_disable();
	}

	$("#span_push").click(function(){
		$("#pushModal").modal({
				show:true,
				backdrop:true
		});
	});

	$("#push_confirm").click(function(){
		$("#pushModal").modal("hide");
	});
})

function changePush(or_id,distance){
	$.ajax({
        url:'/t/around_rec/id'+or_id+'dis'+$("#or_push").val(),
        method:'get',
        dateType:'json',
        success:function(data){
            //alert(data.num);
            $("#or_pushTip").removeClass('onError');
            $("#or_pushTip").addClass('onCorrect');
            $("#or_pushTip").text("");
			$("#or_pushTip").append('大约有'+data.num+'辆车')
        },
        error:function(date){
        }
    });
}

function refresh(id){
	if(typeof($("#span_refresh").attr("disabled"))=="undefined"){
			$.cookie('load_timeout',refresh_time);
			$('#span_refresh').attr('disabled', 'disabled');
			//$('#span_refresh').css("color","#666");
			window.location.href="/t/i/receive/id"+id+"s1";
			btn_disable();
		}else{
			return false;
		}
}

function btn_disable() {
	var load_timeout = $.cookie('load_timeout');
	if (load_timeout >= 0) {
		$('#span_refresh').text(load_timeout+'s');
		$.cookie('load_timeout' , load_timeout - 1);
		var timer = setTimeout("btn_disable()", 1000);
	}else{
		$('#span_refresh').attr('disabled', false);
		//$('#span_refresh').css("color","#017aff");
		$('#span_refresh').text('点击刷新');
	}
	
}