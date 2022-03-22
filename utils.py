import math


def vec_d(vec1, vec2):
    return math.sqrt(math.pow(vec2[0] - vec1[0], 2) + math.pow(vec2[1] - vec1[1], 2))