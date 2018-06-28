import os
from .img_recognition import recongnition

class Method(object):

  
    def image_save(request, userId):
        """
        将用户上传的照片保存到服务器，并返回照片保存的路径
        """
        import time
        p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        post_time = time.strftime('%Y-%m-%d_%H-%M-%S_')+'%s.jpg' % userId   # 照片命名 时间加学号
        if request.method == 'POST':
            img = request.FILES.get('file')
            path = os.path.join(p, 'images', post_time)
        with open(path, 'wb') as f:
            for line in img.chunks():
                f.write(line)
        return path

    
    def image_processing(path):
        """
        图像处理，得到返回的数据，成功返回字典结果, 失败返回False
        """
        a = recongnition(path)
        return a


    
    def data_processing(s):
        """
        处理图像分析后的数据，返回result字典
        """
        result = {'status':False, 'message':'', 'site': '', 'credit':''} # status:状态 message:向前端传递的消息 site垃圾箱编号 credit 加的分数
        menu = {'plastic':'塑料瓶', 'cans':'易拉罐', 'glass':'玻璃瓶', 'others':'others'}
        list1 = []
        for key, item in s[2].items():
            if item > 0:
                list1.append(menu.get(key))
        if menu.get(s[1]) in list1:
            if 'others' in list1:
                list1.remove('others')
            if len(list1) == 1:
                result['status'] = True
                result['message'] = '回收%s成功, 公益积分加%s分。' % (menu.get(s[1]), s[2].get(s[1]))
                result['site'] = s[0]
                result['credit'] = s[2].get(s[1])
                return result
            else:
                list1.remove(menu.get(s[1]))
                w = ' '.join(list1)
                result['message'] = '除了%s还有%s, 请分类回收' % (menu.get(s[1]), w)
                return result
        else:
            result['message'] = '请放入%s' % menu.get(s[1])
            return result
        



