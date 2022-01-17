from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rps.game_rps import *
from .models import RPS_Results

#from chat.consumers import *


# Create your views here.


def rps_index(request):
    rounds = [1, 3, 5, 7]
    return render(request, 'rps/index.html', {'rounds': rounds})


def rps_results(request):
    # if "rounds" in request.POST:
    r = request.POST['rounds']
    rounds = int(r)
    d1 = request.POST['decision1']
    #d2 = request.POST['decision2']
    list_result, d1_win_count, d2_win_count = rps_game(rounds)

    rps_stats = RPS_Results.objects.get(game_name='rps')
    rps_stats.total_rps_initiated += 1

    temp_total_round_count = len(list_result)
    rps_stats.total_round_count += temp_total_round_count

    temp_list_result = [num for elem in list_result for num in elem]
    temp_rock_count = temp_list_result.count('Rock')
    temp_paper_count = temp_list_result.count('Paper')
    temp_scissors_count = temp_list_result.count('Scissors')

    rps_stats.total_rock_count += temp_rock_count
    rps_stats.total_paper_count += temp_paper_count
    rps_stats.total_scissors_count += temp_scissors_count

    if d1_win_count > d2_win_count:
        yay_or_nay = 'Yay'
        rps_stats.rps_yay_count += 1
        # chat.consumers.receive("rock")

    else:
        yay_or_nay = 'Nay'
        rps_stats.rps_nay_count += 1

    rps_stats.save()

    return render(request, 'rps/results.html', {'list_result': list_result, 'd1': d1, 'd1_win_count': d1_win_count, 'd2_win_count': d2_win_count})
