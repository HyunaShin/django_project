"""skin_type URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from skin import views as sk_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^username$', sk_views.userName, name='userName'),

    url(r'^q1$', sk_views.question_1, name='question_1'),
    url(r'^q2$', sk_views.question_2, name='question_2'),
    url(r'^q3$', sk_views.question_3, name='question_3'),
    url(r'^q4$', sk_views.question_4, name='question_4'),
    url(r'^q5$', sk_views.question_5, name='question_5'),
    url(r'^q6$', sk_views.question_6, name='question_6'),
    url(r'^q7$', sk_views.question_7, name='question_7'),
    url(r'^q8$', sk_views.question_8, name='question_8'),
    url(r'^q9$', sk_views.question_9, name='question_9'),
    url(r'^q10$', sk_views.question_10, name='question_10'),
    url(r'^q11$', sk_views.question_11, name='question_11'),
    url(r'^q12$', sk_views.question_12, name='question_12'),
    url(r'^q13$', sk_views.question_13, name='question_13'),
    url(r'^q14$', sk_views.question_14, name='question_14'),
    url(r'^q15$', sk_views.question_15, name='question_15'),
    url(r'^q16$', sk_views.question_16, name='question_16'),
    url(r'^q17$', sk_views.question_17, name='question_17'),
    url(r'^q18$', sk_views.question_18, name='question_18'),
    url(r'^q19$', sk_views.question_19, name='question_19'),
    url(r'^q20$', sk_views.question_20, name='question_20'),
    url(r'^q21$', sk_views.question_21, name='question_21'),
    url(r'^q22$', sk_views.question_22, name='question_22'),
    url(r'^q23$', sk_views.question_23, name='question_23'),
    url(r'^q24$', sk_views.question_24, name='question_24'),
    url(r'^q25$', sk_views.question_25, name='question_25'),

    # url(r'^login$', sk_views.login, name='login')

]
