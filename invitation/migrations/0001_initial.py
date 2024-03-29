# Generated by Django 3.2.3 on 2021-05-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, max_length=50, null=True, verbose_name='온라인/오프라인')),
                ('invitee', models.CharField(blank=True, max_length=50, null=True, verbose_name='참여자 이름')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='전화번호')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='이메일')),
                ('bgm', models.CharField(blank=True, max_length=255, null=True, verbose_name='결혼식에 듣고 싶은 BGM')),
                ('get_paper_invitation', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='생성일')),
            ],
        ),
        migrations.CreateModel(
            name='Cheering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='unknown', max_length=50, null=True, verbose_name='응원자 이름')),
                ('cheer_message', models.TextField(blank=True, null=True, verbose_name='개별 메세지')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='생성일')),
            ],
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='축의금 보낸 이')),
                ('amount', models.PositiveBigIntegerField(verbose_name='축의금 금액')),
                ('how_to_spend', models.CharField(blank=True, max_length=255, null=True, verbose_name='축의금 어떻게 사용할까요?')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='답례품 받을 주소')),
                ('payment', models.CharField(max_length=50, verbose_name='입금 방법')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='생성일')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(blank=True, max_length=50, null=True, verbose_name='개인/단체')),
                ('relation', models.CharField(blank=True, max_length=50, null=True, verbose_name='친구/어른/모임/친지')),
                ('lang', models.CharField(blank=True, max_length=50, null=True, verbose_name='한국/영어')),
                ('inviter', models.CharField(blank=True, max_length=50, null=True, verbose_name='박재용/서새롬')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='unique code')),
                ('message', models.TextField(blank=True, null=True, verbose_name='개별 메세지')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='unknown', max_length=50, null=True, verbose_name='응원자 이름')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='이메일')),
                ('where_to_regist', models.CharField(max_length=50, verbose_name='결혼식 이후의 소식/중요한 순간')),
            ],
        ),
    ]
