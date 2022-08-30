from django.shortcuts import render
import random

def arrayValues():
    ary = []
    for i in range(0, 150):
        n = random.randint(100, 600)
        ary.append(n)
    return ary


def index(request):
    global arr
    arr = arrayValues()
    return render(request, "index.html", {'arr': arr})
