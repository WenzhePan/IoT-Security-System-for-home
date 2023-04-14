function rad(){
    var result="";
    for(i=0;i<4;i++)
    {
        result=result+(parseInt(Math.random()*10)).toString();
    }
    document.getElementById("val_r").value=result;
}

function rad_E(){
    var result="";
    for(i=0;i<4;i++)
    {
        result=result+(parseInt(Math.random()*10)).toString();
    }
    document.getElementById("val_r_E").value=result;
}

function vall(){
var u = document.getElementById("user").value;
var p = document.getElementById("password").value;
if(isNone()) {
        if(localStorage.user) {
            // 从localStorage取出键为user的数据模型
            arr = eval(localStorage.user);
            let k = 0;
            // 循环取出
            for(e in arr) {
                // 判断用户名，密码是否和localStorage中的数据一致，兼容性写法必须添加trim(),不需要兼容可以不写
                if(u == arr[e].loginName) {
                    if(p == arr[e].loginPsd) {
                        localStorage.setItem("p_user",u);
                        k = 0;
                        alert('登录成功');
                        // 成功之后跳转到主页
                        window.location.href="../index";
                    } else {
                        alert('密码错误');
                        k = 0;
                        return;
                    }
                break;
                }else if(u != arr[e].loginName){
                    k=1;
                }
            }
            if(k == 1) {
                alert('用户名不存在');
            }
        }
    }
}

function enroll(){
    var u = document.getElementById("Euser").value;
    var p = document.getElementById("Epassword1").value;
    if(isNoneE()) {
        // 定义一个空数组
        let arr = [];
        if(localStorage.user) {
            arr = eval(localStorage.user);
            for(e in arr) {
                // 取出数据判断是否注册过
                if(u == arr[e].loginName) {
                    alert('该账号已被注册');
                    return;
                }
            }
        }
        const user = {
            'loginName': u,
            'loginPsd': p
        };
        // 添加数据
        arr.push(user);
        localStorage.user = JSON.stringify(arr);
        localStorage.setItem("p_user",u);
        alert('注册成功');
        window.location.href="../index";
    }
}
//function isNone() {
//    var u = document.getElementById("user").value;
//    var p = document.getElementById("password").value;
//    var val1 = parseInt(document.getElementById("val").value);
//    var val2 = parseInt(document.getElementById("val_r").value);
//    if(u == "") {
//        alert('用户名不能为空');
//        return false;
//    } else if(p == "") {
//        alert('密码不能为空');
//        return false;
//    } else if(val1 != val2){
//        alert('验证码错误');
//        return false;
//    }
//    return true;
//}

function isNoneE() {
    var u = document.getElementById("Euser").value;
    var p = document.getElementById("Epassword1").value;
    var p2 = document.getElementById("Epassword2").value;
    var val1 = parseInt(document.getElementById("val_E").value);
    var val2 = parseInt(document.getElementById("val_r_E").value);
    if(u == "") {
        alert('用户名不能为空');
        return false;
    } else if(p == "") {
        alert('密码不能为空');
        return false;
    } else if(p != p2) {
        alert('两次密码不一致，请检查！');
        return false;
    } else if(val1 != val2){
        alert('验证码错误');
        return false;
    }
    return true;
}
let animation3 =
    anime({
        targets: '.login',
        translateX: ['110%','0%'],
        autoplay: false,
        loop: false,
        easing: 'easeInOutQuad'
    })
let animation4 =
    anime({
        targets: '.enroll',
        translateX: ['-110%','0%'],
        autoplay: false,
        loop: false,
        easing: 'easeInOutQuad'
    })
let animation1 = 
    anime({
        targets: '.login',
        translateX: ['0%','110%'],
        autoplay: false,
        loop: false,
        easing: 'easeInOutQuad',
        
    })
let animation2 =
    anime({
        targets: '.enroll',
        translateX: ['0%','-110%'],
        autoplay: false,
        loop: false,
        easing: 'easeInOutQuad',
        
    })

let play1 = document.querySelector('#btn_enroll');
let play2 = document.querySelector('#btn_lg_E');
play1.onclick=()=>{
    animation1.play()
    animation2.play()
}
play2.onclick=()=>{
    animation3.play()
    animation4.play()
}


//js文件要放在底部加载
//把JS内容用window.οnlοad=function(){ }包裹起来
//W3School中介绍浏览器先加载完按钮节点才执行JS，当浏览器自顶向下解析时，找不到onclick绑定的按钮节点了
var btn_enroll_E=document.getElementById("btn_enroll_E");
//btn_enroll_E.onclick=enroll;
var btn_val_E=document.getElementById("btn_val_E");
btn_val_E.onclick=rad_E;
var user=document.getElementById("user");
user.placeholder="用 戶 名";
user.autocomplete="off";
var password=document.getElementById("password");
password.placeholder="密   碼";
password.autocomplete="off";
var val=document.getElementById("val");
val.placeholder="校 驗 碼";
val.autocomplete="off";
//var btn_lg=document.getElementById("btn_lg");
//btn_lg.onclick=vall;
var btn_val=document.getElementById("btn_val");
btn_val.onclick=rad;
var Euser=document.getElementById("Euser");
Euser.autocomplete="off";
Euser.placeholder="用 戶 名";
var Epassword1=document.getElementById("Epassword1");
Epassword1.placeholder="密   碼";
Epassword1.autocomplete="off";
var Epassword2=document.getElementById("Epassword2");
Epassword2.placeholder="重復密碼";
Epassword2.autocomplete="off";
var val_E=document.getElementById("val_E");
val_E.placeholder="校 驗 碼";
val_E.autocomplete="off";
