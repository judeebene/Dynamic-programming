
#Q. Count number of ways to reach a given score in a game

#Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of ways to reach the given score.

#Examples:
#Input: n = 20 Output: 4
#There are following 4 ways to reach 20 (10, 10) (5, 5, 10) (5, 5, 5, 5) (3, 3, 3, 3, 3, 5)

#Input: n = 13 Output: 2
# There are following 2 ways to reach 13 (3, 5, 5) (3, 10)

def count_dp_bottom(n, scores, end_index):

    table = [0 for i in range(n + 1)]

    # base case
    table[0] = 1

    # One by one consider given 3 scores and update the
    # table[] values after the index greater than or equal
    # to the value of the picked score.
    for i in range(3, n + 1):
        table[i] += table[i - 3]
    for i in range(5, n + 1):
        table[i] += table[i - 5]
    for i in range(10, n + 1):
        table[i] += table[i - 10]

    return table[n]


def count_dp(n, scores, end_index):
    key = str(n) + ":" + str(end_index)
    dict1 = {}
    if dict1.get(key):
        return dict1.get(key)

    if n == 0:
        return 1

    elif n < 0 or end_index < 0:
        return 0

    elif scores[end_index] > n:
        val = count_dp(n, scores, end_index - 1)
    else:
        val = count_dp(n - scores[end_index], scores, end_index) + count_dp(n, scores, end_index - 1)

    dict1[key] = val

    return val