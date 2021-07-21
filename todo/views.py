from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
    {'all_items': all_todo_items})

def addTodo(request):
    """
    create new todo all_items
    save it
    redirect the browser to where it came from '/todo/' 
    """
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    
def deleteTodo(request, todo_id):
    """
    find item to delete
    delete it
    redirect the browser to where it came from '/todo/' 
    """
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
    

