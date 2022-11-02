from django.shortcuts import render, redirect
from todo.models import Task


# Create your views here.

def add(request):
    if (request.method == 'POST'):
        heading_ = request.POST['heading']
        details_ = request.POST['details']
        date_ = request.POST['date']
        #print(heading)
        #print(details)
        #print(date)

        insert_data = Task.objects.create(heading = heading_, details = details_, date = date_)
        insert_data.save()
        return redirect("/")
    return render (request,'todo/add.html')

def home(request):
    #display = Task.objects.all()
    display = Task.objects.filter(is_deleted = 'n')
    data = {'display':display}
    return render(request, 'todo/home.html', context = data)

def delete(request, tid):
    delete_data = Task.objects.filter(id = tid)
    #delete_data.delete()
    delete_data.update(is_deleted = 'y')
    return redirect("/")

def update(request, tid):
    if (request.method == 'POST'):
        heading_ = request.POST['heading']
        details_ = request.POST['details']
        date_ = request.POST['date']
        edit_data = Task.objects.filter(id = tid)
        edit_data.update(heading = heading_, details = details_, date = date_ )
        return redirect("/")
    else:
        update = Task.objects.get(id = tid)
        data = {'update':update}
        return render(request, 'todo/update.html', data)
