from django.shortcuts import render
from . import models
# Create your views here.
from django.shortcuts import render,redirect

def index(request):
    pass
    return render(request, 'index.html')
def L(request):
    pass
    return render(request, 'login.html')
def login(request):
    error_msg = ''
    error_msg2 = ''
    if request.method == "POST":
        if 'login' in request.POST:
            user = request.POST.get("username")
            password = request.POST.get("password")
            val = request.POST.get("val")
            val_r = request.POST.get("val_r")
            ret = models.User.objects.filter(name=user, password=password)
            print("登录成功")
            if ret and val == val_r and val != '':
                print("跳转")
                print(ret)
                return redirect('/index/')
            elif val != val_r:
                print("E:验证码错误")
                error_msg = '驗證碼錯誤'
                print(error_msg)
            elif user == '' or password == '' or val == '' or val_r == '':
                print("E:输入有空")
                error_msg = '輸入有空'
                print(error_msg)
            else:
                print("E:用户名或密码错误")
                error_msg = '用戶名或密碼錯誤'
                print(error_msg)
        if 'register' in request.POST:
            userE = request.POST.get('Euser')
            password1 = request.POST.get('Epassword1')
            password2 = request.POST.get('Epassword2')
            val_E = request.POST.get('val_E')
            val_r_E = request.POST.get('val_r_E')
            user_list = models.User.objects.filter(name=userE)
            print("注册成功")
            print(user_list)
            if user_list:
                error_msg2 = '用戶名已存在'
                print(error_msg2)
            elif val_E != val_r_E and val_r_E != '':
                error_msg2 = '驗證碼不正確'
                print(error_msg2)
            elif password1 == '' or password2 == '' or userE == '' or val_r_E == '':
                error_msg2 = '輸入有空'
                print(error_msg2)
            elif password1 != password2:
                error_msg2 = '兩次密碼不一致'
                print(error_msg2)
            else:
                user = models.User.objects.create(name=userE, password=password1)
                user.save()
                return redirect('/index/')
    return render(request, 'login.html', {'error_msg': error_msg, 'error_msg2': error_msg2})

def register(request):
    # error_msg = ''
    # if request.method == "POST":
    #
    return render(request,'login.html')

def Jump_R(request):
    print("quit")
    if request.method == "GET":
        return render(request, 'login.html')
    return render(request, 'index.html')


def logout(request):
    pass
    return redirect('/index/')

