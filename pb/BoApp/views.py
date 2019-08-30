from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import json
from django.core import serializers
from django.db.models import Q



# Create your views here.定义视图
def index(request):
    #__init__() takes 1 positional argument but 2 were given ,如果写成return HttpResquest就会报这个错
    #return HttpRequest("Hello World! Sunny.")
    return  HttpResponse("Hello World! Sunny.")

def returnnum(request,num):
    return HttpResponse("num is: %s" %num)

def returnnums(request,num1,num2):
    return HttpResponse("nums is: %s and %s" %(num1,num2))

from .models import BodyMlboTotalboAnnual
def totalboannual(request):
    #去models里取数据
    totalboannualList=BodyMlboTotalboAnnual.objects.all()
    #将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request,'BoApp/mlbo_totalbo_annual.html',
                  {"BodyMlboTotalboAnnual":totalboannualList})




from .models import BodyMlboRank
def filmborank(request):
    filmborankList=BodyMlboRank.objects.all()
    year = 0
    return render(request,'BoApp/mlbo_rank.html',
                  {"MlboRank":filmborankList, 'GivenYear':year})

def filmborankAgivenyear(request,year):
    #不能用get，get返回一天数据，返回多条会有问题，要用filter
    #flimrecord=BodyMlboRank.objects.get(releaseyear=year)
    filmborankList = BodyMlboRank.objects.filter(releaseyear=year)
    #filmborankList=flimrecord.bodymlborank_set.all()
    #filmborankList = flimrecord.objects.all()
    return render(request,'BoApp/mlbo_rank.html',
                  {"MlboRank": filmborankList,'GivenYear':year})


def attributes(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attributes")

def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+" "+b+" "+c)

def get2(request):
    a=request.GET.getlist('a')
    a1=a[0]
    a2=a[1]
    c=request.GET.get('c')
    return HttpResponse(a1+' '+a2+' '+c)

def register(request):
    return render(request,'BoApp/register.html')

def registerresult(request):
    name=request.POST.get("xm")
    gender=request.POST.get("xb")
    age=request.POST.get("nl")
    lobby=request.POST.getlist("ah")
    print(name)
    print(gender)
    print(age)
    print(lobby)
    return HttpResponse("Register Result is:"+ name+" "+gender+" "+age+" "+lobby[0])

from django.shortcuts import redirect
def main(request):
    username2=request.session.get('name',"游客")
    return render(request,'BoApp/main.html',{'username':username2})

def login(request):
    return render(request,'BoApp/login.html')

def afterlogin(request):
    username1 = request.POST.get('account')
    request.session['name']=username1
    #可以设置session过期时间，比如下面设置10s后过期，还可以设置
    #截至具体时间过期，还可以设置为0，浏览器关闭时过期
    #request.session.set_expiry(10)
    request.session.set_expiry(0)
    return redirect('/boapp/main')

from django.contrib.auth import logout
def logoff(request):
    logout(request)
    #另一种方法
    #request.session.clear()
    #request.session.flush()
    return redirect('/boapp/main')

