from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from . import models

admin.site.register(models.Book)
admin.site.register(models.Publishing)
admin.site.register(models.Author)

class Bookadmin(admin.ModelAdmin):
    #用出版日期作为导航查询字段
    date_hierarchy = 'publishdate'

    #设置字段无值时显示的内容
    empty_value_display = '-无值-'

    #设置author字段的选择方式为水平扩展选择
    filter_horizontal = ('author',)

    #以下代码在页面上对字段进行分组显示或布局
    fieldsets = (
        (
            '图书信息',
            {'fields':(('title','publishdate'),'publishing','author')}
        ),
        (
            '图书简介',
            {'classes':('collapse',),'fields':('descript',)}
        ),
    )

    #自定义一个字段
    def descript_str(self,obj):
        #对字段进行切片，取前20个字符
        return obj.descript[:20]

    #设置自定义字段名称
    descript_str.short_description = '简介'

    #设置过滤导航字段
    list_filter = ('title','publishing','author')

    #设置查询字段
    search_fields = ('title', 'publishing__name', 'author__name')

    #列表显示字段
    list_display = ('title','descript_str','publishdate','publishing',)

    #显示查询到的记录数
    show_full_result_count = True
    #设定每页显示6条记录
    list_per_page = 6

    def change_publishing(self,request,queryset):
        publishing_obj = models.Publishing.objects.get(name = 'xxx出版社')
        rows = queryset.update(publishing=publishing_obj)
        self.message_user(request,'%s条记录被修改成"xxx出版社"'%rows)
    change_publishing.short_description='选中记录的出版社改为"xxx出版社"'
    #把方法名加到actions
    actions = ['change_publishing']

class PublishingAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    list_editable = ('address',)
    list_per_page = 10


class Authoradmin(admin.ModelAdmin):
    #自定义字段，使图片带有html格式并显示
    def header_data(self,obj):
        #mark_safe() 函数避免格式字符被转义 防止html代码被转义
        return mark_safe(u'<img src="/media/%s" width="50px" height="30px"/>'%obj.header)
    #定义字段名字
    header_data.short_description = '简介'
    list_display = ('name','email','birthday','header_data')
    list_per_page = 10



admin.site.unregister(models.Book)
admin.site.register(models.Book,Bookadmin)
admin.site.unregister(models.Publishing)
admin.site.register(models.Publishing,PublishingAdmin)
admin.site.unregister(models.Author)
admin.site.register(models.Author,Authoradmin)