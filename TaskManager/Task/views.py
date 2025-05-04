from django.shortcuts import render,redirect,get_object_or_404
from Task.models import Register,AddTask,Page
from django.contrib import messages



# Create your views here.

def page(request):
    p = Page.objects.all()
    return render(request,'index.html',{'p':p})

from django.shortcuts import render, redirect
from .models import Register

def register(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            message = "Passwords do not match"
            return render(request, 'registration.html', {'message': message})

        if Register.objects.filter(username=username).exists():
            message = "Username already taken"
            return render(request, 'registration.html', {'message': message})

        data = Register(username=username, password=password, confirm_password=confirm_password)
        data.save()
        message = "You are successfully registered"
        return redirect('login')

    return render(request, 'registration.html', {'message': message})



def login(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Register.objects.get(username=username, password=password)
            request.session['username'] = user.username
            message = "Login successful!"
            return redirect('addtask')
        except Register.DoesNotExist:
            message = "Invalid username or password"
            return render(request, 'login.html', {'message': message})

    return render(request, 'login.html', {'message': message})

def addtask(request):
    message = ''
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        if title:  
           data = AddTask(title=title,description=description,deadline=deadline)
           data.save()
           return redirect('tasklist')
        else:
            message = "title cannot be empty"
    
    return render(request,'addtask.html',{'messages':message})


def tasklist(request):
    tasks = AddTask.objects.all().order_by('-deadline')
    return render(request,'tasklist.html',{'tasks':tasks})

def complete_task(request,task_id):
     task = get_object_or_404(AddTask,id=task_id)
     task.save()
     messages.success(request, 'Task mark as completed!')
     return redirect('tasklist')


def delete_task(request,task_id):
     task = get_object_or_404(AddTask,id=task_id)
     task.delete()
     messages.success(request, 'Successfully deleted')
     return redirect('tasklist')
   
