from django.db import models

# Create your models here.


class Role(models.Model):

    roleName = models.CharField(max_length=20, verbose_name='用户角色名称')

    class Meta:
        verbose_name='角色表'
        verbose_name_plural='角色表'

    def __str__(self):
        return self.roleName


class User(models.Model):

    uchoices = (('是','是'),('否','否'))
    number = models.CharField(max_length=10, verbose_name='学号')
    userPassword = models.CharField(max_length=20, verbose_name='密码', default='000000')
    name = models.CharField(max_length=30, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号码', blank=True, null=True)
    emailField = models.EmailField(verbose_name='邮箱',blank=True, null=True)
    credit = models.IntegerField(verbose_name='公益积分', default=0)
    score = models.IntegerField(verbose_name='团学积分', default=0)
    donate = models.IntegerField(verbose_name='捐赠积分', default=0)
    autoDonate = models.CharField(max_length=1, default='否', choices= uchoices, verbose_name='积分是否自动捐赠')
    disable = models.CharField(max_length=1, default='否', choices=uchoices, verbose_name='冻结用户资格')
    role = models.ForeignKey(Role, verbose_name='用户角色', on_delete=models.CASCADE)
    wxOpenId = models.CharField("微信OpenId", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.number


class RecycleCategory(models.Model):

    name = models.CharField(max_length=20, verbose_name='物品类别名称')
    desc = models.CharField(max_length=20, verbose_name='详细描述', blank=True, null=True)

    class Meta:
        verbose_name = '回收类别表'
        verbose_name_plural = '回收类别表'

    def __str__(self):
        return self.name



class Site(models.Model):

    name = models.CharField(max_length=20, verbose_name='回收点编号')
    recType = models.ForeignKey(RecycleCategory, verbose_name='回收类别', on_delete=models.CASCADE)
    location = models.CharField(max_length=20, verbose_name='所在位置', blank=True, null=True)
    capacity = models.IntegerField(verbose_name='垃圾桶容量', default=50)
    count = models.IntegerField(verbose_name='目前垃圾的数量', default=0)


    class Meta:
        verbose_name = '回收点表'
        verbose_name_plural = '回收点表'

    def __str__(self):
        return self.name


class RecycleRecord(models.Model):
    
    userId = models.ForeignKey(User, verbose_name='用户编号', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, verbose_name='所在回收点', on_delete=models.CASCADE)
    qty = models.IntegerField(verbose_name='数量')
    time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)

    def user_name(self):
        return self.userId.name
    
    user_name.short_description = '姓名'
    userName = property(user_name)

    def site_location(self):
        return self.site.location
    site_location.short_description = '地点'
    siteLocation = property(site_location)

    def site_recType_name(self):
        return self.site.recType.desc
    site_recType_name.short_description = '物品名'
    siteRecTypeName = property(site_recType_name)
    

    class Meta:
        verbose_name = '回收记录表'
        verbose_name_plural = '回收记录表'

    def __str__(self):
        return '成功'


class Denote(models.Model):
    
    denoteUser = models.CharField("用户", max_length=30)
    toatalNumber = models.IntegerField("总计捐赠分数", default=0)
    denoteDes = models.CharField('描述', max_length=50)

    class Meta:
        verbose_name = '总计捐赠分数'
        verbose_name_plural = '总计捐赠分数'

    def __str__(self):
        return self.denoteUser


class Feedback(models.Model):

    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    information = models.CharField("反馈信息", max_length=200)
    time = models.DateTimeField("提交时间", auto_now_add=True)
    
    class Meta:
        verbose_name = '反馈信息'
        verbose_name_plural = '反馈信息'
