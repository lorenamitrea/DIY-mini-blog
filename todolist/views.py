from django.shortcuts import render
from todolist.models import Board, Task
from django.contrib.auth.decorators import login_required
from .forms import NewBoard, NewTask
from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


@login_required
def add_board(request):

    if request.user.is_authenticated:
        username = request.user.id
        boards = Board.objects.filter(username_id=username)
        if request.method == 'POST':
            if 'board' in str(request.POST):
                board_form = NewBoard(request.POST, prefix='board')
                if board_form.is_valid():
                    user = request.user
                    board = Board(name=board_form.cleaned_data['board_name'], username=user)
                    board.save()
                    return HttpResponseRedirect(reverse('todo'))
    return HttpResponseNotFound


@login_required
def todo(request):

    todo_dict = {}
    username = None
    board_form = None
    task_form_set = None
    if request.user.is_authenticated:
        username = request.user.id
        boards = Board.objects.filter(username_id=username)
        tasks = Task.objects.filter(board_id__in=boards)
        no_boards = Board.objects.filter(username_id=username).count()
        TaskFormSet = formset_factory(NewTask, extra=no_boards)
        board_form = NewBoard(prefix='board')
        task_form_set = TaskFormSet(prefix='task')
        for board in boards:
            todo_dict[board.name] = []
        for task in tasks:
            task_dict = {'id': task.id, 'action': task.name, 'done': task.status, 'details': task.details}
            todo_dict[task.board.name].append(task_dict)
    context = {
        'todo_dict': todo_dict,
        'board_form': board_form,
        'task_form_set': task_form_set
    }
    print(context)
    return render(request, 'todo.html', context=context)
