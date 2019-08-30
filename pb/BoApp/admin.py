from django.contrib import admin

# Register your models here.
from .models import BodyMlboRank,BodyMlboTotalboAnnual,BodyMlboDaybo,Calendarinfo
#视图无法引入admin,引入后会报错无法正常使用
#from .models import viewbodyfilm1stdayboOrm

class BodyMlboRankinfo(admin.TabularInline):
    model = BodyMlboRank
    extra = 2

class BodyMlboRankAdmin(admin.ModelAdmin):
    #class下面的内容得缩进，否则识别不了
    #列表页属性
    list_display =['filmname','releaseyear','boxoffice']
    #显示哪些字段
    list_filter=['releaseyear']
    #过滤器
    search_fields=['releaseyear']
    #搜索字段
    list_per_page=5
    #分页
    #添加、修改页的属性，fields与fieldsets不能同时使用，具有互斥性
    fields=['releaseyear','filmname','boxoffice']
    #属性的先后顺序
    #fieldsets=[]
    #给属性分组

class BodyMlboTotalboAnnualAdmin(admin.ModelAdmin):
    list_display = ['releaseyear','totalboxoffice']
    list_per_page = 10
    inlines = [BodyMlboRankinfo]
    #self.releaseyear.short_description = "年份"

class BodyMlboDayboAdmin(admin.ModelAdmin):
    list_display = ['yearmonthday','daytotalboxoffice','dayrank','filmname','releasedays','totalboxofficeoffilm','dayboxofficeoffilm']
    list_per_page = 10

class Calendarinfo(admin.ModelAdmin):
    list_display = ['solarcalendar','year','month','day','woc','weekday','specialday','festival','lunarcalendar','lunarcalendarmonth','lunarcalendarday','forrefer','remark']
    list_per_page=10

class Breakrecordstat(admin.ModelAdmin):
    list_display = ['filmname', 'releasedate', 'enddate', 'highestrank', 'milestonebo', 'milestonboedate',
                    'milestonebodatetime', 'surpassedfilm', 'firstroundfinalbo',  'remark']
    list_per_page = 10
#注册
admin.site.register(BodyMlboRank,BodyMlboRankAdmin)
admin.site.register(BodyMlboTotalboAnnual,BodyMlboTotalboAnnualAdmin)
admin.site.register(BodyMlboDaybo,BodyMlboDayboAdmin)
#admin.site.rigister(viewbodyfilm1stdayboOrm)
#@admin.register(viewbodyfilm1stdayboOrm)
#@admin.register(BodyMlboRank)
