from pickle import FALSE
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

import hotelapp.model_df.board as bod
import hotelapp.model_df.reserve as re
import hotelapp.model_df.ad_room as ar
import hotelapp.model_df.ad_mem as adm
import hotelapp.model_df.ad_reserve as adre
import hotelapp.model_df.test as ts
import hotelapp.model_df.ad_bp as bp
import hotelapp.model_df.event as et
import hotelapp.model_df.login as lg

def index(request):
    return render(request,
                "hotelapp/index.html", {})

def room(request):
    return render(request,
                "hotelapp/room.html", {})
    
def reserve_info(request):
    return render(request,
                "hotelapp/reserve_info.html", {})
def reserve(request):
    return render(request,
                "hotelapp/reserve.html", {})
    
def hotel_info(request):
    return render(request,
                "hotelapp/hotel_info.html", {})
    
def login(request):
    return render(request,"hotelapp/login.html", {})

def login_ing(request):
    id = request.GET.get("mem_id")
    pw = request.GET.get("mem_pw")
    result = lg.login(id, pw)
    if result is None :
        return render(request,"hotelapp/login.html", {})
    html = render(request, 'hotelapp/login_ing.html', {})
    html.set_cookie('mem_id', id, max_age=None)
    html.set_cookie('mem_pw', pw, max_age=None)
    html.set_cookie('mem_inid', result[0], max_age=None)
    return html

def logout(request):
    html = render(request, 'hotelapp/login_ing.html', {})
    html.delete_cookie('mem_id')
    html.delete_cookie('mem_pw')
    html.delete_cookie('mem_inid')
    return html
    
def ad_reserve(request):
    return render(request,
                "hotelapp/ad_reserve.html", {})
    
def ad_room(request):
    return render(request,
                "hotelapp/ad_room.html", {})
    
def twin(request):
    return render(request,
                "hotelapp/room/twin.html", {})
def suite(request):
    return render(request,
                "hotelapp/room/suite.html", {})
def deluxe(request):
    return render(request,
                "hotelapp/room/deluxe.html", {})
def bussiness(request):
    return render(request,
                "hotelapp/room/bussiness.html", {})
    
def board_write(request):
    return render(request,
                "hotelapp/board_write.html", {})
    
def buyer(request):
    buyer = bp.get_Buyer()
    context = {"buyer":buyer}
    return render(request,
                "hotelapp/ad_buyer.html", context)
    
def prod(request):
    prod = bp.get_Prod()
    context = {"prod":prod}
    return render(request,
                "hotelapp/ad_prod.html", context)
    
def event(request):
    return render(request,
                "hotelapp/event.html", {})

def board(request):
    bd = bod.board()
    
    pg = Paginator(bd, 10)
    page = int(request.GET.get('page', 1))
    board_list = pg.get_page(page)
    
    context = {"board_list" : board_list}
    return render(request, "hotelapp/board.html", context)
    
def reserve(request):
    return render(request,
                    "hotelapp/reserve.html", {})

def reserve_info(request):
    mem = request.COOKIES['mem_inid']
    if request.GET.get('res_rmnum') == "오션뷰":
        rmnum = str(501)
    elif request.GET.get('res_rmnum') == "마운틴뷰":
        rmnum = str(503)
    else:
        rmnum = str(505)
    c_in = request.GET.get('res_in')
    c_out = request.GET.get('res_out')
    adult= request.GET.get('res_adult')
    kid= request.GET.get('res_kid')
    baby= request.GET.get('res_baby')
    name = request.GET.get('mem_name')
    email = request.GET.get('mem_email')
    tel = request.GET.get('mem_tel')
    cardno = request.GET.get('mem_cardno')
    cardpw = request.GET.get('mem_cardpw')
    
    df1 = re.getReserve_list(mem, rmnum, c_in, c_out, adult, kid, baby, name, email, tel, cardno, cardpw)
    df2 = re.getReserve_list(mem, rmnum, c_in, c_out, adult, kid, baby,  name, email, tel, cardno, cardpw)
    context = {"df1" : df1, "df2" : df2}
    return render(request,
                    "hotelapp/reserve_info.html", context)
    
def reserve_in4(request):
    mem = request.COOKIES['mem_inid']
    info = re.getReserve_info1(mem)
    context = {"info": info}
    return render(request,
                'hotelapp/reserve_in4.html', context)
    
def ad_room(request):
    adr = ar.ad_room()
    context = {"adr" : adr}
    return render(request,
                "hotelapp/ad_room.html", context)
    
def ad_reserve(request):
    asdf = adre.ad_Reserve()
    
    pg = Paginator(asdf, 10)
    page = int(request.GET.get('page', 1))
    board_list = pg.get_page(page)
    
    context = {"board_list" : board_list} 
    return render(request,
                "hotelapp/ad_reserve.html", context)

def ad_search(request):
    in_date = request.GET.get('in_date')
    out_date = request.GET.get('out_date')
    if in_date is None:
        in_date = request.COOKIES['in_date']
    if out_date is None:
        out_date = request.COOKIES['out_date']
    
    asdf = adre.ad_Search(1, in_date, out_date)
    
    pg = Paginator(asdf, 10)
    page = int(request.GET.get('page', 1))
    board_list = pg.get_page(page)
    
    context = {"board_list" : board_list} 
    
    html = render(request, "hotelapp/ad_reserve.html", context)
    html.set_cookie('in_date', in_date)
    html.set_cookie('out_date', out_date)
    
    return html

def update(request):
    id = request.COOKIES['mem_id']
    result = adm.update(id)
    data = {"data" : result}
    
    return render(request, 'hotelapp/update.html', data)


def update_suc(request):
    id = request.COOKIES['mem_inid']
    pw = request.GET.get('mem_pw')
    regno = request.GET.get('mem_regno')
    tel = request.GET.get('mem_tel')
    email = request.GET.get('mem_email')
    result = adm.update_suc(id, pw, regno, tel, email)
    
    return render(request, 'hotelapp/update_suc.html', {})

def ad_mem(request):
    result = adm.adminMemberShow()

    data = {"data" : result}
    return render(request, 'hotelapp/ad_mem.html', data)

def ad_mem_delete(request, inid):
    result = adm.adminMemberDelete(str(inid))
    
    data = {"data" : result}
    return render(request, 'hotelapp/ad_mem.html', data)

def plot(request):
    ts.get_Plot()
    ts.test()
    ts.monthlycount()
    return render(request, 'hotelapp/plot.html', {})

def event(request):
    eve = et.get_event()
    asdf = {"eve" : eve}
    return render(request, 'hotelapp/event.html', asdf)



def join(request):
    return render(request, 'hotelapp/join.html', {})

def join_suc(request):
    id = request.GET.get('mem_id')
    pw = request.GET.get('mem_pw')
    m_name = request.GET.get('mem_name')
    m_email = request.GET.get('mem_email')
    tel = request.GET.get('mem_tel')
    regno = request.GET.get('mem_regno')
    if request.GET.get('mem_gender') == '남성':
        gender = '1'
    else:
        gender = '0'
    result = adm.join(id,pw, m_name, m_email, tel, regno, gender)
    data = {"data" : result}
    
    return render(request, 'hotelapp/join_suc.html', data)


def board_done(request):
    id = request.COOKIES['mem_inid']
    ti = request.GET.get('post_title')
    cont = request.GET.get('post_cont')
    date = request.GET.get('post_date')
    if request.GET.get('post_hide') == '비밀글':
        phide = '1'
    else:
        phide = '0'
    
    bod.bdw(id, ti, cont, date, phide)
    return render(request, 'hotelapp/board_done.html', {})