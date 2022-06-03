import operator

def clean_text(lista_texto):
    list_clean_text = []
    for word_i in lista_texto:
        chars = ['-','¿','?','.',',','¡','!',':','"','–']
        for char_i in chars:
            word_i = word_i.replace(char_i,"")
        word_i= word_i.lower()
        if word_i != "":
            list_clean_text.append(word_i)
    return list_clean_text

def count_word(lista_texto):
    count_words = {}
    for word_i in lista_texto:
        if word_i in count_words.keys():
            count_words[word_i] = count_words[word_i] + 1
        else:
            count_words[word_i] = 1
    count_words = sorted(count_words.items(), key=operator.itemgetter(1), reverse=True)
    count_words=  list(count_words)
    return count_words

def most_frequent(count_words):
    lista_conteo = []
    for i in range(0,20):
        list_aux = []
        word, value = count_words[i]
        list_aux.append(word)
        list_aux.append(value)
        lista_conteo.append(list_aux)
    return lista_conteo



def main(lista_texto):
    # ACÁ INICIA LA FUNCIÓN main
    lista_texto = clean_text(lista_texto)
    count_words = count_word(lista_texto)
    lista_conteo = most_frequent(count_words)
    
    # ACÁ TERMINA LA FUNCIÓN main
    # NO MODIFICAR LA SIGUIENTE LÍNEA
    return lista_conteo