from django.shortcuts import render
from todolist.models import Board, Task
from django.contrib.auth.decorators import login_required


@login_required
def todo(request):
    todo_dict = {}
    username = None
    if request.user.is_authenticated:
        username = request.user.id
        boards = Board.objects.filter(username_id=username)
        tasks = Task.objects.filter(board_id__in=boards)
        for board in boards:
            todo_dict[board.name] = []
        for task in tasks:
            task_dict = {'id': task.id, 'action': task.name, 'done': task.status, 'details': task.details}
            todo_dict[task.board.name].append(task_dict)
    context = {
        'todo_dict': todo_dict
    }
    print(context)
    return render(request, 'todo.html', context=context)
