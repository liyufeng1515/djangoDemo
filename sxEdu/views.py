#coding=gbk

from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden 
from sxEdu.models import Student
from sxEdu.models import Opus 
import xlrd
import os

def index(request):
	return render(request,'main.html',{})

def login(request):
    studentId = request.POST.get('studentId') if request.POST.get('studentId') else request.COOKIES.get('studentId') 
    studentName = request.POST.get('studentName') if request.POST.get('studentName') else request.COOKIES.get('studentName') 
    if not studentId or not studentName:
        return HttpResponse('Required student id/name not found.')

    students = Student.objects.filter(studentId=studentId,studentName=studentName)
    if students:
        response = render(request,'main.html',{'studentId':studentId,'studentName':studentName})
        response.set_cookie('studentId',studentId)
        response.set_cookie('studentName',studentName)
        return response
    else:
        return HttpResponse('Not found which student name is %s and student id is %s' %(studentName,studentId))

def uploadOpus(request):
    studentId = request.COOKIES.get('studentId')
    page = None
    message = None
    if studentId:
        page = 'uploadOpus.html'
    else:
        page = 'index.html'
        message = 'Not found student that loginned.Please log back in.'
    return render(request,page,{'message':message})

class ImageForm(forms.Form):
    studentId = forms.CharField(required=False)
    imageTitle = forms.CharField(required=False)
    opusImage = forms.ImageField()

def doUpload(request):
    studentId = request.COOKIES.get('studentId') 
    page = None
    message = None
    if studentId:
        page = 'uploadSuccess.html'
        message = 'image upload success.'
        if request.method == "POST":
            form = ImageForm(request.POST,request.FILES)
            if form.is_valid():
                opus = Opus(studentId=studentId,imageTitle=form.cleaned_data['imageTitle'],opusImage=form.cleaned_data['opusImage'])
                opus.save()
    else:
        page = 'index.html'
        message = 'Not found student that loginned.Please log back in.'
    return render(request,page,{'message':message})
    
def myOpus(request):
    studentId = request.COOKIES.get('studentId')                                
    page = None
    message = None
    opusList = []
    if studentId:
        page = 'myOpus.html'
        opusList = Opus.objects.filter(studentId=studentId)  
    else:
        page = 'index.html'
        message = 'Not found student that loginned.Please log back in.'
    return render(request,page,{'message':message,'opusList':opusList})

def othersOpus(request):
    if request.GET.get('studentId'):
        opusList = Opus.objects.filter(studentId=request.GET.get('studentId'))
        return render(request,'othersOpus.html',{'opusList':opusList,'studentId':request.GET.get('studentId')})
    return render(request,'othersOpus.html',{})

def getStudentTranscript(request):
    studentId = request.COOKIES.get('studentId')
    page = None
    message = None
    transcriptList = []
    if studentId:
        page = 'studentTranscript.html'
        studentIdIndex = None
        studentIdTitle = "学号".decode('utf-8')
        workBook = xlrd.open_workbook(os.path.join(os.path.dirname(__file__),'studentTranscript.xls'),'utf-8')
        sheet = workBook.sheets()[0]
        titleRow = sheet.row_values(0)
        transcriptList.append(titleRow)
        if studentIdTitle in titleRow:
            studentIdIndex = titleRow.index(studentIdTitle)
            for i in range(sheet.nrows):
                value = sheet.cell_value(i,studentIdIndex)
                if sheet.cell_type(i,studentIdIndex)==2:
                    value = str(int(value))
                if value == request.COOKIES.get('studentId'):
                    rowValues = sheet.row_values(i)
                    transcriptList.append(rowValues)    
        else:
            message = 'Not found '+studentIdTitle+' in first row.'
    else:
        page = 'index.html'
        message = 'Not found student that loginned.Please log back in.'
    return render(request,page,{'message':message,'transcriptList':transcriptList})


