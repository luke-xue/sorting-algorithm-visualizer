from django.shortcuts import render, HttpResponse
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

def insertion_sort(request):
    animation = []
    for i in range(1,len(arr)):
        temp = i
        while temp > 0 and arr[temp] < arr[temp-1]:
            animation.append([temp-1, arr[temp-1], temp, arr[temp]])
            arr[temp], arr[temp-1] = arr[temp-1], arr[temp]
            temp -= 1
    return HttpResponse([animation])