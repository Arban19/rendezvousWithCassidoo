def word_length_product(words):
    products = [0]
    for index, word in enumerate(words):
        char_set = set(word)
        succeeding_words = words[index:]
        for other_word in succeeding_words:
            if not char_set.intersection(set(other_word)):
                products.append(len(word)*len(other_word))
    return max(products)

assert word_length_product(["fish","fear","boo","egg","cake","abcdef"]) == 16
assert word_length_product(["a","aa","aaa","aaaa"]) == 0
