from django.contrib import admin
from . import models
# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'roleName',)
    search_fields = ['id', 'roleName']
admin.site.register(models.Role, RoleAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('number', 'userPassword', 'name',
                    'credit', 'score', 'donate', 'autoDonate', 'disable', 'wxOpenId', 'role')
    search_fields = ['userName', 'name', 'number']
    list_editable = ('credit', 'score', 'donate', 'autoDonate', 'disable')
admin.site.register(models.User, UserAdmin)


class RecycleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_filter = ('name',)
    search_fields = ['id',]
admin.site.register(models.RecycleCategory, RecycleCategoryAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'recType', 'location', 'capacity', 'count')
admin.site.register(models.Site, SiteAdmin)


class RecycleRecordAdmin(admin.ModelAdmin):
    list_display = ('userId', 'userName', 'site', 'siteLocation', 'siteRecTypeName', 'qty', 'time')
    search_fields = ['userId__number',]
    list_filter = ('site__location', 'site__recType__desc')

admin.site.register(models.RecycleRecord, RecycleRecordAdmin)


class DemoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'denoteUser', 'toatalNumber', 'denoteDes')

admin.site.register(models.Denote, DemoteAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'information', 'time')

admin.site.register(models.Feedback, FeedbackAdmin)

admin.site.site_header = '校园易回收后台管理'
admin.site.site_title = '校园易回收后台管理'
