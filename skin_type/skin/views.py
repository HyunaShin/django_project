from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse
# Create your views here.



def userName(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Q0.html')

    all_username = None
    if request.method == 'POST':
        username = Username(
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

def post_comment(request):
    if request.method == "POST":

        comment = request.POST["comment"]
        user = request.session["user_name"]
        comment = Comment.objects.create(comment_contents=comment)
        print(comment.comment_contents)
        comment.save()

        return redirect("/bookmark_detail/" + id)
















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
#         comment = Comment.objects.create(comment_contents=comment,user=user,bookmark=bookmark)
#         print(comment.comment_contents)
#         comment.save()
