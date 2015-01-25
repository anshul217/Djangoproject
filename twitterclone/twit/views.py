from django.shortcuts import render_to_response
from twit.models import twit
# Create your views here.
from forms import twitform
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def articles(request):

    return render_to_response('articles.html', {'twits': twit.objects.all()})


def article(request, twit_id=1):

    return render_to_response('article.html', {'twit': twit.objects.get(id=twit_id)})


def create(request):
    if request.POST:
        form = twitform(request.POST)
        if form.is_valid():
            form.save()

#            return HttpResponseRedirect('create_twit.html',form)
    else:
        form = twitform()

    args = {}

    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_twit.html', args)