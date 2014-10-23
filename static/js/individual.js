var G_or_id;
var GETOFFERTIME = 10;
var G_COUNT = -1;
$(document).ready(function(){
      
      $(".basic").jRating({
        canRateAgain : true,
        nbRates : 1000,
        length : 5,
        step:true,
        onClick : function(element,rate) {
          $("div[id = "+element.id+"]").attr('data',rate)
        }
      });

      $(".view_rating").jRating({
        length : 5,
        isDisabled : true
      });


      $("#command_confirm").click(function(){
        //alert($("#Comment1").attr('data')+G_or_id);
        $.ajax({
          url:'/t/i/comment/',
          type:'POST',
          data:{take:$("#Comment1").attr('data'),transport:$("#Comment2").attr('data'),server:$("#Comment3").attr('data'),goods:$("#Comment4").attr('data'),reputation:$("#Comment5").attr('data'),comment:$("#comment_msg").val(),or_id:G_or_id},
          //data:{'Name':'yuandong'},
          success:function(result){
            alert(result.status);
            location.reload(true)
          },
          error:function(){}
        });

        $("#comment_modal").modal("hide");
      });

      //查找是否有新的报价
      var path = window.location.pathname;
      if(path.endWith("psall/")||path.endWith("ps0/")){
        checkNewOffer();
      };
});


function comment(or_id){
  //alert(or_id);
  window.G_or_id = or_id;
  $("#comment_modal").modal("show");
  //$(".jRatingAverage").width(0);
  //$(".basic").attr('data-average','0');
      
}

function view_comment(or_id){
  window.G_or_id = or_id;
  $("#view_comment_modal").modal("show");

  $.ajax({
    url:'/t/i/view_comment/'+G_or_id,
    type:'GET',
    dataType:'json',
    success:function(result){
      if(result.status == 1){
        $('#view_comment_msg').text(result.or_comment);
          $('#view_Comment1 .jRatingAverage').width(23*(result.or_com_take));
          $('#view_Comment2 .jRatingAverage').width(23*(result.or_com_transport));
          $('#view_Comment3 .jRatingAverage').width(23*(result.or_com_server));
          $('#view_Comment4 .jRatingAverage').width(23*(result.or_com_goods));
          $('#view_Comment5 .jRatingAverage').width(23*(result.or_com_reputation));
      }
    },
    error:function(){

    }
  });
  
}

function checkNewOffer(){
  or_ids = [];
  $("input[name=OrderList]").each(function(){
    or_ids.push($(this).val());
  })
  $.ajax({
    url:'/t/i/new_offer/'+or_ids,
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



String.prototype.endWith=function(str){
  if(str==null||str==""||this.length==0||str.length>this.length)
    return false;
  if(this.substring(this.length-str.length)==str)
    return true;
  else
    return false;
  return true;
}