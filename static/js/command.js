var G_or_id;

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


      $("#command_confirm").click(function(){
        alert($("#Comment1").attr('data')+G_or_id);
      });

});


function comment(or_id){
  //alert(or_id);
  window.G_or_id = or_id;
  $("#comment_modal").modal("show");
  $(".jRatingAverage").width(0);
  $(".basic").attr('data-average','0');
      
}