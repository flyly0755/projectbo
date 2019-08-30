from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)/$',views.returnnum),
    url(r'^(\d+)/(\d+)/$',views.returnnums),
    url(r'^totalboannual/$',views.totalboannual),
    url(r'^filmborank/$',views.filmborank),
    url(r'^filmborank/(\d+)$',views.filmborankAgivenyear),
    url(r'^attributes/$',views.attributes),
    url(r'^get1/$',views.get1),
    url(r'^get2/$',views.get2),
    url(r'^register/$',views.register),
    url(r'^registerresult/$',views.registerresult),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^afterlogin/$',views.afterlogin),
    url(r'^logoff/$',views.logoff),
    url(r'^mlborankpagnation/$',views.mlborankpagnation),
    url(r'^mlborankpagnation2/(\d{4}|$)',views.mlborankpagnation2),
    url(r'^film1stdaybo/$',views.film1stdaybo),
    url(r'^daytotalbo/$',views.daytotalbo),
    url(r'^daytotalbo/festival=(.+?)$',views.daytotalbofestival),
    #url(r'^daytotalbo/?festival=(平安夜)$',views.daytotalbofestival),
    #url(r'^daytotalbo/festival=(\d)$',views.daytotalbofestival),
    url(r'^xaddy/$', views.sumtest),
    url(r'^calendarinfo/$', views.calendarinfo),
    url(r'^breakrecordstat/$', views.breakrecordstat),
    url(r'^filmsbocompare/$',views.filmsbocompare),
    url(r'^entdayboyx/$',views.entdayboyx),
    url(r'^addfilmsandcompare/index/$',views.filmsbocompare_ajax_index),
    url(r'^addfilmsandcompare/get/$', views.filmsbocompare_ajax_get),
    url(r'^addfilmsandcompare/post/$', views.filmsbocompare_ajax_post),
    url(r'^addfilmsandcompare/json/$', views.filmsbocompare_ajax_json),
    url(r'^ajax/index/', views.ajax_index),
    url(r'^ajax/get/', views.ajax_get),
    url(r'^ajax/post/', views.ajax_post),
    url(r'^ajax/json/', views.ajax_json)

]