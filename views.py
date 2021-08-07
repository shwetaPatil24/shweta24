from django.shortcuts import render, redirect  
from student.forms import EmployeeForm  
from student.models import Employee  
# Create your views here.  
def stu(request):  
    if request.method == "POST":  
        form = studentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = studentForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    students = student.objects.all()  
    return render(request,"show.html",{'students':students})  
def insert(request, rollnumber):  
    student = student.objects.get(id=id)  
    return render(request,'insert.html', {'student':student})  
def update(request, id):  
    student = student.objects.get(id=id)  
    form = studentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'insert.html', {'student': student})  
def delete(request, id):  
    student = student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  