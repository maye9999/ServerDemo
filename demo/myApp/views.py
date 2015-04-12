from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from myApp.models import InfoPack, TransmitEntry
from base64 import b64decode
from json import dumps
# Create your views here.


def login_view(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        response_data = {'code': 0, 'text': 'Login Successful'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    else:
        response_data = {'code': 1, 'text': 'Invalid username or password'}
        return HttpResponse(dumps(response_data), content_type="application/json")


def logout_view(request):
    if logged_in_or_auth(request):
        auth.logout(request)
    response_data = {'code': 0, 'text': 'Logout Successful'}
    return HttpResponse(dumps(response_data), content_type="application/json")


def register_view(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    if User.objects.filter(username=username).exists():
        response_data = {'code': 1, 'text': 'Username Already Existed!'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    if username and password:
        # TODO: check the password length
        user = User.objects.create_user(username=username, password=password)
        info_pack = InfoPack()
        info_pack.user = user
        info_pack.balance = 0
        info_pack.flow = 0
        # TODO: UUID Save
        info_pack.save()
        response_data = {'code': 0, 'text': 'Register Successfully'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    else:
        response_data = {'code': 2, 'text': 'Invalid Username'}
        return HttpResponse(dumps(response_data), content_type="application/json")


def get_info(request):
    if not logged_in_or_auth(request):
        response_data = {'code': 1, 'text': 'Not Login!'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    info_pack = request.user.infopack
    response_data = {"code": 0,
                        "user": request.user.username,
                        "balance": info_pack.balance,
                        "flow": info_pack.flow}
    return HttpResponse(dumps(response_data), content_type="application/json")


def set_info(request):
    if not logged_in_or_auth(request):
        response_data = {'code': 1, 'text': 'Not Login!'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    info_pack = request.user.infopack
    balance = request.GET.get("balance", 0)
    flow = request.GET.get("flow", 0)
    if balance:
        info_pack.balance = balance
    if flow:
        info_pack.flow = flow
    info_pack.save()
    return get_info(request)


def get_transmit_entries_from(request):
    if not logged_in_or_auth(request):
        response_data = {'code': 1, 'text': 'Not Login!'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    entries = request.user.entries_from.all()
    history = list()
    for entry in entries:
        item = dict()
        item["user from"] = entry.user_from.username
        item["user to"] = entry.user_to.username
        item["date"] = entry.date_time.date().isoformat()
        item["time"] = entry.date_time.time().isoformat()
        item["flow"] = entry.flow
        history.append(item)
    response_data = {"code": 0, "data": history}
    return HttpResponse(dumps(response_data), content_type="application/json")


def get_transmit_entries_to(request):
    if not logged_in_or_auth(request):
        response_data = {'code': 1, 'text': 'Not Login!'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    entries = request.user.entries_to.all()
    history = list()
    for entry in entries:
        item = dict()
        item["user from"] = entry.user_from.username
        item["user to"] = entry.user_to.username
        item["date"] = entry.date_time.date().isoformat()
        item["time"] = entry.date_time.time().isoformat()
        item["flow"] = entry.flow
        history.append(item)
    response_data = {"code": 0, "data": history}
    return HttpResponse(dumps(response_data), content_type="application/json")


def add_new_entry(request):
    user_from = request.GET.get("user_from", "")
    user_to = request.GET.get("user_to", "")
    flow = request.GET.get("flow", 0)
    if not user_to or not user_from or not flow:
        response_data = {'code': 1, 'text': 'Missing Arguments'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    user_from = User.objects.get_by_natural_key(user_from)
    user_to = User.objects.get_by_natural_key(user_to)
    if user_from is None or user_to is None:
        response_data = {'code': 2, 'text': 'Username Not Exists'}
        return HttpResponse(dumps(response_data), content_type="application/json")
    entry = TransmitEntry.create(user_from, user_to, flow)
    entry.save()
    response_data = {'code': 0, 'text': 'Entry Added'}
    return HttpResponse(dumps(response_data), content_type="application/json")


def logged_in_or_auth(request):
    if request.user.is_authenticated():
        return True
    if 'HTTP_AUTHORIZATION' in request.META:
        au = request.META['HTTP_AUTHORIZATION'].split()
        if len(au) == 2:
            if au[0].lower() == "basic":
                username, password = b64decode(au[1]).split(':')
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        request.user = user
                        return True
    return False