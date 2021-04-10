from django.shortcuts import render,redirect
from .models import *
from .forms import Taksform

# Create your views here.
def index(request):
    task=Task.objects.all()
    form=Taksform()

    if request.method=='POST':
        form=Taksform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'value':task,'form':form}
    return render(request,'TodoApp/list.html',context)

def update_taks(request,pk):
    task = Task.objects.get(id=pk)
    form= Taksform(instance=task)
    if request.method== 'POST':
        form=Taksform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'TodoApp/update.html',context)

def delete_item(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'TodoApp/delete_task.html',context)
