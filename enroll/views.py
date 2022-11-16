from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import StudentRegistration
from .models import User
# this function will add new item and show new item
def add_show(request):#if data comes with post request(if you want to save all the data then use this method otherwise given.)
    if request.method =='POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
        fm.save() #if u want to show blank form after clicking on add button then add fm=studentregistration()after this line
    else: #if it comes with get request
     fm = StudentRegistration()
    stud = User.objects.all()  #this shown data in side table
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#this function will update/edit
def update_data(request,id):
 if request.method =='POST':
   pi = User.objects.get(pk=id)
   fm = StudentRegistration(request.POST,instance=pi)     #(instance = pi used for import data in updated  form)
   if fm.is_valid():
    fm.save()
    return redirect('addandshow')
 else:
    pi=User.objects.get(pk=id)
    fm=StudentRegistration(instance=pi)
 return render(request,'enroll/updatestudent.html',{'form':fm})



#this function will delete
def delete_data(request,id):
    if request.method=='POST':
      pi=User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')

#this method is used to save single column data(make object of models class)
#if fm.is_valid():
 # nm=fm.cleaned_data['name']
  #em=fm.cleaned_data['email']
  #reg=User(name=nm,email=em)
  #reg.save()