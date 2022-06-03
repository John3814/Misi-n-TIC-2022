import numpy as np
import random

def balotera(balotas):
    # ACÁ INICIA LA FUNCIÓN
    vector = np.array(balotas)
    random.shuffle(vector)

    balotas_min = []
    count_b = 0
    count_i = 0
    count_n = 0
    count_g = 0 
    count_o = 0
    is_bingo = False

    counter = 0

    balotas_b = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15']
    balotas_i = ['I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24','I25', 'I26', 'I27', 'I28', 'I29', 'I30']
    balotas_n = ['N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45']
    balotas_g = ['G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60']
    balotas_o = ['O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'O71', 'O72', 'O73', 'O74', 'O75']

    while is_bingo == False:
        if vector[counter] in balotas_b:
            count_b += 1
            balotas_min.append(vector[counter])
        elif vector[counter] in balotas_i:
            count_i += 1
            balotas_min.append(vector[counter])
        elif vector[counter] in balotas_n:
            count_n += 1
            balotas_min.append(vector[counter])
        elif vector[counter] in balotas_g:
            count_g += 1
            balotas_min.append(vector[counter])
        elif vector[counter] in balotas_o:
            count_o += 1
            balotas_min.append(vector[counter])

        counter += 1

        if (count_b>=5) and (count_i>=5) and (count_n>=4) and (count_g>=5) and (count_o>=5):
            is_bingo = True
    balotas_revueltas = tuple(balotas_min)

    return balotas_revueltas
    