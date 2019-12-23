from django.shortcuts import render
from todolist.models import Board, Task
from django.contrib.auth.decorators import login_required
from .forms import NewBoard


@login_required
def todo(request):

    todo_dict = {}
    username = None
    form = None
    if request.user.is_authenticated:
        username = request.user.id
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NewBoard(request.POST)

            # check whether it's valid:
            if form.is_valid():
                user = request.user
                board = Board(name=form.cleaned_data['board_name'], username=user)
                board.save()
        else:
            form = NewBoard()
        boards = Board.objects.filter(username_id=username)
        tasks = Task.objects.filter(board_id__in=boards)
        for board in boards:
            todo_dict[board.name] = []
        for task in tasks:
            task_dict = {'id': task.id, 'action': task.name, 'done': task.status, 'details': task.details}
            todo_dict[task.board.name].append(task_dict)
    context = {
        'todo_dict': todo_dict,
        'form': form
    }
    print(context)
    return render(request, 'todo.html', context=context)
