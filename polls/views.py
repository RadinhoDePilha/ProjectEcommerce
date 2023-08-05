from django.shortcuts import render, HttpResponse
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Aqui estõ os detalhes da questão %s" % question_id)


def results(request, question_id):
    return HttpResponse("Seguem os resultaods da questão %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote para a questão %s" % question_id)
