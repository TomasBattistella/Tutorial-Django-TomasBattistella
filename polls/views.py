from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")

def detail(request, question_id):
    return HttpResponse("Youre looking at question %s" %question_id)

def results(request, question_id):
    response = "Youre looking at the result of question %s" 
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("Youre voting on question %s" %question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
