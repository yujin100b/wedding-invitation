
from datetime import datetime, timedelta
from django.utils import timezone
from collections import Counter
from django.http import JsonResponse
from django.db.models.query_utils import Q
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Max
from .serializers import AttendanceSerializer, CheeringSerializer, FundingSerializer, SubscriberSerializer
from .models import HitCount, Attendance, Cheering, Funding, Subscriber


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
        hits = HitCount.objects.create(ip=ip)
    else:
        # 조회 기록은 있으나, 날짜가 다른 경우
        if not hits.date == datetime.now().date():
            hits = HitCount.objects.create(ip=ip)
        # 날짜가 같은 경우
        else:
            print(str(ip) + ' has already hit this post.\n\n')
    return Response('ok')


def left_seat(reqest):
    flea_market = Attendance.objects.filter(attend_time="벼룩시장").count()
    wedding = Attendance.objects.filter(attend_time="메인 이벤트").count()
    after_wedding = Attendance.objects.filter(attend_time="피로연").count()

    response = {
        "flea_market": 100 - flea_market,
        "wedding": 30 - wedding,
        "after_wedding": 100 - after_wedding
    }

    return JsonResponse({'r': response})


def funfact(request):
    count = HitCount.objects.count()
    all_attend_count = Attendance.objects.count()
    online_attend_count = Attendance.objects.filter(method="online").count()
    not_attend_count = Attendance.objects.filter(email__isnull=False).count()

    recently_fund_pk = Funding.objects.all().last()
    recently_fund = Funding.objects.get(id=recently_fund_pk.id-1)

    all_name = Funding.objects.values('name').all()
    all_surname = [name['name'][0] for name in all_name]

    max_surname = Counter(all_surname).most_common(1)
    key, _ = max_surname[0]

    all_amount = Funding.objects.values('amount').all()
    all_amount_len = [len(str(amount['amount'])) for amount in all_amount]

    max_amount_len = Counter(all_amount_len).most_common(1)
    key_len, _ = max_amount_len[0]

    max_amount = Funding.objects.aggregate(max_amount=Max('amount'))
    max_amount = Funding.objects.filter(amount=max_amount['max_amount']).last()
    addr_list = max_amount.address.split(' ')

    if len(addr_list) > 1:
        max_amount_addr = f"{addr_list[0]} {addr_list[1]}"
    elif len(addr_list) == 1:
        max_amount_addr = addr_list[0]
    else:
        max_amount_addr = "none"

    seconds_elapsed = timezone.now() - recently_fund.created_date

    import random

    random_en = [
        "Harvey J. Locke wrote (in 1953) that the modern families are turning from institutional organizations to fellowships.",
        '''"Today's lifelong development tasks for youths, such as college admissions, graduation, employment, and marriage, and childbirth, are closely related to the polarization and unequal economic structure of Korean society."
- Tae Young So, "Spiritual Education as a Way to Overcome the Inferiority of the Korean Emerging Adulthood." Christian Education & Information Technology 50, 2016.9, 119-153'''
    ]

    random_ko = [ 
        '''Harvey J. Locke는 현대사회에서 가족이 "제도적 가족에서 우애적 가족으로" 변화 중이라고 (1953년에) 말했습니다.  ''',
        '''"오늘날 청년들의 대학입학과 졸업, 취업, 그리고 결혼과 출산 등과 같은 청년기 생애 발달 과업들은 한국사회의 양극화와 불평등한 경제구조와 밀접하게 관련되어 있다."
- 소태영, "수저계급론 논쟁의 중심에 선 한국 청년들의 열등감 극복을 위한 영성교육" (기독교교육정보 50, 2016.9, 119-153)'''
    ]

    random_index =random.randrange(0,len(random_ko))


    response = {
        "hit": count,
        "online": int(online_attend_count / all_attend_count * 100),
        "highlight": int(not_attend_count / all_attend_count * 100),
        "recent_name": recently_fund.name,
        "recent_time": int(seconds_elapsed.total_seconds()),
        "max_surname": key,
        "max_amount_len": key_len,
        "max_amount_addr": max_amount_addr,
        "random_en": random_en[random_index],
        "random_ko": random_ko[random_index]
        }
    return JsonResponse({'r': response})
