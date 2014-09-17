$(document).ready(function(){
	loadMap();

});



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