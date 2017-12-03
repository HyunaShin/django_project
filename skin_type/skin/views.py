from django.shortcuts import render
from django.http import HttpResponse


def new_time(request):
    return render(request,"start_page.html")
# Create your views here.
def input_user_name(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        request.session['user_name'] = user_name
        print(request.session['user_name'])
        return render(request,'final.html',{"user_name":user_name})
