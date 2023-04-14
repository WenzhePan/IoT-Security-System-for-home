function showtime(){
    var today,hour,second,minute,year,month,date;
    var strDate;
    var mArray = new Array("一","二","三","四","五","六","七","八","九","十","零");
    today = new Date();
    var n_day = today.getDay();

    switch(n_day){
        case 0:{
            strDate = "Sunday";
        }break;
        case 1:{
            strDate = "Monday";
        }break;
        case 2:{
            strDate = "Tuesday";
        }break;
        case 3:{
            strDate = "Wednesday";
        }break;
        case 4:{
            strDate = "Thursday";
        }break;
        case 5:{
            strDate = "Friday";
        }break;
        case 6:{
            strDate = "Saturday"
        }break;
        case 7:{
            strDate = "Sunday"
        }break;
    }

    year = today.getFullYear();
    month = today.getMonth()+1;
    date = today.getDate();
    hour = today.getHours();
    minute = today.getMinutes();
    second = today.getSeconds();
    
    if(month >=1 && month <= 9){
        month = "0" + month;
    }
    if(date >= 0 && date <= 9){
        date = "0"+ date;
    }
    if(hour >= 0&& hour <= 9){
        hour="0"+ hour;
    }
    if(minute >= 0 && minute <=9){
        minute = "0" +minute;
    }
    if(second>0 && second <=9){
        second = "0" +second;
    }
    
    document.getElementById("date_week").value=("   "+strDate);
    document.getElementById("date").value=("   "+year+"/"+month+"/"+date);
    document.getElementById("time").value=(hour+":"+minute+":"+second);
    setTimeout("showtime();",1000);
    
}
showtime();
