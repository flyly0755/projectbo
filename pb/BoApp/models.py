# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BodyMlboDaybo(models.Model):
    yearmonthday = models.DateField(db_column='YearMonthDay', blank=True, null=True)  # Field name made lowercase.
    daytotalboxoffice = models.BigIntegerField(db_column='DayTotalBoxOffice', blank=True, null=True)  # Field name made lowercase.
    urlofmaoyan = models.CharField(db_column='URLofMaoYan', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dayrank = models.SmallIntegerField(db_column='DayRank', blank=True, null=True)  # Field name made lowercase.
    filmname = models.CharField(db_column='FilmName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    releasedays = models.IntegerField(db_column='ReleaseDays', blank=True, null=True)  # Field name made lowercase.
    totalboxofficeoffilm = models.BigIntegerField(db_column='TotalBoxOfficeOfFilm', blank=True, null=True)  # Field name made lowercase.
    dayboxofficeoffilm = models.BigIntegerField(db_column='DayBoxOfficeOfFilm', blank=True, null=True)  # Field name made lowercase.
    ratioofboxoffice = models.FloatField(db_column='RatioOfBoxOffice', blank=True, null=True)  # Field name made lowercase.
    sessions = models.IntegerField(db_column='Sessions', blank=True, null=True)  # Field name made lowercase.
    ratioofsessions = models.FloatField(db_column='RatioOfSessions', blank=True, null=True)  # Field name made lowercase.
    persontimepersession = models.SmallIntegerField(db_column='PersonTimePerSession', blank=True, null=True)  # Field name made lowercase.
    occupancyrate = models.FloatField(db_column='OccupancyRate', blank=True, null=True)  # Field name made lowercase.
    reshow = models.IntegerField(db_column='ReShow', blank=True, null=True)  # Field name made lowercase.
    limitedreleasedays = models.IntegerField(db_column='LimitedReleaseDays', blank=True, null=True)  # Field name made lowercase.
    ymdtran = models.CharField(db_column='YMDtran', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=255, blank=True, null=True)  # Field name made lowercase.
    limitedrelease1stday = models.DateField(db_column='LimitedRelease1stDay', blank=True, null=True)  # Field name made lowercase.
    search_fields = ["yearmonthday", "reshow"]
    #date_hierarchy = "yearmonthday"
    class Meta:
        managed = False
        db_table = 'body-mlbo-daybo'
        ordering=['-yearmonthday']



class BodyMlboRank(models.Model):
    filmname = models.CharField(db_column='FilmName', primary_key=True, max_length=255)  # Field name made lowercase.
    releaseyear = models.ForeignKey('BodyMlboTotalboAnnual', models.DO_NOTHING, db_column='ReleaseYear')  # Field name made lowercase.
    boxoffice = models.BigIntegerField(db_column='BoxOffice', blank=True, null=True)  # Field name made lowercase.
    islogicdelete = models.TextField(db_column='isLogicDelete', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    #def __str__(self):
     #  return "电影：%s 总票房：%s" %(self.filmname,self.boxoffice)
    class Meta:
        managed = False
        db_table = 'body-mlbo-rank'
        ordering=['-releaseyear','-boxoffice']


class BodyMlboTotalboAnnual(models.Model):
    #自定义模型管理器，使用自定义模型管理器，则objects就不存在了
    #botOBJ=models.Manager()
    releaseyear = models.TextField(db_column='ReleaseYear', primary_key=True)  # Field name made lowercase. This field type is a guess.
    totalboxoffice = models.BigIntegerField(db_column='TotalBoxOffice', blank=True, null=True)  # Field name made lowercase.
    #这里一定要返回对象的属性，才能使BodyMlboRank使用的外键releaseyear正常显示，否则显示为xxx object，同时需要使用der__str__,而不能使用def__unicode__
    def __str__(self):
        return self.releaseyear
        #def __str__(self):
        ##%self.xxx一定要有%，表引用
       #return "%s年总票房：%s"%(self.releaseyear,self.totalboxoffice)
        ##return "%s" %self.releaseyear
    class Meta:
        managed = False
        db_table = 'body-mlbo-totalbo-annual'
        ordering=['-releaseyear']


class Calendarinfo(models.Model):
    solarcalendar = models.DateField(primary_key=True)
    year = models.SmallIntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    woc = models.CharField(max_length=10, blank=True, null=True)
    weekday = models.CharField(max_length=10, blank=True, null=True)
    specialday = models.CharField(max_length=30, blank=True, null=True)
    festival = models.CharField(max_length=30, blank=True, null=True)
    lunarcalendar = models.CharField(max_length=20, blank=True, null=True)
    lunarcalendarmonth = models.CharField(max_length=10, blank=True, null=True)
    lunarcalendarday = models.CharField(max_length=10, blank=True, null=True)
    forrefer = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendarinfo'
        ordering = ['solarcalendar']

class Breakrecordstat(models.Model):
    filmname = models.CharField(primary_key=True, max_length=255)
    releasedate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    highestrank = models.IntegerField(blank=True, null=True)
    milestonebo = models.BigIntegerField(blank=True, null=True)
    milestonboedate = models.DateField(blank=True, null=True)
    milestonebodatetime = models.DateTimeField(blank=True, null=True)
    surpassedfilm = models.CharField(max_length=255, blank=True, null=True)
    firstroundfinalbo = models.BigIntegerField(db_column='1stroundfinalbo', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breakrecordstat'
        ordering=['releasedate']

class Entdaybofull(models.Model):
    yearmonthday = models.DateField()
    weekday = models.CharField(max_length=5, blank=True, null=True)
    totalboxoffice = models.BigIntegerField(db_column='TotalBoxOffice', blank=True, null=True)  # Field name made lowercase.
    filmname = models.CharField(max_length=255)
    filmentlink = models.CharField(max_length=255, blank=True, null=True)
    filmentlinkxp = models.CharField(max_length=255, blank=True, null=True)
    filmnameent = models.CharField(max_length=255, blank=True, null=True)
    releasedays = models.FloatField(blank=True, null=True)
    releasedaysbak = models.FloatField(blank=True, null=True)
    rdremark = models.CharField(max_length=100, blank=True, null=True)
    rdflag = models.CharField(max_length=20, blank=True, null=True)
    remark2 = models.CharField(max_length=255, blank=True, null=True)
    ftbo = models.FloatField()
    daybo = models.BigIntegerField(blank=True, null=True)
    session = models.IntegerField(blank=True, null=True)
    ftbopd = models.FloatField(blank=True, null=True)
    irank = models.IntegerField(db_column='Irank')  # Field name made lowercase.
    releasedaysxp = models.IntegerField(blank=True, null=True)
    totalcounts = models.IntegerField(db_column='TotalCounts', blank=True, null=True)  # Field name made lowercase.
    totalshowcount = models.IntegerField(db_column='TotalShowCount', blank=True, null=True)  # Field name made lowercase.
    totalofferseat = models.BigIntegerField(db_column='TotalOfferSeat', blank=True, null=True)  # Field name made lowercase.
    totalaudicencecount = models.BigIntegerField(db_column='TotalAudicenceCount', blank=True, null=True)  # Field name made lowercase.
    audiencecount = models.IntegerField(db_column='AudienceCount', blank=True, null=True)  # Field name made lowercase.
    offerseat = models.IntegerField(db_column='OfferSeat', blank=True, null=True)  # Field name made lowercase.
    attandence = models.FloatField(db_column='Attandence', blank=True, null=True)  # Field name made lowercase.
    offerseatpercent = models.FloatField(db_column='OfferSeatPercent', blank=True, null=True)  # Field name made lowercase.
    totalserviceprice = models.CharField(db_column='TotalServicePrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weblink = models.CharField(max_length=255, blank=True, null=True)
    releasedate = models.DateField(blank=True, null=True)
    releasedatexp = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    basebo = models.CharField(max_length=255, blank=True, null=True)
    ftbobak = models.FloatField(blank=True, null=True)
    removeflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    minireleaseflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    nofilmflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    nofeaturefilmflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    filmnamewosc = models.CharField(max_length=255, blank=True, null=True)
    urlofmaoyan = models.CharField(max_length=255, blank=True, null=True)
    entdataflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    columnlist1 = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    avgprice = models.SmallIntegerField(blank=True, null=True)
    persontimepersession = models.SmallIntegerField(blank=True, null=True)
    scrapytime = models.DateTimeField(blank=True, null=True)
    filmnamexp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entdaybofull'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'





