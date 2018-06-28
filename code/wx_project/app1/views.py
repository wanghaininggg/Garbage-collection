from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F
from . import models
from .function.processing import Method as m
import json


def index(request):

    """
    上传照片
    """

    if request.method == 'POST':
        result = {}
        userId = request.POST.get('userId')
        path = m.image_save(request, userId)   # 保存图片并获取照片路径
        data = m.image_processing(path) # 图像处理 得到处理后的返回值
        if data:
            print(data)
            result = m.data_processing(data) # 处理数据
            if result['status'] == True:
                siteId = result['site']
                number = result['credit']
                # 在用户表修改用户分数
                models.User.objects.filter(number=userId).update(credit=F('credit')+number, score=F('score')+str(int(number)*5))
                student = models.User.objects.get(number=userId)
                siteId = models.Site.objects.get(name=siteId)
                models.RecycleRecord.objects.create(userId=student, site=siteId, qty=number)   # 在回收记录表添加记录
            return HttpResponse(json.dumps(result))
        else:
            result['message'] = '图片不正确'
            return HttpResponse(json.dumps(result))
    return HttpResponse('index')


def bind(request):
    
    """
    绑定学号和微信
    """

    message={'message':'', 'status':False}
    if request.method == 'POST':
        wx_openid = request.POST.get('openid')
        userId = request.POST.get('yktid')
        userPassword = request.POST.get('passwd')
        user = models.User.objects.filter(number=userId)
        if user:
            if  user[0].wxOpenId == None:
                if user[0].userPassword == userPassword:
                    user.update(wxOpenId = wx_openid)
                    message['message'] = '绑定成功'
                    message['status'] = True
                else:
                    message['message'] = '密码错误'
            else:
                message['message'] = '该学号已被绑定'
        else:
            message['message'] = '学号错误'
        return HttpResponse(json.dumps(message))
    return HttpResponse('bind')
    

def login(request):

    """
    用户登录
    """

    APPID = 'wx8df921163e621d57'
    SECRET = 'd772720ab37805e2dbaaa7ab64f270bb'
    message = {'user_info':'', 'is_bind':True, 'wx_openid':''}
    if request.method == 'POST':
        JSCODE = request.POST.get('code')
        api = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code'%(APPID, SECRET, JSCODE)
        from urllib import request as rq
        with rq.urlopen(api) as f:
            data = f.read()
            s = json.loads(data.decode('utf8'))
            wx_openid = s.get('openid')    # 获取用户微信的openid
            message['wx_openid'] = wx_openid
            user = models.User.objects.filter(wxOpenId=wx_openid).values()
            if user:
                message['user_info'] = user[0]
            else:
                message['is_bind'] = False
        return HttpResponse(json.dumps(message))
    return HttpResponse('login')


def history(request):

    """
    用户查看个人捐赠历史
    """

    if request.method == 'POST':
        number = request.POST.get('userId', None)
        data = models.RecycleRecord.objects.filter(
            userId__number=number).order_by('-time').values('userId', 'site__name', 'site__location', 'site__recType__desc', 'qty', 'time')
        data = [x for x in data]
        import datetime
        class CJsonEncoder(json.JSONEncoder):    # 将日期格式变为字符串格式
            def default(self, obj):
                if isinstance(obj, datetime.datetime):
                    return obj.strftime('%Y-%m-%d %H:%M:%S')
                if isinstance(obj, datetime.date):
                    return obj.strftime("%Y-%m-%d")
                else:
                    return json.JSONEncoder.default(self, obj)
        return HttpResponse(json.dumps(data, cls=CJsonEncoder))
    return HttpResponse('history')


def rank(request):

    """
    用户积分排名
    """

    s = models.User.objects.filter(donate__gt=0).order_by(
        '-donate').values('number', 'name', 'donate')
    data = [x for x in s]
    return HttpResponse(json.dumps(data))


def denote(request):

    """
    捐献积分
    """
    
    message = {'status':False, 'message':''}
    if request.method == 'POST':
        userId = request.POST.get('user')
        num = request.POST.get('num').strip()
        user = models.User.objects.filter(number=userId)
        if num:
            if int(num) > 0 and int(num) <= user[0].credit:
                user.update(credit=F('credit')-num, donate=F('donate')+num)
                models.Denote.objects.filter(
                    denoteUser='everyone').update(toatalNumber=F('toatalNumber')+num)
                message['status'] = True
                message['message'] = '操作成功'
                return HttpResponse(json.dumps(message))
            else:
                message['message'] = '请输入正确的数额'
                return HttpResponse(json.dumps(message))
        else:
            message['message'] = '请输入捐赠数额'
            return HttpResponse(json.dumps(message))
    else:
        s = models.Denote.objects.get(denoteUser='everyone')
        return HttpResponse(s.toatalNumber)
    return HttpResponse('捐赠积分')


def feedback(request):

    if request.method == 'POST':
        userId = request.POST.get('user')
        information1 = request.POST.get('information')
        user1 = models.User.objects.filter(number=userId)[0]
        models.Feedback.objects.create(user=user1, information = information1)
        return HttpResponse('提交成功，谢谢您的参与')
    return HttpResponse('feedback')
