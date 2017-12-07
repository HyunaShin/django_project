from django.shortcuts import render, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from .models import Comment
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

# def userName(request):
#
#     return(request,'q0.html')
# def is_logged(request):
#     all_username = None
#     if request.method == 'POST':
#         # username = User_names(
#         user_name=request.POST["user_name"]
#         print(user_name)
#     return render(request,'q1.html')
#         # )
#
#         username.save()
#
#         result = { "user_name": request.POST["user_name"]}
#
#
#
#         return render(request, 'Q0.html', result)
#
#     else:
#
#         all_username = Username.objects.all()
#
#         result = {"user_name": all_username}
#
#         return render(request, 'Q0.html', result)

def question_1(request):
    # try:
    #     email = request.session['login_id']
    # except KeyError as e:
        return render(request, 'Q1.html')

def question_2(request):

        return render(request, 'Q2.html')

def question_3(request):

        return render(request, 'Q3.html')

def question_4(request):

        return render(request, 'Q4.html')

def question_5(request):

        return render(request, 'Q5.html')

def question_6(request):

        return render(request, 'Q6.html')

def question_7(request):

        return render(request, 'Q7.html')

def question_8(request):

        return render(request, 'Q8.html')

def question_9(request):

        return render(request, 'Q9.html')

def question_10(request):

        return render(request, 'Q10.html')

def question_11(request):

        return render(request, 'Q11.html')

def question_12(request):

        return render(request, 'Q12.html')

def question_13(request):

        return render(request, 'Q13.html')

def question_14(request):

        return render(request, 'Q14.html')

def question_15(request):

        return render(request, 'Q15.html')

def question_16(request):

        return render(request, 'Q16.html')

def question_17(request):

        return render(request, 'Q17.html')

def question_18(request):

        return render(request, 'Q18.html')

def question_19(request):

        return render(request, 'Q19.html')

def question_20(request):

        return render(request, 'Q20.html')

def question_21(request):

        return render(request, 'Q21.html')

def question_22(request):

        return render(request, 'Q22.html')

def question_23(request):

        return render(request, 'Q23.html')

def question_24(request):

        return render(request, 'Q24.html')

def question_25(request):

        return render(request, 'Q25.html')

def question_26(request):

        return render(request, 'Q26.html')

def comment_detail_26(request, comment_contents):
    comment = Comment.objects.get(comment_contents=comment_contents)

    return render(request, 'q26.html', {"comment": comment })

def post_comment_26(request):
    try:
        comment = request.POST["comment"]

    except KeyError as e:
        return render(request, 'q26.html')

    else:
        comment = Comment(comment_contents=comment)
        comment.save()

        return HttpResponseRedirect(reverse('question_1'))

def question_27(request):

        return render(request, 'Q27.html')

def comment_detail_27(request, comment_contents):
    comment = Comment.objects.get(comment_contents=comment_contents)

    return render(request, 'q27.html', {"comment": comment })

def post_comment_27(request):
    try:
        comment = request.POST["comment"]

    except KeyError as e:
        return render(request, 'q27.html')

    else:
        comment = Comment(comment_contents=comment)
        comment.save()

        return HttpResponseRedirect(reverse('question_1'))

def question_28(request):

        return render(request, 'Q28.html')
def comment_detail_28(request, comment_contents):
    comment = Comment.objects.get(comment_contents=comment_contents)

    return render(request, 'q28.html', {"comment": comment })

def post_comment_28(request):
    try:
        comment = request.POST["comment"]

    except KeyError as e:
        return render(request, 'q28.html')

    else:
        comment = Comment(comment_contents=comment)
        comment.save()

        return HttpResponseRedirect(reverse('question_1'))

def question_29(request):

        return render(request, 'Q29.html')
def comment_detail_29(request, comment_contents):
    comment = Comment.objects.get(comment_contents=comment_contents)

    return render(request, 'q29.html', {"comment": comment })

def post_comment_29(request):
    try:
        comment = request.POST["comment"]

    except KeyError as e:
        return render(request, 'q29.html')

    else:
        comment = Comment(comment_contents=comment)
        comment.save()

        return HttpResponseRedirect(reverse('question_1'))

def question_30(request):

        return render(request, 'q30.html')

def comment_detail_30(request, comment_contents):
    comment = Comment.objects.get(comment_contents=comment_contents)

    return render(request, 'q30.html', {"comment": comment })

def post_comment_30(request):
    try:
        comment = request.POST["comment"]

    except KeyError as e:
        return render(request, 'q30.html')

    else:
        comment = Comment(comment_contents=comment)
        comment.save()

        return HttpResponseRedirect(reverse('question_1'))

