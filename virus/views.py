from django.shortcuts import render
from .models import virus_record, mail_info, asset
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.

# 获取病毒处理记录所有数据,展示info.html


def info(request):
    info = virus_record.objects.all().order_by('pcip')
    return render(request, 'info.html', {'info': info})

# 获取资产请购所有数据,展示assetinfo.html


def assetinfo(request):
    assetinfo = asset.objects.all().order_by('Requisition_date')
    return render(request, 'assetinfo.html', {'assetinfo': assetinfo})

# 查询Info表数据


def searchinfo(request):
    if request.method == 'POST':
        temp_ip = request.POST['pcip']
        search_info = virus_record.objects.filter(pcip=temp_ip)
        return render(request, 'search.html', {'searchinfo': search_info})

# 查询asset表数据


def searchassetinfo(request):
    if request.method == 'POST':
        temp_Requisitioner= request.POST['Requisitioner']
        search_assetinfo = asset.objects.filter(Requisitioner=temp_Requisitioner)
        return render(request, 'searchasset.html', {'searchassetinfo': search_assetinfo})

# 新增数据


def addinfo(request):
    if request.method == 'POST':
        temp_pcip = request.POST['pcip']
        temp_username = request.POST['username']
        temp_number = request.POST['number']
        temp_pcname = request.POST['pcname']
        temp_status = request.POST['status']
        temp_handle_time = request.POST['handle_time']
        temp_remarks = request.POST['remarks']
        temp_virus_type = request.POST['virus_type']
        temp_pcmac = request.POST['pcmac']

    temp_info = virus_record(
        pcip=temp_pcip,
        username=temp_username,
        number=temp_number,
        pcname=temp_pcname,
        status=temp_status,
        handle_time=temp_handle_time,
        remarks=temp_remarks,
        virus_type=temp_virus_type,
        pcmac=temp_pcmac,
    )
    temp_info.save()
    # 重定向
    return HttpResponseRedirect(reverse('info'))


# 删除数据


def deleteinfo(request, info_id):
    infoID = info_id
    virus_record.objects.filter(id=infoID).delete()
    return HttpResponseRedirect(reverse('info'))

# 删除物资请购数据


def delassetinfo(request, assetinfo_id):
    assetinfoID = assetinfo_id
    asset.objects.filter(id=assetinfoID).delete()
    return HttpResponseRedirect(reverse('showasset'))


# 发送告警邮件


def sendmail(request):
    if request.method == 'POST':
        subject = '笔记本中毒告警'
        text_content = '你好，你的笔记本中了挖矿病毒，需要立即到C栋1.5楼信息部处理！'
        from_email = 'yiwan.jiang@leadchina.cn'
        recipient_list = request.POST['mailaddress']
        send_mail(subject, text_content, from_email, [
                  recipient_list], fail_silently=False)
        return HttpResponse('邮件发送成功')
    else:
        return HttpResponse('邮件发送失败')

# 展示sendmail.html


def showsendmail(request):
    return render(request, 'mail.html')


# 展示新增资产请购数据网页


def showaddasset(request):
    return render(request, 'addasset.html')

# 展示查询信息表


def showsearch(request):
    return render(request, 'search.html')

# 展示查询物资请购信息页面


def showqueryasset(request):
    return render(request, 'searchasset.html')

# showbase


def showbase(request):
    return render(request, 'base.html')

# 展示首页


def showstart(request):
    return render(request, 'start.html')


class IndexView(TemplateView):
    template_name = 'start.html'

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)



# 新增资产请购数据


def addasset(request):
    if request.method == 'POST':
        temp_Finish = request.POST['Finish']
        temp_Source = request.POST['Source']
        temp_Document_No = request.POST['Document_No']
        temp_Order_No = request.POST['Order_No']
        temp_Requisition_date = request.POST['Requisition_date']
        temp_Materials = request.POST['Materials']
        temp_Department = request.POST['Department']
        temp_Requisitioner = request.POST['Requisitioner']
        temp_Requisition_Num = request.POST['Requisition_Num']
        temp_Requisition_purpose = request.POST['Requisition_purpose']
        temp_Order_Time = request.POST['Order_Time']
        temp_Purchaser = request.POST['Purchaser']
        temp_Reason = request.POST['Reason']
        temp_Supplier = request.POST['Supplier']
        temp_Arrival_time1 = request.POST['Arrival_time1']
        temp_Arrival_time2 = request.POST['Arrival_time2']
        temp_Actual_time1 = request.POST['Actual_time1']
        temp_Actual_Num1 = request.POST['Actual_Num1']
        temp_Actual_time2 = request.POST['Actual_time2']
        temp_Actual_Num2 = request.POST['Actual_Num2']
        temp_Actual_time3 = request.POST['Actual_time3']
        temp_Actual_Num3 = request.POST['Actual_Num3']
        temp_Unarrival_Num = request.POST['Unarrival_Num']
        temp_Overdue = request.POST['Overdue']
        temp_Overdue_time = request.POST['Overdue_time']
        temp_Remarks = request.POST['Remarks']

    temp_asset = asset(
        Finish=temp_Finish,
        Source=temp_Source,
        Document_No=temp_Document_No,
        Order_No=temp_Order_No,
        Requisition_date=temp_Requisition_date,
        Materials=temp_Materials,
        Department=temp_Department,
        Requisitioner=temp_Requisitioner,
        Requisition_Num=temp_Requisition_Num,
        Requisition_purpose=temp_Requisition_purpose,
        Order_Time=temp_Order_Time,
        Purchaser=temp_Purchaser,
        Reason=temp_Reason,
        Supplier=temp_Supplier,
        Arrival_time1=temp_Arrival_time1,
        Arrival_time2=temp_Arrival_time2,
        Actual_time1=temp_Actual_time1,
        Actual_Num1=temp_Actual_Num1,
        Actual_time2=temp_Actual_time2,
        Actual_Num2=temp_Actual_Num2,
        Actual_time3=temp_Actual_time3,
        Actual_Num3=temp_Actual_Num3,
        Unarrival_Num=temp_Unarrival_Num,
        Overdue=temp_Overdue,
        Overdue_time=temp_Overdue_time,
        Remarks=temp_Remarks,

    )
    temp_asset.save()
    # 重定向
    return HttpResponseRedirect(reverse('showaddasset'))