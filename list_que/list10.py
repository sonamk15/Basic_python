def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    print (txt)
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(4, "The quick brown fox jumps over the lazy dog"))
