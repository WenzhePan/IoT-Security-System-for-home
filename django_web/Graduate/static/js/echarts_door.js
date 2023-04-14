var array_date = new Array()
var D1,D2,D3
function re_date(){
    $.ajax({
    type:"post",
    url:"/date",
    async:false,
    success:function(result){
    array_date = result; 
    D1 = result[0];
    
    },
    complete: function(XHR, TS){
        XHR=null
    }
    });
}
$(document).ready(function(){
setInterval("re_date()",1000);
});
console.log(D1)

var chartDom = document.getElementById('echarts_id');
    var myChart = echarts.init(chartDom);
    var option;
    option = {
    xAxis: {
      type: 'category',
      boundaryGap: false
    },
    yAxis: {
      type: 'value',
      boundaryGap: [0, '30%']
    },
    visualMap: {
      type: 'piecewise',
      show: false,
      dimension: 0,
      seriesIndex: 0,
      pieces: [
        {
          gt: 1,
          lt: 3,
          color: 'rgba(0, 0, 180, 0.4)'
        },
        {
          gt: 5,
          lt: 7,
          color: 'rgba(0, 0, 180, 0.4)'
        }
      ]
    },
    series: [
      {
        type: 'line',
        smooth: 0.6,
        symbol: 'none',
        lineStyle: {
          color: '#5470C6',
          width: 5
        },
        markLine: {
          symbol: ['none', 'none'],
          label: { show: false },
          data: [{ xAxis: 0 }, { xAxis: 3 }, { xAxis: 5 }, { xAxis: 7 }]
        },
        areaStyle: {},
        data: [
          [result[0],0],
          [result[1],0],
          [result[2],0],        
        ]
      }
    ]
    };

    option && myChart.setOption(option);

