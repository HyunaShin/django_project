from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse
# Create your views here.



def userName(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'Page_1.html')

    all_username = None
    if request.method == 'POST':
        username = Username(
            user_name=request.POST["user_name"]
        )
        username.save()
        result = { "user_name": request.POST["user_name"]}

        return render(request, 'Page_2.html', result)
    else:
        all_username = Username.objects.all()
        result = {"user_name": all_username}
        return render(request, 'Page_2.html', result)


def results(request):
    response = "%s님의 피부타입은"
    return HttpResponse(response % username, 'Page_32.html')

def post_comment(request):
    if request.method == "POST":
        id = request.POST["username"]
        comment = request.POST["comment"]

        comment = Comment.objects.create(comment_contents=comment,user=user,bookmark=bookmark)
        print(comment.comment_contents)
        comment.save()
