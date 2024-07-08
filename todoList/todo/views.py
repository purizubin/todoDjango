from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/index.html", {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Todo.objects.create(title=title, description=description)

        return redirect('todo_list')
    return render(request, 'todo/index.html')

def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/delete_todo.html', {'todo': todo})

