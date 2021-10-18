from django.shortcuts import render,redirect
from task.models import student


from django.core.paginator import Paginator


from task.forms import studentForm
# Create your views here.


def index(request):
    items=2
    p=Paginator(student.objects.all(),items)
    page=request.GET.get('page')
    form=p.get_page(page)
    pages=items*(form.number-1)
    return render(request,'task/index.html',{'form':form,'a':pages})


def add_student(request):
    form=studentForm()
    if request.method=="POST":
        form=studentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/")
    else:
        print("invalid")
    return render(request,'task/new_student.html',{'form':form})


def edit(request,id):

    if request.method=='POST':
        data=student.objects.get(pk=id)

        form=studentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/")
        else:
            return render(request,"task/new_student.html",{'form':form})
    else:
        data=student.objects.get(pk=id)
        form=studentForm(instance=data)
        print(data.phone)
    return render(request,"task/new_student.html",{'form':form})


def details(request,id):
    form=student.objects.get(pk=id)
    return render(request,"task/details.html",{'form':form})
