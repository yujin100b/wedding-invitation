from abc import ABCMeta
from django.db import models
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.utils.translation import gettext as _
from django.utils import timezone


class HitCount(models.Model):
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
    date = models.DateField(auto_now_add=True)  # 조회수가 올라갔던 날짜 


class Attendance(models.Model):
    method = models.CharField(_("온라인/오프라인"), max_length=50, null=True, blank=True)
    name = models.CharField(_("참여자 이름"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("전화번호"), max_length=50, null=True, blank=True)
    email = models.CharField(_("이메일"), max_length=100, null=True, blank=True)
    attend_time = models.CharField(_("언제부터 방문하실 계획이신가요?"), max_length=50, null=True, blank=True)
    offline_camera_yn = CharField(_("아날로그 사진기 수령 여부"), max_length=2, null=True, blank=True)
    created_date = models.DateTimeField(_("생성일"), default=timezone.now)


class Cheering(models.Model):
    cheer_message = models.TextField(_("응원 메세지"), null=True, blank=True)
    created_date = models.DateTimeField(_("생성일"), default=timezone.now)


class Funding(models.Model):
    name = models.CharField(_("축의금 보낸 이"), max_length=50, null=True, blank=True)
    amount = PositiveBigIntegerField(_("축의금 금액"), null=True, blank=True)
    how_to_spend = models.CharField(_("축의금 어떻게 사용할까요?"), max_length=255, null=True, blank=True)
    address = models.CharField(_("답례품 받을 주소"), max_length=255, null=True, blank=True)
    payment = models.CharField(_("입금 방법"), max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(_("생성일"), default=timezone.now)


class Subscriber(models.Model):
    email = models.CharField(_("이메일"), max_length=100, null=True, blank=True)
    where_to_regist = models.CharField(_("결혼식 이후의 소식/중요한 순간"), max_length=50)