from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from mirror.models import season, seriesRus


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
