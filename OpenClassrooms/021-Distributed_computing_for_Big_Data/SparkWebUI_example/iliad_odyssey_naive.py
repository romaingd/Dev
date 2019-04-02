from pyspark import SparkContext

sc = SparkContext()

def star(f):
    return lambda args: f(*args)

def filter_stop_words(word):
    from nltk.corpus import stopwords
    english_stop_words = stopwords.words("english")
    return word not in english_stop_words

def load_text(text_path):
    vocabulary = sc.textFile(text_path)\
                   .flatMap(lambda lines: lines.lower().split())\
                   .flatMap(lambda word: word.split("."))\
                   .flatMap(lambda word: word.split(","))\
                   .flatMap(lambda word: word.split("!"))\
                   .flatMap(lambda word: word.split("?"))\
                   .flatMap(lambda word: word.split("'"))\
                   .flatMap(lambda word: word.split("\""))\
                   .filter(lambda word: word is not None and len(word) > 0)\
                   .filter(filter_stop_words)

    word_count = vocabulary.count()

    word_freq = vocabulary.map(lambda word: (word, 1))\
                          .reduceByKey(lambda count1, count2: count1 + count2)\
                          .map(star(lambda word, count: (word, count / float(word_count))))
    
    return(word_freq)


def main():
    iliad = load_text('input/iliad.mb.txt')
    odyssey = load_text('input/odyssey.mb.txt')

    # Join the two datasets and compute the difference in frequency
    # Note that we need to write (freq or 0) because some words do not appear
    # in one of the two books. Thus, some frequencies are equal to None after
    # the full outer join.
    join_words = iliad.fullOuterJoin(odyssey)\
                      .map(star(lambda word, freq_tuple: (word, (freq_tuple[1] or 0) - (freq_tuple[0] or 0))))
    
    # 10 words that get a boost in frequency in the sequel
    emerging_words = join_words.takeOrdered(
        10,
        star(lambda word, freq_diff: -freq_diff)
    )
    # 10 words that get a decrease in frequency in the sequel
    disappearing_words = join_words.takeOrdered(
        10,
        star(lambda word, freq_diff: freq_diff)
    )

    # Print results
    for word, freq_diff in emerging_words:
        print('%.2f' % (freq_diff*1e4), word)
    for word, freq_diff in disappearing_words[::-1]:
        print('%.2f' % (freq_diff*1e4), word)
    
    # Trick to keep access to the Web UI
    input('Press Ctrl+C to exit')

if __name__ == '__main__':
    main()