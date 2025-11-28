from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    """Display all todos."""
    all_todos = Todo.objects.all()
    
    # Calculate counts
    total_count = all_todos.count()
    resolved_count = all_todos.filter(is_resolved=True).count()
    pending_count = all_todos.filter(is_resolved=False).count()
    
    # Calculate overdue count (todos that are overdue and not resolved)
    overdue_count = len([todo for todo in all_todos if todo.is_overdue()])
    
    # Filter by status if requested
    filter_status = request.GET.get('filter', 'all')
    view_mode = request.GET.get('view', 'grid')  # grid or list
    
    todos = all_todos
    if filter_status == 'pending':
        todos = todos.filter(is_resolved=False)
    elif filter_status == 'resolved':
        todos = todos.filter(is_resolved=True)
    elif filter_status == 'overdue':
        # For overdue, we need to filter in Python since is_overdue() is a model method
        overdue_todos = [todo for todo in all_todos if todo.is_overdue()]
        todo_ids = [todo.id for todo in overdue_todos]
        todos = all_todos.filter(id__in=todo_ids) if todo_ids else all_todos.none()
    
    context = {
        'todos': todos,
        'filter_status': filter_status,
        'view_mode': view_mode,
        'total_count': total_count,
        'resolved_count': resolved_count,
        'pending_count': pending_count,
        'overdue_count': overdue_count,
    }
    return render(request, 'todos/todo_list.html', context)


def todo_create(request):
    """Create a new todo."""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    return render(request, 'todos/todo_form.html', {
        'form': form,
        'title': 'Create Todo'
    })


def todo_edit(request, pk):
    """Edit an existing todo."""
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'todos/todo_form.html', {
        'form': form,
        'todo': todo,
        'title': 'Edit Todo'
    })


def todo_delete(request, pk):
    """Delete a todo."""
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted successfully!')
        return redirect('todo_list')
    
    return render(request, 'todos/todo_confirm_delete.html', {
        'todo': todo
    })


def todo_toggle_resolved(request, pk):
    """Toggle the resolved status of a todo."""
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    
    status = 'resolved' if todo.is_resolved else 'unresolved'
    messages.success(request, f'Todo marked as {status}!')
    
    return redirect('todo_list')

