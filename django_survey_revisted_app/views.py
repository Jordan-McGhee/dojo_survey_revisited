from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def survey(request):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['comment'] = request.POST['comment']

    return redirect("/result")

def result(request):
    # context = {
    #     "name" : request.session['name'],
    #     "dojo" : request.session['dojo'],
    #     "comment" : request.session['comment']
    # }
    return render(request, "request.html")