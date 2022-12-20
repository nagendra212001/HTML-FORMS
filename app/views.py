from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    
    if request.method=='POST':
        #tn=request.POST['topic']
        tn=request.POST.get('topic')
        T=topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inseted successfully')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=topic.objects.all()
    
    d={'topics':topics}

    if request.method=='POST':
        topics=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=topic.objects.get_or_create(topic_name=topics)[0]
        T.save()
        W=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    topics=topic.objects.all()
    
    

    webpages=webpage.objects.all()
    d={'topics':topics,'webpages':webpages}

    if request.method=='POST':
        topics=request.POST['topic']
        webpages=request.POST['webpage']
        ur=request.POST['ur']
        dt=request.POST['dt']
        T=topic.objects.get_or_create(topic_name=topics)[0]
        T.save()
        W=webpage.objects.get_or_create(topic_name=T,name=webpages,url=ur)[0]
        W.save()
        a=access_record.objects.get_or_create(name=W,date=dt)[0]
        a.save()

        return HttpResponse('access_record is inserted successfully')
    return render(request,'insert_accessrecord.html',d)


def select_topic(request):
    topics=topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=webpage.objects.none()
        for i in tn:
            webpages=webpages|webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,"display_webpages.html",data)
    return render(request,"select_topic.html",d)

def checkbox(request):
    topics=topic.objects.all()
    d={'topics':topics}

    return render(request,'checkbox.html',d)

def display_web(request):
    lwo=webpage.objects.all()
    webpage.objects.filter(topic_name="cricket").update(name="MSD")
    lwo=webpage.objects.filter(topic_name='cricket')
    lwo=webpage.objects.all()
    d={'lwo':lwo}
    
    return render(request,"display_web.html",d)

