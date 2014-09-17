// JavaScript Document
$(document).ready(function(){

  //确认关闭订单
  $("#close_order_confirm").click(function(){
    $.ajax({
        url:'/t/i/close/id'+$("#close_order_data").val(),
        method:'get',
        dateType:'json',
        success:function(data){
            $("#closeOrder").modal("hide");
            window.location.href="/t/i/psall"
        },
        error:function(date){
        }
    });
  });

  //详细页面选项卡切换
  $(".tabmenu li").click(function(){
    $(".tabmenu li").removeClass("hover");
    $(this).addClass("hover");
    $(".tabmenu").nextAll(".tabitem").hide();
    $(".tabmenu").parent("div").children("."+$(this).attr("data")).show();
    if($(this).attr("data") == 'posi'){
      loadMap();
    }
  });  

	var selects=$('select');//获取select
  for(var i=0;i<selects.length;i++){
    createSelect(selects[i],i);
  }
  function createSelect(select_container,index){
    //创建select容器，class为select_box，插入到select标签前
    var tag_select=$('<div></div>');//div相当于select标签
    tag_select.attr('class','select_box');
    tag_select.insertBefore(select_container);
    //显示框class为select_showbox,插入到创建的tag_select中
    var select_showbox=$('<div></div>');//显示框
    select_showbox.css('cursor','pointer').attr('class','select_showbox').appendTo(tag_select);
    //创建option容器，class为select_option，插入到创建的tag_select中
    var ul_option=$('<ul></ul>');//创建option列表
    ul_option.attr('class','select_option');
    ul_option.appendTo(tag_select);
    createOptions(index,ul_option);//创建option
    //点击显示框
    tag_select.toggle(function(){
      ul_option.show();
    },function(){
      ul_option.hide();
    });
    var li_option=ul_option.find('li');
    li_option.on('click',function(){
      $(this).addClass('selected').siblings().removeClass('selected');
      var value=$(this).text();
      select_showbox.text(value);
      ul_option.hide();
      //alert(value);
      //需要在这里改变原来select的值，否则django获取不到正确的数据
      var options=selects.eq(index).find('option')
      selected_option=options.filter(':selected')
      selected_option.removeAttr('selected');
      for(var n=0;n<options.length;n++){
        //options.eq(n).removeAttr('selected');
        if(value == options.eq(n).text()){
          options.eq(n).attr('selected','selected');
          //这里调用change方法，触发onchange函数
          options.eq(n).change();
        }
      }
    });
    li_option.hover(function(){
      $(this).addClass('hover').siblings().removeClass('hover');
    },function(){
      li_option.removeClass('hover');
    });
  }
  function createOptions(index,ul_list){
    //获取被选中的元素并将其值赋值到显示框中
    var options=selects.eq(index).find('option');
    //alert(selects.eq(index).attr("default"));
    selected_option=options.filter(':selected');
    selected_index=selected_option.index();
    showbox=ul_list.prev();
    if(typeof(selects.eq(index).attr("default"))=='undefined')
      showbox.text(selected_option.text());
    else{
      showbox.text(selects.eq(index).attr("default"));
    }
      
    //为每个option建立个li并赋值
    for(var n=0;n<options.length;n++){
      var tag_option=$('<li></li>'),//li相当于option
      txt_option=options.eq(n).text();
      //当select有默认值的时候选定select
      if(txt_option == showbox.text()){
        options.eq(n).attr('selected','selected');
      }

      tag_option.text(txt_option).css('cursor','pointer').appendTo(ul_list);
      //为被选中的元素添加class为selected
      if(n==selected_index){
        tag_option.attr('class','selected');
      }
    }

  }

	
	
	function resetloc(){
		//$(".banner > .wrap > .item:eq(1)").css("left","0px");
		$(".banner > .wrap > .item:eq("+ $(".banner .switch .hover").attr("data") +")").css("left","0px").show();
		$(".banner .temp").css("left","1000px");
	}
	function tooglebanner(o){
		var obj;
		if(o == null){
			//alert(($(".banner .switch .hover").attr("data") * 1 + 1) < ($(".banner .wrap .switch li").size()*1));
			var n = ($(".banner .switch .hover").attr("data") * 1) < ($(".banner .wrap .switch li").size()*1-1)?$(".banner .switch .hover").attr("data"):-1;
			obj = $(".banner .switch li:eq("+(n*1+1)+")");
		}
		else{obj = o;}
		$(".banner .switch li").removeClass("hover");
		obj.addClass("hover");
		obj.parent(".switch").parent(".wrap").children(".item").animate({left:"-1000px"},3000);
		$(".banner .temp").html(obj.parent(".switch").parent(".wrap").children(".item:eq("+obj.attr("data")+")").html()).animate({left:"0px"},3000,resetloc);
	}
	$(".banner .switch li").click(function(){
		tooglebanner($(this));
	});
	
	var changebanner = setInterval(tooglebanner,5000);
	$(".banner .wrap").mouseover(function(){
		clearInterval(changebanner);
	});
	$(".banner .wrap").mouseout(function(){
		changebanner = setInterval(tooglebanner,5000);
	});
	
	
	$(".extend").click(function(){
		if($(this).attr("class") == "extend"){
			$(this).addClass("pack");
			$(this).children("a").html("收起");
			$(this).parent("div").children("span").show();
		}
		else{
			$(this).removeClass("pack");
			$(this).children("a").html("更多");
			$(this).parent("div").children(".ep").hide();
		}
	});
	
})
// JavaScript Document



