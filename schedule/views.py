from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from  .models import getclass,addstudent,getteacher,Classes,studentsform, ClassTeachers, Students,askteacher,Teachers,askclass
from django.views import View
from django.views.generic import ListView

class SchoolSchedules(View):
    def index(request):
        return render(request,"schedule/index.html")

    def askpage(request):
        form = studentsform()
        return render(request, 'schedule/askpage.html',{"form":form})

    def studentdetails(request):
        if request.method == "POST":
            form = studentsform(request.POST)
            if form.is_valid():
                adm = form.cleaned_data['Adm_number']
                try:
                    student=Students.objects.filter(adm_number__icontains=adm)
                    return render(request,"schedule/studentdetails.html",{"student":student})
                except:
                    return HttpResponseRedirect(reverse('index'))

    def addstudentdetails(request):
        form = addstudent()
        return render(request,"schedule/addstudent.html",{"form":form})

    def addstudent(request):
        if request.method == "POST":
            form = addstudent(request.POST)
            if form.is_valid():
                adm_number = form.cleaned_data['adm_number']
                surname=form.cleaned_data['Surname']
                othernames=form.cleaned_data['othernames']
                presentclass_v=form.cleaned_data['presentclass']
                DOB=form.cleaned_data['DOB']
                cl_arm=form.cleaned_data['cl_arm']
                try:
                    presentclass=Classes.objects.get(level__iexact=presentclass_v,arm__iexact=cl_arm)
                    student=Students.objects.create(adm_number=
                    adm_number,surname  = surname,othernames=othernames,
                    presentclass=presentclass, DOB=DOB,cl_teacher=presentclass)
                    student.save()
                    return HttpResponse("<h1>Student added successfully!</h1>")
                except:
                    return HttpResponse("<h1>Student not added!</h1>")

    def rmvstudent(request,pk):
        try:
            st=get_object_or_404(Students,pk=pk)
            st.delete()
            return HttpResponse('''<h1>Student %s deleted!</h1>'''%(st.surname))
        except:
            return HttpResponse('''<h1>Student not found!</h1>''')

    def aboutus(request):
            return render(request,'schedule/aboutus.html')

    def askteacher(request):
        form = askteacher()
        return render(request, 'schedule/askteacher.html',{"form":form})

    def askclass(request):
        form = askclass()
        return render(request, 'schedule/askclass.html',{"form":form})
    def getclass(request):
        form = getclass()
        return render(request, 'schedule/addclass.html',{"form":form})

    def addclass(request):
        if request.method == "POST":
            form = getclass(request.POST)
            if form.is_valid():
                level = form.cleaned_data['level']
                arm = form.cleaned_data['arm']
                no_of_students = form.cleaned_data['no_of_students']
                classteacher = form.cleaned_data['classteacher']
                try:
                    c=Classes.objects.get(level__iexact=level,arm__iexact=arm)
                    tch = Teachers.objects.get(name=classteacher)
                    clteacher = ClassTeachers.objects.create(name=tch)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    tch = Teachers.objects.get(name=classteacher)
                    clteacher = ClassTeachers.objects.create(name=tch)
                    clteacher.save()
                    nclass = Classes.objects.create(level = level,arm  = arm, no_of_students = no_of_students,
                    classteacher = clteacher)
                    nclass.save()
                    return HttpResponse('''<h1>Class added successfully!</h1>''')
            #return HttpResponseRedirect(reverse('index'))
    def rmvclass(request,pk):
        cl=Classes.objects.get(pk=pk)
        cl.delete()
        return HttpResponse('''<h1>Class deleted! <a href="{%url 'index'%}">Home</a></h1>''')
#View to see class details
    def classdetails(request):
        import pandas as pd
        if request.method == "POST":
            form = askclass(request.POST)
            if form.is_valid():
                level = form.cleaned_data['level']
                arm = form.cleaned_data['arm']
                try:
                    presentclass= Classes.objects.get(level__iexact=level, arm__iexact=arm)
                    studentsinclass=Students.objects.filter(presentclass=presentclass)
                    student_df = pd.DataFrame(studentsinclass.values())
                    student_df = student_df[['surname','othernames','adm_number','DOB']]
                    student_df.columns = ['Surname','Othernames','Adm_No','DOB']
                    context = {"pclass":presentclass,'s':studentsinclass,'df':student_df.to_html()}
                    return render(request,"schedule/classdetails.html",context)
                except:
                    return HttpResponseRedirect(reverse('index'))
#View to get data of new teacher
    def getteacher(request):
        form = getteacher()
        return render(request, 'schedule/addteacher.html',{"form":form})
    #To add the teacher to database
    def addteacher(request):
        if request.method == "POST":
            form = getteacher(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                title =form.cleaned_data['title']
                subject =form.cleaned_data['subject']
                admin_role=form.cleaned_data['admin_role']
                staffID=form.cleaned_data['staffID']
                try:
                    teacher = Teachers.objects.get(name__icontains=name)
                    return HttpResponseRedirect(reverse("index"))
                except:
                        teacher=Teachers.objects.create(name = name,title  = title,subject = subject,admin_role = admin_role,staffID=staffID)
                        teacher.save()
                        return HttpResponse("<h1>Teacher added successfully!</h1>")

#To view list of existing Classteachers
class ClassTeachersList(ListView):
    model = ClassTeachers
    context_object_name='classteacherlist'
    queryset = ClassTeachers.objects.all()
    template_name='schedule/classteacherlist.html'

#To check teachers' details and remove any teacher from the database or as a classteacher
class teacher(View):
    def teacherdetails(request):
        if request.method == "POST":
            form = askteacher(request.POST)
            if form.is_valid():
                try:
                    name = form.cleaned_data['teacher_name']
                    teacher = Teachers.objects.filter(name__icontains=name)
                    return render(request,"schedule/teacherdetails.html",{"teacher":teacher})
                except:
                    return HttpResponseRedirect(reverse('index'))
    #To remove a teacher from database
    def rmvteacher(request,pk):
        t=get_object_or_404(Teachers,pk=pk)
        t.delete()
        return HttpResponse('''<h1>Teacher %s deleted!</h1>'''%(t.name))
        #To remove teacher as a classteacher
    def rmvclassteacher(request,pk):
        try:
            ct=get_object_or_404(ClassTeachers,pk=pk)
            ct.delete()
            return HttpResponseRedirect(reverse('index'))
        except:
            return HttpResponse('''Classteacher not existing!''')
