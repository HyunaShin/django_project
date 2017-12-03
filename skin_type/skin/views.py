from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse
# Create your views here.
# from .models import Question


def input_user_name(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        request.session['user_name'] = user_name
        print(request.session['user_name'])
        return render(request,'final.html',{"user_name":user_name})

# def results(request, question_id):
#     response = "%s님의 피부타입은"
#     return HttpResponse(response % user_name)
#
def index(requsest):
    # question_list = question.objects
    return HttpResponse("Hello, CodeSquad")
def detail(request, question_id):
    response = "Dettail Page id : %s"
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "Question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vote Page: %s"% question_id)