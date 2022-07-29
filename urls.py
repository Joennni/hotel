
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('event/',views.event),
    path('prod/',views.prod),
    path('buyer/',views.buyer),
    path('plot/',views.plot),
    path('update_suc/',views.update_suc),
    path('update/',views.update),
    path('board_done/',views.board_done),
    path('board_write/',views.board_write),
    path('join_suc/',views.join_suc),
    path('join/',views.join),
    path('bussiness/',views.bussiness),
    path('deluxe/',views.deluxe),
    path('suite/',views.suite),
    path('twin/',views.twin),
    path('board/',views.board),
    path('reserve/',views.reserve),
    path('reserve_info/',views.reserve_info),
    path('reserve_in4/',views.reserve_in4),
    path('ad_room/',views.ad_room),
    path('board/',views.board),
    path('ad_reserve/',views.ad_reserve),
    path('ad_search/',views.ad_search),
    path('ad_mem/',views.ad_mem),
    path('ad_mem_delete/<int:inid>',views.ad_mem_delete),
    path('login/',views.login),
    path('login_ing/',views.login_ing),
    path('logout/',views.logout),
    path('hotel_info/',views.hotel_info),
    path('room/',views.room),
    path('index/',views.index),
]
