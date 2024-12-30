from django.shortcuts import render
from tracker.models import Score
from tracker.forms import ScoreForm

def index(request):
    context = {} # attributes 1-1 relationship + search
    form = ScoreForm()
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Home'
    context['form'] = form
    if request.method == 'POST':
        if 'save' in request.POST:
            primKey = request.POST.get('save')
            if not primKey:
                form = ScoreForm(request.POST)
            else:
                score= Score.objects.get(id=primKey)
                form = ScoreForm(request.POST, instance=score)
            form.save()
            form = ScoreForm()
        elif 'delete' in request.POST:
            primKey = request.POST.get('delete') # gets id of 'delete' from POST request 
            score = Score.objects.get(id=primKey) # uses that id as a primary key to find score value associated with that primKey
            score.delete()
        elif 'edit' in request.POST:
            primKey = request.POST.get('edit')
            score = Score.objects.get(id=primKey)
            form = ScoreForm(instance=score)
    context['form'] = form
    return render(request,'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request,'about.html', context)