def mlborankpagnation(request):
    filmborankList = BodyMlboRank.objects.all()
    year = 0
    return render(request,'BoApp/mlbo_rank_pagnation.html',{"MlboRank":filmborankList, 'GivenYear':year})


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def mlborankpagnation2(request,year):
    if year:
        filmborankList = BodyMlboRank.objects.filter(releaseyear=year)
    else:
        filmborankList = BodyMlboRank.objects.all()

    paginator = Paginator(filmborankList, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        givenpage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        givenpage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        givenpage = paginator.page(paginator.num_pages)

    return render(request, 'BoApp/mlbo_rank_pagnation2.html', {'givenpage': givenpage, 'GivenYear':year})

from .mysql_view_models import viewbodyfilm1stdayboOrm,vdaytotalbociOrm
def film1stdaybo(request):
    film1stdayboList = viewbodyfilm1stdayboOrm.objects.all()
    listperpage =20
    paginator = Paginator(film1stdayboList, listperpage)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        givenpage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        givenpage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        givenpage = paginator.page(paginator.num_pages)
    basenum = (givenpage.number - 1) * listperpage
    return render(request,'BoApp/mlbo_1stdaybo.html',{'givenpage':givenpage,'basenum':basenum})


def daytotalbo(request):
    vdaytotalbolist = vdaytotalbociOrm.objects.all().order_by("yearmonthday")
    listperpage = 20
    paginator = Paginator(vdaytotalbolist, listperpage)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        givenpage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        givenpage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        givenpage = paginator.page(paginator.num_pages)
    basenum = (givenpage.number - 1) * listperpage
    #assert False
    return render(request, 'BoApp/mlbo_daytotalbo.html', {'givenpage': givenpage, 'basenum': basenum})



def daytotalbofestival(request,festival):
    #vdaytotalbolist = vdaytotalbociOrm.objects.filter(festival__contains=festival).order_by('id')
    #vdaytotalbolist = vdaytotalbociOrm.objects.filter(festival__contains=festival).order_by('totalambo')
    vdaytotalbolist = vdaytotalbociOrm.objects.filter(festival__contains = festival).order_by('yearmonthday')
    listperpage = 20
    paginator = Paginator(vdaytotalbolist, listperpage)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        givenpage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        givenpage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        givenpage = paginator.page(paginator.num_pages)
    basenum = (givenpage.number - 1) * listperpage
    #assert False
    return render(request, 'BoApp/mlbo_daytotalbo.html', {'givenpage': givenpage, 'basenum': basenum})

#闭包测试
def addx():
    x=[0]
    def addy(y):
        if y:
            x[0] = x[0]+int(y)
        return  x[0]
    return addy

addsum = 0
def sumtest(request):
    add2 = request.POST.get("yvalue")
    print(add2)
    #使用闭包无法多次累加，需使用全局变量
    # addsum = addx()
    # addresult=addsum(add2)
    # addresult1=addsum(20)
    global addsum
    if add2:
        addresult =int(add2)+addsum
    else: addresult = addsum
    addsum= addresult
    return render(request,'BoApp/xaddy.html',{'sum': addresult,'add2':add2})

from .models import Calendarinfo
def calendarinfo(request):
    calendarinfolist = Calendarinfo.objects.all()
    listperpage = 20
    paginator = Paginator(calendarinfolist, listperpage)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        givenpage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        givenpage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        givenpage = paginator.page(paginator.num_pages)
    basenum = (givenpage.number - 1) * listperpage
    # assert False
    return render(request, 'BoApp/calendarinfo.html', {'givenpage': givenpage, 'basenum': basenum})

from .models import Breakrecordstat
def breakrecordstat(request):
    breakrecordstatlist1=Breakrecordstat.objects.all()
    #breakrecordstatlist2=json.dumps(breakrecordstatlist1)
    breakrecordstatlist2 = serializers.serialize("json", breakrecordstatlist1)
    #print("brlist1 is:" %breakrecordstatlist1)
    #output_path = "E:/Python3.6/projects/projectbo/templates/BoApp/breakrecordstat-m.html"
    #bar_chart("localhost", 3306, "root", "123456", "body", "utf8", output_path)
    return render(request, 'BoApp/breakrecordstat.html', {"brlist1": breakrecordstatlist1,"brlist2":breakrecordstatlist2})

from .models import Entdaybofull
from .mysql_view_models import Entdaybocp
def filmsbocompare(request):
    datalist1=Entdaybofull.objects.filter(Q(releasedays__range=(1,30)) & (Q(filmname__exact='海王')|Q(filmname__exact='毒液：致命守护者')))\
        .values("filmname", "yearmonthday","releasedays", "daybo").order_by('releasedays','filmname')
    datalist2=Entdaybocp.objects.filter(filmname__in=['海王','毒液：致命守护者'])
    #print("datalist2 is %s" %datalist2)
    #datalist21=serializers.serialize("json", datalist2)
    #filter(filmname__exact="海王")

    #.values("filmname", "yearmonthday","releasedays", "daybo")
    #print("datalist21 is" %datalist21)
    return render(request,'BoApp/filmscompare.html',{"fclist1":datalist1,"fclist2":datalist2})



# from .models import Entdaybofull
# from .mysql_view_models import Entdayboyx
# def entdayboyx(request):
#     datalist1=Entdaybofull.objects.filter(Q(releasedays__range=(1,30)) & (Q(filmname__exact='海王')|Q(filmname__exact='毒液：致命守护者')))\
#         .values("filmname", "yearmonthday","releasedays", "daybo").order_by('releasedays','filmname')
#     datalist2=Entdayboyx.objects.filter(filmname__in=['海王','毒液：致命守护者'])
#     return render(request,'BoApp/filmscompare.html',{"fclist1":datalist1,"fclist2":datalist2})
import datetime
from  datetime import date
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

from .models import Entdaybofull
def entdayboyx(request):
    datalist1=Entdaybofull.objects.filter(Q(releasedays__range=(1,30)) & (Q(filmname__exact='海王')|Q(filmname__exact='毒液：致命守护者')))\
        .values("filmname", "yearmonthday","releasedays", "daybo").order_by('releasedays','filmname')
    datalist2=Entdaybofull.objects.filter(Q(releasedays__range=(1,30)) & Q(filmname__exact='海王'))\
       .values("filmname", "yearmonthday", "releasedays", "daybo")
    datalist21 = list(datalist2)
    datalist22 = json.dumps(datalist21, cls=ComplexEncoder)
    #datalist22=str(datalist22)
    #datalist21 = serializers.serialize("json", datalist2)
    datalist3=Entdaybofull.objects.filter(Q(releasedays__range=(1,30)) & Q(filmname__exact='毒液：致命守护者')) \
        .values("filmname", "yearmonthday", "releasedays", "daybo")
    datalist31 = list(datalist3)
    datalist32 = json.dumps(datalist31, cls=ComplexEncoder)
    return render(request,'BoApp/filmscompare.html',{"fclist1":datalist1,"fclist21":datalist22,"fclist31":datalist32})



def addfilmbocompare(request,filmname):
    filmexists=Entdaybofull.objects.filter(filmname__exact=filmname)
    if filmexists.exists():
        datalist1 = Entdaybofull.objects.filter(Q(releasedays__range=(1, 30)) & Q(filmname__exact='filmname')) \
            .values("filmname", "yearmonthday", "releasedays", "daybo")
    else:pass


# 默认访问页面
#def filmsbocompare_ajax_index
def filmsbocompare_ajax_index(request):
    return render(request, 'boapp/addfilmsandcompare.html')



# Ajax GET 提交数据
def filmsbocompare_ajax_get(request):
    searchfn = request.GET.get("searchfn")
    #1.若该电影存在，返回电影名称；若电影不存在，则返回“该电影不存在，请重新查询！”2.根据输入值进行精确查询
    # filmexist=Entdaybofull.objects.filter(filmname__exact=searchfn).values("filmname").distinct()
    # if filmexist:
    #     filmret=filmexist[0]['filmname']
    # else: filmret="该电影不存在，请重新查询！"
    # return HttpResponse(str(filmret))
    #返回值固定为test进行测试
    #return HttpResponse(str("test"))
    #返回json数据
    filmexist = Entdaybofull.objects.filter(filmname__exact=searchfn).values("filmname").distinct()
    if filmexist:
        #filmret = filmexist[0]['filmname']
        filminfolist = Entdaybofull.objects.filter(Q(releasedays__range=(1, 30)) & Q(filmname__exact=searchfn)) \
            .values("filmname", "yearmonthday", "releasedays", "daybo")
        filminfolist2 = list(filminfolist)
        filminfolist3 = json.dumps(filminfolist2, cls=ComplexEncoder, ensure_ascii=False)
        #return HttpResponse({"datalist":filminfolist3})
        return HttpResponse(filminfolist3)
    else:return HttpResponse("该电影不存在，请重新查询！")




# Ajax POST 提交数据
def filmsbocompare_ajax_post(request):
    return HttpResponse('')


# Ajax 返回 JSON 数据
def filmsbocompare_ajax_json(request):
    return HttpResponse('')





# import pymysql
# import pandas as pd
# import plotly.plotly
# import plotly.graph_objs as pg
#
#
# def bar_chart(host, port, user, passwd, dbname, charset,output_path):
#     try:
#         conn = pymysql.Connection(
#             host=host,
#             port=port,
#             user=user,
#             passwd=passwd,
#             db=dbname,
#             charset=charset
#         )
#         cur = conn.cursor()
#         cur.execute("select filmname, releasedate,1stroundfinalbo from breakrecordstat order by releasedate;")
#
#         rows = cur.fetchall()
#
#         df = pd.DataFrame([[ij for ij in i] for i in rows])
#         print(df)
#         df.rename(columns={ 0: 'filmname', 1: 'releasedate', 2: '1stroundfinalbo'}, inplace=True)
#
#
#         date_bo = pg.Bar(x=df["filmname"], y=df["1stroundfinalbo"],hovertext=df["releasedate"],name="",opacity=0.5,width=0.1)
#
#         date_bo2=pg.Scatter(text=df["releasedate"],textposition='middle center')
#
#         data = [date_bo,date_bo2]
#
#         layout = pg.Layout(barmode='group', title="单片票房里程碑")
#
#         fig = pg.Figure(data=data, layout=layout)
#         plotly.offline.plot(fig, filename=output_path)
#
#
#     finally:
#         if conn:
#             conn.close()



# 默认访问页面
def ajax_index(request):
    return render(request, 'BoApp/ajax_request_bak.html')


# Ajax GET 提交数据
def ajax_get(request):
    # a = request.GET.get("a")
    # b = request.GET.get("b")
    # n = int(a) * int(b)
    # return HttpResponse(str(n))
    searchfn = request.GET.get("searchfn")
    filmexist = Entdaybofull.objects.filter(filmname__exact=searchfn).values("filmname").distinct()
    if filmexist:
        filmret = filmexist[0]['filmname']
    else:
        filmret = "该电影不存在，请重新查询！"
    return HttpResponse(str(filmret))
    #return HttpResponse(str("test"))


# Ajax POST 提交数据
def ajax_post(request):
    return HttpResponse('')


# Ajax 返回 JSON 数据
def ajax_json(request):
    return HttpResponse('')








