var device="C4ABBDA29LQ7";
var keyword="f90d68049ada";
var quickDate="";
var queryType="";
//var token="";
// alert('start');
// window.onload=function(){
//     $.ajax({
//         async : false,
//         type:'get',
//         url:'https://storage.diandeng.tech/api/v1/ts?e=1596510236&device='+device+'&keyword='+keyword+'&quickDate=1h&queryType=avg',
//         dataType      : 'jsonp',
//         jsonp         : 'callback',
//         jsonpCallback : 'data',
//         success       : function(data){
//             if(data.success!='1'){
//                 alert("结果异常："+data.msgid+' '+data.msg);
//                 exit;
//             }
//             var desc="data.result";
//             alert(desc);
//         },
//         error:function(){
//             alert('请求失败');
//         }
//     });
// };
let hmac_sha1 = require("../crypto-js/hmac-sha1");
let enc_base64 = require("../crypto-js/enc-base64");
const axios = require('axios').default;

// 管理台获取accessKey、secretKey
let accessKey = 'DGXn5LZ782seRxHYEjh6vIgNK9uPfCpJrwF0ilBT'
let secretKey = '1Qt6g9RqFD47aZX83EjOwuVG5_nKUHWLJczxm0Bl'

// APP或管理台获取设备识别码
let deviceName = 'C4ABBDA29LQ7'

// 存储数据的key
let dataKey = 'f90d68049ada'

// token过期时间
let expirationTime = parseInt(new Date().getTime() / 1000) + (60 * 60);

let url = `https://storage.diandeng.tech/api/v1/ts?e=${expirationTime}&device=${deviceName}&keyword=${dataKey}&quickDate=1h&queryType=avg`
let sign = enc_base64.stringify(hmac_sha1(url, secretKey)).replace(/\+/g, '-').replace(/\//g, '_')
let token = accessKey + ":" + sign
console.log(token);

axios.get('https://storage.diandeng.tech/api/v1/ts', {
    params: {
        "e": expirationTime, // 过期时间，unix时间戳(秒）
        "device": deviceName, // 设备名
        "keyword": dataKey, // 存储key
        "quickDate": "1h", // 快速查询码：最近1小时
        "queryType": "avg", // 查询类型：平均
        "token": token // 计算出的token
    }
}).then(resp => {
    console.log(resp.data);
})

