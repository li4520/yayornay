from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from cointoss.game_cointoss import *
from .models import Cointoss_Results

# Create your views here.


def cointoss_index(request):
    rounds = [1, 3, 5, 7]
    return render(request, 'cointoss/index.html', {'rounds': rounds})


def cointoss_results(request):
    # if "rounds" in request.POST:
    r = request.POST['rounds']
    d1 = request.POST['decision1']
    rounds = int(r)
    list_result, heads_win_count, tails_win_count = cointoss_game(rounds)

    cointoss_stats = Cointoss_Results.objects.get(game_name='cointoss')
    cointoss_stats.total_cointoss_initiated += 1
    cointoss_stats.total_round_count += rounds
    cointoss_stats.total_heads_count += heads_win_count
    cointoss_stats.total_tails_count += tails_win_count

    if heads_win_count > tails_win_count:
        yay_or_nay = 'Yay'
    else:
        yay_or_nay = 'Nay'

    cointoss_stats.save()

    return render(request, 'cointoss/results.html', {'list_result': list_result, 'd1': d1, 'heads_win_count': heads_win_count, 'tails_win_count': tails_win_count})
