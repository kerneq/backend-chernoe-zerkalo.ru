from django.core.validators import validate_email
from django.forms import forms
from django.shortcuts import render, get_object_or_404

# Create your views here.
from mirror.models import season, seriesRus, subscribers


def index(request):
    dictionary = {}
    listOfSeasons = season.objects.order_by('-number')
    for ses in listOfSeasons:
        listOfSeries = seriesRus.objects.filter(obj=ses).order_by('number')
        dictionary[ses.number] = listOfSeries
    return render(request, 'mirror/index.html', {'dict': dictionary})


def seasonView(request, num):
    currentSeason = get_object_or_404(season, number=int(num))
    series = seriesRus.objects.filter(obj=currentSeason).order_by('number')
    return render(request, 'mirror/season.html', {'season': currentSeason,
                                                  'series': series,
                                                  'seasons': season.objects.all()})


def subscribe(request):
    if request.method == "POST":
        try:
            validate_email(request.POST.get("email", ""))
            subscribers(email=request.POST['email']).save()
            return index(request)
        except forms.ValidationError:
            return render(request, 'mirror/subscribe.html', {'error': 'неверно введен e-mail'})
    else:
        return render(request, 'mirror/subscription.html', {'error': None,
                                                            'seasons': season.objects.all()})