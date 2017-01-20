from django.core.validators import validate_email
from django.forms import forms
from django.shortcuts import render, get_object_or_404

# Create your views here.
from mirror.models import season, seriesRus, subscribers, questions, seriesEng


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
            subscribers(email=request.POST["email"]).save()
            return render(request, 'mirror/subscription.html', {'ok': 'ok',
                                                                'seasons': season.objects.all()})
        except forms.ValidationError:
            return render(request, 'mirror/subscription.html', {'errors': 'неверно введен e-mail'})
    else:
        return render(request, 'mirror/subscription.html', {'errors': None,
                                                            'seasons': season.objects.all()})


def callback(request):
    if request.method == "POST":
        try:
            validate_email(request.POST.get("email", ""))
            questions(name=request.POST.get("name", ""),
                      email=request.POST.get("email", ""),
                      question=request.POST.get("text", "")).save()
            return render(request, 'mirror/callback.html', {'seasons': season.objects.all(),
                                                            'ok': 'ok'})
        except forms.ValidationError:
            return render(request, 'mirror/callback.html', {'seasons': season.objects.all(),
                                                            'errors': 'неверно введен e-mail'})
    else:
        return render(request, 'mirror/callback.html', {'seasons': season.objects.all()})


def watch(request, seasonNum, seriesNum):
    seasonCurrent = get_object_or_404(season, number=int(seasonNum))
    allSeries = seriesRus.objects.filter(obj=seasonCurrent).order_by('number')

    # последняя ли серия
    max = int(seriesRus.objects.filter(obj=seasonCurrent).order_by('-number')[0].number)
    if int(seriesNum) < max:
        lastSeries = False
    else:
        lastSeries = True

    # последний ли сезон
    maxSes = int(season.objects.all().order_by('-number')[0].number)
    if int(seasonNum) < maxSes:
        lastSeason = False
    else:
        lastSeason = True

    # последняя серия в предыдущем сезоне
    if int(seasonNum) > 1:
        prevS = season.objects.filter(number=(int(seasonNum) - 1))[0].number
        prev = int(seriesRus.objects.filter(obj=prevS).order_by('-number')[0].number)
    else:
        prev = 0

    ses = seriesRus.objects.filter(obj=seasonCurrent, number=seriesNum)[0]
    return render(request, 'mirror/watch.html', {'seasonNum': int(seasonNum),
                                                 'seriesNum': int(seriesNum),
                                                 'series': allSeries,
                                                 'seasons': season.objects.all(),
                                                 'islastSeries': lastSeries,
                                                 'islastSeason': lastSeason,
                                                 'ses': ses,
                                                 'nextNumSeries': int(seriesNum) + 1,
                                                 'nextNumSeason': int(seasonNum) + 1,
                                                 'prevSeries': int(seriesNum) - 1,
                                                 'prevSeason': int(seasonNum) - 1,
                                                 'prev': int(prev)})


def watchEngl(request, seasonNum, seriesNum):
    seasonCurrent = get_object_or_404(season, number=int(seasonNum))
    allSeries = seriesRus.objects.filter(obj=seasonCurrent).order_by('number')

    # последняя ли серия
    max = int(seriesRus.objects.filter(obj=seasonCurrent).order_by('-number')[0].number)
    if int(seriesNum) < max:
        lastSeries = False
    else:
        lastSeries = True

    # последний ли сезон
    maxSes = int(season.objects.all().order_by('-number')[0].number)
    if int(seasonNum) < maxSes:
        lastSeason = False
    else:
        lastSeason = True

    # последняя серия в предыдущем сезоне
    if int(seasonNum) > 1:
        prevS = season.objects.filter(number=(int(seasonNum) - 1))[0].number
        prev = int(seriesRus.objects.filter(obj=prevS).order_by('-number')[0].number)
    else:
        prev = 0

    rusAnalog = seriesRus.objects.filter(obj=seasonCurrent, season=int(seasonNum), number=int(seriesNum))
    ses = seriesEng.objects.filter(obj=rusAnalog)[0]
    return render(request, 'mirror/watchEng.html', {'seasonNum': int(seasonNum),
                                                 'seriesNum': int(seriesNum),
                                                 'series': allSeries,
                                                 'seasons': season.objects.all(),
                                                 'islastSeries': lastSeries,
                                                 'islastSeason': lastSeason,
                                                 'ses': ses,
                                                 'nextNumSeries': int(seriesNum) + 1,
                                                 'nextNumSeason': int(seasonNum) + 1,
                                                 'prevSeries': int(seriesNum) - 1,
                                                 'prevSeason': int(seasonNum) - 1,
                                                 'prev': int(prev)})