import random


def cointoss_game(rounds):
    count = 0
    heads_win_count = 0
    tails_win_count = 0
    cointoss = 'Heads', 'Tails'
    temp_list = []

    while count < rounds:
        coin = random.choice(cointoss)
        temp_list.append(coin)

        if coin == 'Heads':
            heads_win_count += 1
            count += 1
            # print(coin)

        else:
            tails_win_count += 1
            count += 1
            # print(coin)

    # print(temp_list)
    # print(heads_win_count)
    # print(tails_win_count)
    return temp_list, heads_win_count, tails_win_count
