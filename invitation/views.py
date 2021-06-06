
from datetime import datetime, timedelta
from django.utils import timezone
from collections import Counter
from django.http import JsonResponse
from django.db.models.query_utils import Q
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Max
from .serializers import LetterSerializer, AttendanceSerializer, CheeringSerializer, FundingSerializer, SubscriberSerializer
from .models import HitCount, Letter, Attendance, Cheering, Funding, Subscriber


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class CheeringViewSet(viewsets.ModelViewSet):
    queryset = Cheering.objects.all()
    serializer_class = CheeringSerializer


class FundingViewSet(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def hit(request):
    ip = _get_client_ip(request)
    try:
        # ip주소와 게시글 번호로 기록을 조회함
        hits = HitCount.objects.get(ip=ip)
    except Exception as e:
        # 처음 게시글을 조회한 경우엔 조회 기록이 없음
        print(e)
        hits = HitCount(ip=ip)
        hits.save()
    else:
        # 조회 기록은 있으나, 날짜가 다른 경우
        if not hits.date == datetime.now().date():
            hits = HitCount(ip=ip)
            hits.save()
        # 날짜가 같은 경우
        else:
            print(str(ip) + ' has already hit this post.\n\n')
    return Response('ok')



def funfact(self):
    count = HitCount.objects.count()
    all_attend_count = Attendance.objects.count()
    online_attend_count = Attendance.objects.filter(method="offline").count()
    not_attend_count = Attendance.objects.filter(attend_yn="N", email__isnull=False).count()
    recently_fund_pk = Funding.objects.count()
    recently_fund = Funding.objects.get(id=recently_fund_pk-1)
    all_name = Funding.objects.values('name').all()
    all_surname = [name['name'][0] for name in all_name]
    max_surname=Counter(all_surname).most_common(1)
    key, _ = max_surname[0]

    all_amount = Funding.objects.values('amount').all()
    all_amount_len = [len(str(amount['amount'])) for amount in all_amount]
    max_amount_len = Counter(all_amount_len).most_common(1)
    key_len, _ = max_amount_len[0]

    max_amount = Funding.objects.aggregate(max_amount=Max('amount'))
    max_amount = Funding.objects.filter(amount = max_amount['max_amount']).last()
    addr_list = max_amount.address.split(' ')

    if len(addr_list) > 1:
        max_amount_addr = f"{addr_list[0]} {addr_list[1]}"
    elif len(addr_list) == 1:
        max_amount_addr = addr_list[0]
    else:
        max_amount_addr = "none"
    

    all_bgm = Attendance.objects.values('bgm').exclude(Q(bgm__isnull=True) |Q(bgm=''))
    all_bgm_trimd = [i['bgm'].lower().replace(' ', '') for i in all_bgm]
    max_count_bgm = Counter(all_bgm_trimd).most_common(1)


    seconds_elapsed = timezone.now() - recently_fund.created_date
    


    response = {
        "hit" : count,
        "online" : int(online_attend_count / all_attend_count * 100),
        "highlight": int(not_attend_count / all_attend_count * 100),
        "recent_name": recently_fund.name,
        "recent_time": int(seconds_elapsed.total_seconds()),
        "max_surname": key,
        "max_amount_len" : key_len,
        "max_amount_addr" : max_amount_addr,
        "max_count_bgm" : max_count_bgm[0][0],
    }
    print(response)
    return JsonResponse({'r': response})
    


