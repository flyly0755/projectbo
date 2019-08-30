from .models import *
class viewbodyfilm1stdayboOrm(models.Model):
    yearmonthday = models.DateField(db_column='年月日',blank=True,null=True)
    filmname = models.CharField(db_column='片名', max_length=255, primary_key=True)
    releaseddays = models.IntegerField(db_column='上映天数', blank=True, null=True)
    firstdaybo = models.BigIntegerField(db_column='首日票房', blank=True, null=True)
    firstdayboyw = models.CharField(db_column='首日票房(亿万)', max_length=15, blank=True, null=True)
    def __str__(self):
        return "电影：%s 首日票房：%s" %(self.filmname,self.firstdaybo)

    class Meta:
        managed = False
        db_table = 'view_body_film1stdaybo'


class vdaytotalbociOrm(models.Model):
    yearmonthday = models.DateField(db_column='日期',blank=True,null=True,primary_key=True)
    totalambo = models.BigIntegerField(db_column='大盘',blank=True,null=True)
    top1movie= models.CharField(db_column='榜首影片', max_length=50)
    releaseddays = models.IntegerField(db_column='上映天数', blank=True, null=True)
    top1moviedaybo = models.BigIntegerField(db_column='影片日票房', blank=True, null=True)
    top1movietotalbo = models.BigIntegerField(db_column='影片总票房', blank=True, null=True)
    wov = models.CharField(db_column='班休',max_length=10,blank=True, null=True)
    weekday = models.CharField(db_column='星期',max_length=10, blank=True, null=True)
    festival = models.CharField(db_column='特殊节日1',max_length=30, blank=True, null=True)
    lunarcalendar = models.CharField(db_column='农历', max_length=20,blank=True, null=True)
    lunarcalendarmonth = models.CharField(db_column='农历月份',max_length=10, blank=True, null=True)
    lunarcalendarday = models.CharField(db_column='农历日',max_length=50, blank=True, null=True)
    def __str__(self):
        return "：%s 大盘：%s" %(self.yearmonthday,self.totalambo)

    class Meta:
        managed = False
        db_table = 'vdaytotalboci'
        ordering = ['-yearmonthday']


class Entdaybocp(models.Model):
    filmname = models.CharField(max_length=255)
    number_1strdymd = models.DateField(db_column='1strdymd', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    lrtbo = models.BigIntegerField(blank=True, null=True)
    number_30daystbo = models.BigIntegerField(db_column='30daystbo', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    finaltbo = models.FloatField(blank=True, null=True)
    wdmaxdaybo = models.IntegerField(blank=True, null=True)
    maxdayboymd = models.DateField()
    maxdaybo = models.BigIntegerField(blank=True, null=True)
    day1 = models.BigIntegerField(blank=True, null=True)
    day2 = models.BigIntegerField(blank=True, null=True)
    day3 = models.BigIntegerField(blank=True, null=True)
    day4 = models.BigIntegerField(blank=True, null=True)
    day5 = models.BigIntegerField(blank=True, null=True)
    day6 = models.BigIntegerField(blank=True, null=True)
    day7 = models.BigIntegerField(blank=True, null=True)
    day8 = models.BigIntegerField(blank=True, null=True)
    day9 = models.BigIntegerField(blank=True, null=True)
    day10 = models.BigIntegerField(blank=True, null=True)
    day11 = models.BigIntegerField(blank=True, null=True)
    day12 = models.BigIntegerField(blank=True, null=True)
    day13 = models.BigIntegerField(blank=True, null=True)
    day14 = models.BigIntegerField(blank=True, null=True)
    day15 = models.BigIntegerField(blank=True, null=True)
    day16 = models.BigIntegerField(blank=True, null=True)
    day17 = models.BigIntegerField(blank=True, null=True)
    day18 = models.BigIntegerField(blank=True, null=True)
    day19 = models.BigIntegerField(blank=True, null=True)
    day20 = models.BigIntegerField(blank=True, null=True)
    day21 = models.BigIntegerField(blank=True, null=True)
    day22 = models.BigIntegerField(blank=True, null=True)
    day23 = models.BigIntegerField(blank=True, null=True)
    day24 = models.BigIntegerField(blank=True, null=True)
    day25 = models.BigIntegerField(blank=True, null=True)
    day26 = models.BigIntegerField(blank=True, null=True)
    day27 = models.BigIntegerField(blank=True, null=True)
    day28 = models.BigIntegerField(blank=True, null=True)
    day29 = models.BigIntegerField(blank=True, null=True)
    day30 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entdaybocp'


class Entdayboyx(models.Model):
    filmname = models.CharField(max_length=255)
    filmentlink = models.CharField(max_length=255, blank=True, null=True)
    filmentlinkxp = models.CharField(max_length=255, blank=True, null=True)
    lrtbo = models.BigIntegerField(blank=True, null=True)
    thirtydaystbo = models.BigIntegerField(db_column='30daystbo', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    finaltbo = models.FloatField(blank=True, null=True)
    maxdaybo = models.BigIntegerField(blank=True, null=True)
    day1 = models.BigIntegerField(blank=True, null=True)
    day2 = models.BigIntegerField(blank=True, null=True)
    day3 = models.BigIntegerField(blank=True, null=True)
    day4 = models.BigIntegerField(blank=True, null=True)
    day5 = models.BigIntegerField(blank=True, null=True)
    day6 = models.BigIntegerField(blank=True, null=True)
    day7 = models.BigIntegerField(blank=True, null=True)
    day8 = models.BigIntegerField(blank=True, null=True)
    day9 = models.BigIntegerField(blank=True, null=True)
    day10 = models.BigIntegerField(blank=True, null=True)
    day11 = models.BigIntegerField(blank=True, null=True)
    day12 = models.BigIntegerField(blank=True, null=True)
    day13 = models.BigIntegerField(blank=True, null=True)
    day14 = models.BigIntegerField(blank=True, null=True)
    day15 = models.BigIntegerField(blank=True, null=True)
    day16 = models.BigIntegerField(blank=True, null=True)
    day17 = models.BigIntegerField(blank=True, null=True)
    day18 = models.BigIntegerField(blank=True, null=True)
    day19 = models.BigIntegerField(blank=True, null=True)
    day20 = models.BigIntegerField(blank=True, null=True)
    day21 = models.BigIntegerField(blank=True, null=True)
    day22 = models.BigIntegerField(blank=True, null=True)
    day23 = models.BigIntegerField(blank=True, null=True)
    day24 = models.BigIntegerField(blank=True, null=True)
    day25 = models.BigIntegerField(blank=True, null=True)
    day26 = models.BigIntegerField(blank=True, null=True)
    day27 = models.BigIntegerField(blank=True, null=True)
    day28 = models.BigIntegerField(blank=True, null=True)
    day29 = models.BigIntegerField(blank=True, null=True)
    day30 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entdayboyx'