function showBg() { 
  var bh = $("body").height(); 
  var bw = $("body").width(); 
  $(".fullbg").css({ 
  height:bh, 
  width:bw, 
  display:"block" 
  }); 
  $(".dialog").show(); 
} 
  //关闭灰色 jQuery 遮罩 
function closeBg() { 
  $(".fullbg, .dialog").hide(); 
}

//详细页面地图加载函数
function loadMap(){
  
  lon = parseFloat($("#longitude").val());
  lat = parseFloat($("#latitude").val());
  loc = $("#location").val();
  updatedate = $("#updatedate").val();
  // 百度地图API功能
  var map = new BMap.Map("allmap");    // 创建Map实例
  
  var center = new BMap.Point(lon, lat);
  map.centerAndZoom(center, 15);  // 初始化地图,设置中心点坐标和地图级别
  
  var top_right_navigation = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_LEFT, type: BMAP_NAVIGATION_CONTROL_ZOOM}); //右上角，仅包含平移和缩放按钮
  map.addControl(top_right_navigation);

  var markerArr = [{icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}];
  var iconImg = createIcon(markerArr[0].icon);
  var marker = new BMap.Marker(center,{icon:iconImg}); // 创建点

  var opts = {
    enableMessage:false    //设置允许信息窗发送短息
  }
  var infoWindow = createInfoWindow(loc,updatedate,opts);  // 创建信息窗口对象 
  map.openInfoWindow(infoWindow,center); //开启信息窗口
  marker.addEventListener("click", function(){          
    map.openInfoWindow(infoWindow,center); //开启信息窗口
  });
  map.addOverlay(marker);            //增加点
}

//创建InfoWindow
function createInfoWindow(loc,updatedate,opts){
  var iw = new BMap.InfoWindow("<b class='iw_poi_title' title='" + loc + "'>" + loc + "</b><div class='iw_poi_content'>"+updatedate+"(上次定位)</div>",opts);
  return iw;
}

//创建地图图标
function createIcon(json){
  var icon = new BMap.Icon("http://app.baidu.com/map/images/us_mk_icon.png", 
                            new BMap.Size(json.w,json.h),
                            {
                              imageOffset: new BMap.Size(-json.l,-json.t),
                              infoWindowAnchor:new BMap.Size(json.lb+5,1),
                              anchor:new BMap.Size(json.x-2,json.h-22)}
                            )
  return icon;
}


//个人页面关闭页面
function closeOrder(or_id){
  $("#closeOrder").modal({
        show:true,
        backdrop:true
  });
  $("#close_order_data").val(or_id);
  //alert($("#close_order_data").val())
}

