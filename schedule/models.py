from django.db import models
# Create your models here.
from django.db import models
# Create your models here.
from django.db import models
from django import forms

class studentsform(forms.Form):
    Adm_number = forms.CharField(max_length=4,label="Student's Admission Number")

class askteacher(forms.Form):
    teacher_name = forms.CharField(label="Teacher's Name")

class getteacher(forms.Form):
    name = forms.CharField(label="Teacher's name")
    title = forms.CharField(label="Title")
    subject= forms.CharField(label="Subject")
    admin_role=forms.CharField(label="Teacher's admin_role")
    staffID=forms.CharField(label='Staff Id')
class Teachers(models.Model):
    class Meta:
        verbose_name_plural="Teachers"
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=4)
    subject = models.CharField(max_length=64)
    admin_role = models.CharField(max_length=64)
    staffID = models.CharField(max_length=11)
    def __str__(self):
        return "%s"%(self.name)

class ClassTeachers(models.Model):
    class Meta:
        verbose_name_plural="ClassTeachers"
    name = models.OneToOneField(Teachers,on_delete=models.CASCADE)
    def __str__(self):
        return "%s"%(self.name)
class askclass(forms.Form):
    level = forms.CharField(label="Class")
    arm = forms.CharField(label="arm", max_length=1)
class getclass(forms.Form):
    ct1=ClassTeachers.objects.all()
    ct=Teachers.objects.exclude(name__in=[n for n in ct1])
    ce = (('','Choose'),)
    for i in range(len(ct)):
        ce+=((ct[i],ct[i]),)
    level = forms.CharField(label="Class")
    arm = forms.CharField(label="arm", max_length=1)
    no_of_students=forms.IntegerField()
    classteacher=forms.ChoiceField(label="classteacher",choices=ce)

ce=(('','Choose'),("JSS1",'JSS1'),("JSS2",'JSS2'),("JSS3",'JSS3'),("SS1",'SS1'),("SS2",'SS2'),("SS3",'SS3'))
class addstudent(forms.Form):
    adm_number = forms.CharField(max_length=4,label="Student's Adm_number")
    Surname = forms.CharField(label="Student's Surname")
    othernames= forms.CharField(label="Student's othernames")
    presentclass=forms.ChoiceField(label="Student's presentclass",choices=ce)
    cl_arm=forms.CharField(label="Student's class arm")
    DOB = forms.DateField(label="Student's Birth date", widget=forms.DateInput(attrs={'type':'date'}))

# Create your models here.
class Classes(models.Model):
    class Meta:
        verbose_name_plural="Classes"
    level=models.CharField(max_length=4)
    arm = models.CharField(max_length=1)
    no_of_students=models.IntegerField()
    classteacher=models.OneToOneField(ClassTeachers, null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return " %s %s "%(self.level,self.arm)

class Students(models.Model):
    class Meta:
        verbose_name_plural="Students"
    adm_number=models.CharField(max_length=4, unique=True)
    surname=models.CharField(max_length=20)
    othernames=models.CharField(max_length=40)
    presentclass=models.ForeignKey(Classes,on_delete=models.CASCADE,related_name="student")
    DOB=models.DateField()
    cl_teacher = models.ForeignKey(Classes,on_delete=models.DO_NOTHING, related_name='students')

    def __str__(self):
        return '%s %s '%(self.surname,
        self.othernames)
