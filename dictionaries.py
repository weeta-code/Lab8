# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497

def count_words(words: tuple) -> dict:
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1
    return some_dict

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(commodities: tuple) -> dict:
    t_price= {}
    t_number = {}
    
    for commodity,price in commodities:
        t_price[commodity] = t_price.get(commodity, 0) + price
        t_number[commodity] = t_number.get(commodity, 0) + 1

    average_price = {commodity: t_price[commodity] / t_number[commodity] for commodity in t_price}
    return average_price

    
# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

def count_bigrams(s_tuple: tuple) -> dict:
    some_dict = {}
    i = 0
    f = 1
    while f < len(s_tuple):
        bigram  = (s_tuple[i], s_tuple[f])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else:
            some_dict[bigram] += 1
        i += 1
        f += 1
    return some_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))