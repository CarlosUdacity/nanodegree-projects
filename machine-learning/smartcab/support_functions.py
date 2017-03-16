import random


def weighted_choice(weights):
    """
    The following is a simple function to implement weighted random selection in Python.
    Given a list of weights, it returns an index randomly, according to these weights
    :param weights: list of weights
    :return: the index with the probability
    """
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i


def xstr(s):
    if s is None:
        return 'none'
    return s


def state_str1(state):
    aux = xstr(state[0]) + '_' + xstr(state[1]['light']) + '_' + xstr(state[1]['oncoming']) + '_' + xstr(state[1]['left'])
    aux = aux.replace("__", "_")

    if aux[-1:] == "_":
        aux = aux[:(len(aux) - 1)]

    return aux


def state_str2(state):
    aux = xstr(state[0]) + '_' + xstr(state[1]) + '_' + xstr(state[2]) + '_' + xstr(state[3])
    aux = aux.replace("__", "_")

    if aux[-1:] == "_":
        aux = aux[:(len(aux) - 1)]

    return aux
