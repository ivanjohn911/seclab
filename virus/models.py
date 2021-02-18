from django.db import models
from datetime import datetime

# Create your models here.


class virus_record(models.Model):
    # ID
    id = models.AutoField(verbose_name='序号', primary_key=True)
    # 笔记本IP地址
    pcip = models.CharField(verbose_name='IP地址',
                            max_length=128, blank=True, null=True)
    # 用户姓名
    username = models.TextField(
        max_length=30, verbose_name='姓名', blank=True, null=True)
    # 笔记本编号
    number = models.TextField(
        max_length=30, verbose_name='编号', blank=True, null=True)
    # 计算机名
    pcname = models.TextField(
        max_length=30, verbose_name='计算机名', blank=True, null=True)
    # 处理情况
    status = models.TextField(verbose_name='处理情况', blank=True, null=True)
    # 处理时间
    handle_time = models.DateField(verbose_name='处理时间', blank=True, null=True)
    # 备注
    remarks = models.TextField(
        max_length=100, verbose_name='备注', blank=True, null=True)
    # 病毒种类
    virus_type = models.TextField(max_length=100,
                                  verbose_name='病毒种类', blank=True, null=True, default='挖矿病毒')
    # MAC地址
    pcmac = models.TextField(
        max_length=50, verbose_name='MAC', blank=True, null=True)

    class Meta:
        verbose_name = '病毒记录表'
        verbose_name_plural = verbose_name


def __str__(self):
    return self.name


class mail_info(models.Model):
    # 用户姓名
    username = models.ForeignKey(
        virus_record, on_delete=models.CASCADE, verbose_name='姓名')
    # 邮箱
    usermail = models.TextField(max_length=100, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户邮箱表'
        verbose_name_plural = verbose_name


def __str__(self):
    return self.name


class asset(models.Model):
    # ID
    id = models.AutoField(verbose_name='序号', primary_key=True)
    # 是否完成
    Finish = models.TextField(verbose_name='是否完成', blank=True, null=True)
    # 需求来源
    Source = models.TextField(
        max_length=30, verbose_name='需求来源', blank=True, null=True)
    # 单据号
    Document_No = models.TextField(
        max_length=50, verbose_name='单据号', blank=True, null=True)
    # 采购订单号
    Order_No = models.TextField(
        max_length=50, verbose_name='采购订单号', blank=True, null=True)
    # 请购日期
    Requisition_date = models.DateField(
        verbose_name='请购日期', blank=True, null=True)
    # 请购物资/固定资产
    Materials = models.TextField(max_length=300,
                                 verbose_name='请购物资/固定资产', blank=True, null=True)
    # 请购部门
    Department = models.TextField(
        max_length=50, verbose_name='请购部门', blank=True, null=True)
    # 请购人
    Requisitioner = models.TextField(
        max_length=30, verbose_name='请购人', blank=True, null=True)
    # 请购数量
    Requisition_Num = models.CharField(max_length=20,
                                       verbose_name='请购数量', blank=True, null=True)
    # 请购用途
    Requisition_purpose = models.TextField(max_length=300,
                                           verbose_name='请购用途', blank=True, null=True)
    # 采购订单生成时间
    Order_Time = models.DateField(
        verbose_name='采购订单生成时间', blank=True, null=True)
    # 采购员
    Purchaser = models.TextField(
        max_length=30, verbose_name='采购员', blank=True, null=True)
    # 超长原因说明
    Reason = models.TextField(
        max_length=300, verbose_name='超长原因说明', blank=True, null=True)
    # 供应商
    Supplier = models.TextField(
        max_length=100, verbose_name='供应商', blank=True, null=True)
    # 预计到货时间（采购回复）
    Arrival_time1 = models.DateField(
        verbose_name='预计到货时间（采购回复）', blank=True, null=True)
    # 预计到货时间（供应商回复）
    Arrival_time2 = models.DateField(
        verbose_name='预计到货时间（供应商回复）', blank=True, null=True)
    # 实际到货时间（一）
    Actual_time1 = models.DateField(
        verbose_name='实际到货时间（一）', blank=True, null=True)
    # 实际到货数量（一）
    Actual_Num1 = models.CharField(max_length=20,
                                   verbose_name='实际到货数量（一）', blank=True, null=True)
    # 实际到货时间（二）
    Actual_time2 = models.DateField(
        verbose_name='实际到货时间（二）', blank=True, null=True)
    # 实际到货数量（二）
    Actual_Num2 = models.CharField(max_length=20,
                                   verbose_name='实际到货数量（二）', blank=True, null=True)
    # 实际到货时间（三）
    Actual_time3 = models.DateField(
        verbose_name='实际到货时间（三）', blank=True, null=True)
    # 实际到货数量（三）
    Actual_Num3 = models.CharField(max_length=20,
                                   verbose_name='实际到货数量（三）', blank=True, null=True)
    # 未到数量
    Unarrival_Num = models.CharField(max_length=20,
                                     verbose_name='未到数量', blank=True, null=True)
    # 是否超期
    Overdue = models.TextField(verbose_name='是否超期', blank=True, null=True)
    # 超期时间
    Overdue_time = models.CharField(
        max_length=20, verbose_name='超期时间', blank=True, null=True)
    # 备注
    Remarks = models.TextField(
        max_length=300, verbose_name='备注', blank=True, null=True)


    class Meta:
        verbose_name = '资产请购表'
        verbose_name_plural = verbose_name


def __str__(self):
    return self.name


class user(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

    #姓名
    name = models.CharField(max_length=128,unique=True)
    #用户名
    username = models.CharField(max_length=32,unique=True,default="")
    #密码
    password = models.CharField(max_length=256)
    #性别
    sex = models.CharField(max_length=32,choices=gender,default='男')
    #创建时间
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户表'
        verbose_name_plural = verbose_name