from django.db import models
from datetime import datetime, date


# Create your models here.
class Prices(models.Model):
    flange_id = models.AutoField(primary_key=True)
    date = models.CharField(u'更新日期', max_length=20, default=datetime.strftime(date.today(), '%y-%m-%d'))
    flange_specifications = models.TextField(u'品名')
    flange_varieties = models.TextField(u'规格')
    flange_single_price = models.FloatField(u'单价')
    stocks_nums = models.IntegerField(u'数量')

    class Meta:
        verbose_name = '价目表'
        verbose_name_plural = '价目表'

    def __str__(self):
        return f'{self.flange_specifications} {self.flange_varieties}'


class Specifications(models.Model):
    flange_specifications = models.TextField(u'品名')

    class Meta:
        verbose_name = '型号'
        verbose_name_plural = '型号'

    def __str__(self):
        return self.flange_specifications


class Warehouse(models.Model):
    order_id = models.AutoField(primary_key=True)
    date = models.CharField(u'更新日期', max_length=20, default=datetime.strftime(date.today(), '%y-%m-%d'))
    flange_specifications = models.TextField(u'品名')
    flange_varieties = models.TextField(u'规格')
    flange_single_price = models.FloatField(u'单价')
    order_nums = models.IntegerField(u'数量')
    order_sum = models.FloatField(u'订单总价')
    provider = models.TextField(u'供货商')

    class Meta:
        verbose_name = '入库单'
        verbose_name_plural = '入库单'

    def __str__(self):
        return f'{self.date} {self.provider}'


class Issue(models.Model):
    order_id = models.AutoField(primary_key=True)
    date = models.CharField(u'出库日期', max_length=20, default=datetime.strftime(date.today(), '%y-%m-%d'))
    flange_specifications = models.TextField(u'品名')
    flange_varieties = models.TextField(u'规格')
    flange_single_price = models.FloatField(u'单价')
    order_nums = models.IntegerField(u'数量')
    order_sum = models.FloatField(u'订单总价')
    customer = models.TextField(u'提货单位')

    class Meta:
        verbose_name = '出库单'
        verbose_name_plural = '出库单'

    def __str__(self):
        return f'{self.date} {self.customer}'


class Stocks(models.Model):
    flange_specifications = models.TextField(u'品名')
    flange_varieties = models.TextField(u'规格')
    order_nums = models.IntegerField(u'数量')

    class Meta:
        verbose_name = '库存'
        verbose_name_plural = '库存'

    def __str__(self):
        return f'{self.flange_specifications} {self.flange_varieties}'
