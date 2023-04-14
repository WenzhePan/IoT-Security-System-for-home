var SmokeInput = 0
var FireInput = 0
function smoke(){
    if (SmokeInput == 1){
        document.getElementById("smoke_input").value = "警報";
    }
    else if (SmokeInput == 0){
        document.getElementById("smoke_input").value = "安全";
    }
setInterval("smoke()",5000);    
}
smoke();

function fire(){
    if (FireInput == 1){
        document.getElementById("fire_input").value = "警報";
    }
    else if (FireInput == 0){
        document.getElementById("fire_input").value = "安全";
    }
setInterval("fire()",5000);    
}
fire();
var echo 
function echo_Alarm(){

    if(document.getElementById("echo_input").value>=2&&document.getElementById("echo_input").value<=10){
        document.getElementById("ai_note").value="窗口有人闯进来了！"
    }
setInterval("echo_Alarm()",5000)
}
echo_Alarm()

function hello(){
    now = new Date() 
    hour = now.getHours()
    document.getElementById("ai_note").value=hour
    if(hour<9){
        document.getElementById("ai_note").value="早上好！"
    }
    else if(hour>=9 && hour<13){
        document.getElementById("ai_note").value="中午好！"
    }
    else if(hour>=13 && hour<17){
        document.getElementById("ai_note").value="下午好！"
    }
    else if(hour>=17 || hour<5){
        document.getElementById("ai_note").value="晚上好！"
    }

}
hello()

// function test(){
//     alert("test!!!")
// }