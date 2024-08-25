from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import CreateTodoForm,UpdateTodoForm




# Create your views here.
def home(request):
    all=Todo.objects.all
    return render(request , 'home.html', {'todos': all})


def details(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo_id':todo})


def deletes(request,todo_id):

    todo_title=Todo.objects.get(id=todo_id)
   
    Todo.objects.get(id=todo_id).delete()

    msg = "Todo \'"+todo_title.title+"\' successfully deleted! :)"
    messages.success(request, msg ,'success')
    return redirect('home')


def create(request):

    if (request.method =="POST"):
        form=CreateTodoForm(request.POST)
        if form.is_valid() :
            cd=form.cleaned_data
            Todo.objects.create(title=cd['title'],body=cd['body'],created=cd['created'])
            msg='Todo \''+ cd['title']+ '\' Create Successfully'
            messages.success(request,msg,'success')
            return redirect('home')
    else:
        form=CreateTodoForm()

    return render(request,'create.html',{'form':form})




def updates(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    if (request.method=="POST"):
        form=UpdateTodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Update run successfully','success')
            return redirect('details',todo_id)
        
        
    else:
        form=UpdateTodoForm(instance=todo)    
         
    return render(request,'update.html',{'form':form})

















