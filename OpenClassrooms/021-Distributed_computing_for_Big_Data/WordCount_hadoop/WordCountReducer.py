import sys
total = 0
lastword = None

for line in sys.stdin:
    line = line.strip()

    word, count = line.split()
    count = int(count)

    if lastword is None:
        lastword = word
    if word == lastword:
        total += count
    else:
        print("%s\t%d occurences" % (lastword, total))
        total = count
        lastword = word

if lastword is not None:
    print("%s\t%d occurences" % (lastword, total))
