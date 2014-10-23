var refresh_time = 120;
var GETOFFERTIME = 10;
var G_COUNT = -1;
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


	//控制综合评分的显示
	$(".rateDIV").jRating({
        length : 5,
        isDisabled : true
    });

    //查找是否有新的报价
    checkNewOffer();
})


function checkNewOffer(){
  or_id = $("input[name=OrderList]").val();
  $.ajax({
    url:'/t/i/new_offer/'+or_id,
    type:'GET',
    dataType:'json',
    success:function(result){
      //alert(result.count);
      if(window.G_COUNT == -1){
        window.G_COUNT = result.count;
        console.log("页面第一次加载不刷新");
      }else if(window.G_COUNT != result.count){
        window.G_COUNT = result.count;
        console.log("有新报价，页面刷新");
        location.reload(true);
      }else{
        console.log("没有报价，不刷新")
      }
      setTimeout("checkNewOffer()", 1000*GETOFFERTIME);
    },
    error:function(){

    }
  });
  
  
}

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


String.prototype.endWith=function(str){
  if(str==null||str==""||this.length==0||str.length>this.length)
    return false;
  if(this.substring(this.length-str.length)==str)
    return true;
  else
    return false;
  return true;
}