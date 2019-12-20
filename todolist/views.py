from django.shortcuts import render


def todo(request):
    context = {}
    return render(request, 'todo.html', context=context)
