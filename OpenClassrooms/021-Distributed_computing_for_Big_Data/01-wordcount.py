from collections import defaultdict

# Standard version
def wordcount(text):
    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return(counts)


# MapReduce version
def map_function(key, value):
    map_result = []
    for word in value.split():
        map_result.append((word, 1))
    return(map_result)

def reduce_function(key, values):
    reduce_result = 0
    for val in values:
        reduce_result += val
    return(reduce_result)


if __name__ == '__main__':
    text = "jour lève notre grisaille" \
           + "trottoir notre ruelle notre tour" \
           + "jour lève notre envie vous" \
           + "faire comprendre tous notre tour"

    D1 = {"./lot1.txt" : "jour lève notre grisaille"}
    D2 = {"./lot2.txt" : "trottoir notre ruelle notre tour"}
    D3 = {"./lot3.txt" : "jour lève notre envie vous"}
    D4 = {"./lot4.txt" : "faire comprendre tous notre tour"}

    print('Naive wordcount:')
    print(wordcount(text), '\n')

    print('MapReduce wordcount:')
    print('\tIt\'s a bit more complicated')