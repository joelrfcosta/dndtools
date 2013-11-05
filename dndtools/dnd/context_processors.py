# -*- coding: utf-8 -*-
from dndtools.dnd.models import NewsEntry


def unread_news(request):
    count = 0
    if 'top_news' in request.COOKIES:
        count = len(NewsEntry.objects.filter(enabled=True, pk__gt=request.COOKIES['top_news']))
    else:
        count = len(NewsEntry.objects.filter(enabled=True))

    count = min(15, count)

    return {
        'unreadNewsCount': count,
    }


def disable_social(request):
    return {
        'disable_social': 'disable_social' in request.COOKIES,
    }


def is_mobile(request):
    mobile = False
    if hasattr(request, 'is_mobile') and request.is_mobile:
        mobile = True

    return {
        'is_mobile': mobile,
    }


def is_admin(request):
    return {
        'is_admin': request.user.is_staff and request.user.is_active,
    }