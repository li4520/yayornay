import random


def rps_game(rounds):
    count = 0
    round_lists = []
    decision1_win_count = 0
    decision2_win_count = 0

    while count < rounds:
        # could create dictionry and return dictionary if needed
        WEAPONS = 'Rock', 'Paper', 'Scissors'
        decision1 = random.choice(range(0, 3))
        decision2 = random.choice(range(0, 3))
        temp_list = []
        temp_list.append(WEAPONS[decision1])
        temp_list.append(WEAPONS[decision2])

        # print "decision1: %s vs decision2: %s" % (WEAPONS[decision1], WEAPONS[decision2])
        if decision2 != decision1:
            if (decision1 - decision2) % 3 < (decision2 - decision1) % 3:
                # print "decision1 wins"
                temp_list.append("Yay")
                count += 1
                decision1_win_count += 1

            else:
                # print "decision2 wins"
                temp_list.append("Nay")
                count += 1
                decision2_win_count += 1

        else:
            # print "tie!"
            temp_list.append("Tie")

        round_lists.append(temp_list)
        # print(temp_list)

    # print(round_lists)
    return round_lists, decision1_win_count, decision2_win_count
