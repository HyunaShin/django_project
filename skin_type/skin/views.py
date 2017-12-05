from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from skin.models import Comment
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.



def userName(request):
    try:

        email = request.session['login_id']

    except KeyError as e:

        return render(request, 'Q0.html')



    all_username = None

    if request.method == 'POST':

        username = User_names(

            user_name=request.POST["user_name"]

        )

        username.save()

        result = { "user_name": request.POST["user_name"]}



        return render(request, 'Q1html', result)

    else:

        all_username = Username.objects.all()

        result = {"user_name": all_username}

        return render(request, 'Q1.html', result)

def question_1(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q1.html')

def question_2(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q2.html')

def question_3(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q3.html')

def question_4(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q4.html')

def question_5(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q5.html')

def question_6(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q6.html')

def question_7(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q7.html')

def question_8(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q8.html')

def question_9(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q9.html')

def question_10(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q10.html')

def question_11(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q11.html')

def question_12(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q12.html')

def question_13(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q13.html')

def question_14(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q14.html')

def question_15(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q15.html')

def question_16(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q16.html')

def question_17(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q17.html')

def question_18(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q18.html')

def question_19(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q19.html')

def question_20(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q20.html')

def question_21(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q21.html')

def question_22(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q22.html')

def question_23(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q23.html')

def question_24(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q24.html')

def question_25(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q25.html')

def question_26(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q26.html')

def question_27(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q27.html')

def question_28(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q28.html')

def question_29(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q29.html')

def question_30(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'q30.html')

def comment_detail(request, comment_contents):
    comment = Comment.objects.get(comment_contents=comment_contents)
    email = request.session["login_id"]
    return render(request, 'q30.html', {"comment": comment_contents, "login_id": email})

def post_comment(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'q30.html')
    comment = request.POST.get("comment")
    email = request.session['login_id']
    user = User.objects.get(username=email)
    comment = Comment(comment_contents=comment, user=user)
    print(comment)
    comment.save()
    comments = Comment.objects.all()

    return render(request, "q30.html", {"comments": comments})




#
# def results(request):
#     response = "%s님의 피부타입은"
#     return HttpResponse(response % username, 'Page_32.html')
#
# def post_comment(request):
#     if request.method == "POST":
#         id = request.POST["username"]
#         comment = request.POST["comment"]
#
#     email = request.session["login_id"]
#     return render(request, 'comment_detail.html', {"login_id": email})
