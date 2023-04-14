var ky = "51959";	//注意：此处填入你官网申请下来的key
var sig = "941620aa572f4f30d301bc501679d20f";	//注意：此处填入你官网申请下来的sign
var mip = "ningbo";		//获取位置信息
window.onload=function(){
	$.ajax({
        type : 'get',
        async : false,
        url : 'http://api.k780.com/?app=weather.today&weaid='+mip+'&appkey='+ky+'&sign='+sig+'&format=json&jsoncallback=data',
        dataType      : 'jsonp',
        jsonp         : 'callback',
        jsonpCallback : 'data',
        success       : function(data){
            if(data.success!='1'){
            	//没有结果
                alert("结果异常："+data.msgid+' '+data.msg);
                exit;
            }
            //有结果则遍历
            var desc = "";
            for(var i in data.result){
                var property=data.result[i];	//遍历	
                desc += property + ",";	//拼接结果集为带逗号分隔字符串
            }
            //拆分字符串并转换为数组
            // alert(desc);
            
            var resArr = desc.split(',');
            var icon_src2=resArr[12].match(/weather(\S*)/)[1].replace(/.gif/,".png");
            var icon_src1="../static/assets/weather/icon";
            var icon_src= icon_src1+icon_src2;

            // alert(icon_src);
            //进行传值操作
            // document.getElementById('r1').innerHTML=resArr[1];	//日期
            // document.getElementById('r2').innerHTML=resArr[2];	//星期
            document.getElementById('weather_city').value=resArr[4];	//城市名称

            document.getElementById('weather_temp').value=resArr[7];	//当前温度
            // document.getElementById('r6').innerHTML=resArr[8];	//当前湿度
            // document.getElementById('r7').innerHTML=resArr[9];	//PM2.5
            // document.getElementById('r8').innerHTML=resArr[10];	//天气    	
            // document.getElementById('r9').innerHTML=resArr[14];	//风向
            // document.getElementById('r10').innerHTML=resArr[15];	//风力
 
            // document.getElementById('r11').innerHTML=resArr[11];	//当前天气
            document.images.weather_icon.src=icon_src;	//气象图标志url
            // alert(resArr);	//查看总结果集
            
        },
        error:function(){
            alert('请求失败');
        }
    });
};
