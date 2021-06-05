from abc import ABCMeta
from django.db import models
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.utils.translation import gettext as _
from .util import randomword


class Letter(models.Model):
    target = models.CharField(_("개인/단체"), max_length=50, null=True, blank=True)
    relation = models.CharField(_("친구/어른/모임/친지"), max_length=50, null=True, blank=True)
    lang = models.CharField(_("한국/영어"), max_length=50, null=True, blank=True)
    invitee = models.CharField(_("박재용/서새롬"), max_length=50, null=True, blank=True)
    code = models.CharField(_("unique code"), max_length=50, unique=True, default=randomword(5), primary_key=True) 
    message = models.TextField(_("개별 메세지"), null=True, blank=True)
    name= models.CharField(_("이름"), max_length=50, null=True, blank=True)
    honor= models.CharField(_("직함"), max_length=50, null=True, blank=True)
    full_name= models.CharField(_("풀네임"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("전화번호"), max_length=50, null=True, blank=True)
    email = models.CharField(_("이메일"), max_length=50, null=True, blank=True)

    @property
    def url(self):
        return f"saeromsuh.jaeyongpark/wedding/{self.code}"


class Attendance(models.Model):
    attend_yn = models.CharField(_("참석 여부"), max_length=50, null=True, blank=True)
    method = models.CharField(_("온라인/오프라인"), max_length=50, null=True, blank=True)
    name = models.CharField(_("참여자 이름"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("전화번호"), max_length=50, null=True, blank=True)
    email = models.CharField(_("이메일"), max_length=100, null=True, blank=True)
    bgm = models.CharField(_("결혼식에 듣고 싶은 BGM"), max_length=255, null=True, blank=True)
    get_paper_invitation = models.CharField(max_length=2, default='N', null=True, blank=True)
    junior_name = models.CharField(_("2세 이름"), max_length=50, null=True, blank=True)
    attend_time = models.CharField(_("언제부터 방문하실 계획이신가요?"), max_length=50, null=True, blank=True)
    offline_camera_yn = CharField(_("아날로그 사진기 수령 여부"), max_length=2, null=True, blank=True)
    created_date = models.DateField(_("생성일"), auto_now_add=True)


class Cheering(models.Model):
    name = models.CharField(_("응원자 이름"), max_length=50, default="unknown", null=True, blank=True)
    cheer_message = models.TextField(_("응원 메세지"), null=True, blank=True)
    created_date = models.DateField(_("생성일"), auto_now_add=True)


class Funding(models.Model):
    name = models.CharField(_("축의금 보낸 이"), max_length=50)
    amount = PositiveBigIntegerField(_("축의금 금액"))
    how_to_spend = models.CharField(_("축의금 어떻게 사용할까요?"), max_length=255, null=True, blank=True)
    address = models.CharField(_("답례품 받을 주소"), max_length=255, null=True, blank=True)
    payment = models.CharField(_("입금 방법"), max_length=50)
    created_date = models.DateField(_("생성일"), auto_now_add=True)


class Subscriber(models.Model):
    name = models.CharField(_("응원자 이름"), max_length=50, default="unknown", null=True, blank=True)
    email = models.CharField(_("이메일"), max_length=100, null=True, blank=True)
    where_to_regist = models.CharField(_("결혼식 이후의 소식/중요한 순간"), max_length=50)