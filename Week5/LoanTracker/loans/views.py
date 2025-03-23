from django.shortcuts import render


def listview(request):
    return render(request, 'loans/list.html', {})

def detailview(request):
    return render(request, 'loans/detail.html', {})

def createview(request):
    return render(request, 'loans/list.html', {})

def updateview(request):
    return render(request, 'loans/list.html', {})

