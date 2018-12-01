from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Product(models.Model):
    sn = models.CharField(default='', max_length=128, null=True, blank=True, verbose_name='产品编号')
    name = models.CharField(default='', max_length=128, null=True, blank=True, verbose_name='品名')
    logo = models.ImageField(max_length=200, null=True, blank=True, upload_to='./images', verbose_name='logo图片')
    weight = models.CharField(default='', max_length=128, null=True, blank=True, verbose_name='净含量')
    mixture = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='配料')
    mixture_origin = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='原料产地')
    mixture_country = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='原产国(地区)(原料)')
    mixture_company = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='生产企业名称(原料)')
    mixture_company_address = models.CharField(default='', max_length=256, null=True, blank=True,
                                               verbose_name='生产企业地址(原料)')
    mixture_company_registration = models.CharField(default='', max_length=256, null=True, blank=True,
                                                    verbose_name='生产企业注册号(原料)')
    mixture_batch_number = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='生产批号(原料)')
    mixture_production_date = models.DateField(default=timezone.now, null=True, blank=True,
                                               verbose_name='生产日期(原料)')
    mixture_expiration_date = models.CharField(default='', max_length=32, null=True, blank=True, verbose_name='保质期(原料)')
    mixture_storage_conditions = models.CharField(default='', max_length=256, null=True, blank=True,
                                                  verbose_name='贮藏条件(原料)')
    mixture_format = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='规格(原料)')
    mixture_destination = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='目的地(原料)')
    executive_standard = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='产品执行标准')
    production_date = models.DateField(default=timezone.now, null=True, blank=True, verbose_name='生产日期')
    expiration_date = models.CharField(default='', max_length=32, null=True, blank=True, verbose_name='保质期')
    storage_conditions = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='贮藏条件')
    authorized_agent = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='授权委托商')
    authorized_agent_address = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='地址')
    product_code = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='产品编码')

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ManufacturerInfo(models.Model):
    manufacturer = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='生产商')
    address = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='地址')
    production_origin = models.CharField(default='', max_length=256, null=True, blank=True, verbose_name='产地')
    phone = models.CharField(default='', max_length=32, null=True, blank=True, verbose_name='电话')

    class Meta:
        verbose_name = '生产商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.manufacturer


class User(AbstractUser):
    name = models.CharField(default='', max_length=32, null=True, blank=True, verbose_name='姓名')
    user_info = models.ForeignKey(ManufacturerInfo, null=True, blank=True, on_delete=models.SET_NULL,
                                  verbose_name='生产商')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
