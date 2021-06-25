from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

# function for add student 
def student_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            cl = form.cleaned_data['class_no']
            pw = form.cleaned_data['password']
            reg = Student(name=nm, email=em, class_no=cl ,password=pw,)   
            reg.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    context= {'form':form}
    return render(request, 'add_data.html',context)

# function for all student information
def student_info(request):
    all_info = Student.objects.all()
    context = {'all_info':all_info}
    return render(request, 'student_info.html',context)

# function for edit student data
def edit_data(request,id):
    if request.method == 'POST':
        ed = Student.objects.get(pk=id)
        frm = StudentRegistration(request.POST, instance=ed)
        if frm.is_valid():
            frm.save()
            msg = "Updated Successfully"
            context ={'frm':frm,'msg':msg}
            return render(request,'student_update.html',context)
        
    else:
        ed = Student.objects.get(pk=id)
        frm = StudentRegistration(instance=ed)
    context ={'frm':frm}
    return render(request,'student_update.html',context)

# function for delete student data
def delete_info(request,id):
    Student.objects.get(pk=id).delete()
    return HttpResponseRedirect('/student_info/')
   
