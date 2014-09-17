var order_column_chart = {
    chart: {
                type: 'column',
                renderTo : 'order_column'
            },
            title: {
                text: null
            },
            xAxis: {
                type: 'category'
                //labels: {
                 //   rotation: -55,
                //}
            },
            yAxis: {
                min: 0,
                title: {
                    text: null
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: '{point.y}比交易'
            },
            credits: {
                enabled: false
            },
            series: []
};

var order_pie_chart = {
    chart: {
                renderTo: 'order_pie',
                plotBackgroundColor: null,
                plotBorderWidth: 0,
                plotShadow: false,
                height: 300,
                backgroundColor: 'rgba(255, 255, 255, 0)'
            },
            title: {
                text: null
            },
            tooltip: {
                formatter: function() {
                    return this.point.name + ':<b>' + Math.round(this.point.percentage*Math.pow(10,1))/Math.pow(10,1) +'%</b>';
                }
            },
            legend:{
              layout: 'vertical',
              align: 'left',
              verticalAlign: 'middle',
              borderRadius: 5,
              borderWidth: 1,
              backgroundColor: '#FFFFFF',
              padding: 8,
              y: 5,
              useHTML: true,
              labelFormatter: function(){
                return '<div style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;width:140px;" title="' + this.name + '">' + this.name +'</div>';
              }
            },
            plotOptions: {
                pie: {
                    dataLabels: {
                        enabled: true,
                        distance: 20,
                        format: '{point.percentage:.1f} %'
                        //format: '{point.name}<br/>{point.percentage:.1f} %'
                    },
                    showInLegend: true
                }
            },
            credits: {
                enabled: false
            },
            series: []
};

$(document).ready(function(){
    $.ajax({
        url:'/t/order_column',
        method:'get',
        dateType:'json',
        success:function(data){
            //alert(data)
            var series = {};
            var dataLabels = {
                    enabled: true,                  
                    style: {
                        fontSize: '13px'
                    }
                };
            series.dataLabels = dataLabels;
            series.data = data;
            order_column_chart.series.push(series);
            new Highcharts.Chart(order_column_chart);
        },
        error:function(data){
            //alert('error');
        }
    });


    $.ajax({
        url:'/t/order_pie',
        method:'get',
        dateType:'json',
        success:function(data){
            //data = eval('('+data+')')
            //alert(data);
            var series = {};
            series.type = 'pie';
            series.data = data;
            order_pie_chart.series.push(series);
            new Highcharts.Chart(order_pie_chart);
        },
        error:function(date){
            //alert('error');
        }
    });
});