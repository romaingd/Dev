#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

total = 0
n = 7967
lastcolumn = None
IndexList = []
PageRankList = []
end_of_list = " -1"

i = 0
while i < n:
    PageRankList.append(0)
    IndexList.append([])
    i += 1

for line in sys.stdin:
    line = line.strip()

    # recuperer la cle et la valeur et conversion de la valeur en int
    column, index, value = line.split("\t")
    value = float(value)
    column = int(column)
    index = int(index)

    # passage au mot suivant (plusieurs cles possibles pour une même exécution de programme)
    if lastcolumn is None:
        lastcolumn = column
    if column == lastcolumn:
        total += value
        IndexList[index].append(str(lastcolumn))
    else:
        PageRankList[lastcolumn] = total
        # print("%s\t%f" % (lastcolumn, total))
        total = value
        lastcolumn = column
        IndexList[index].append(str(lastcolumn))

if lastcolumn is not None:
    PageRankList[column] = total
    IndexList[index].append(str(lastcolumn))
    # print("%s\t%f" % (lastcolumn, total))

for i, value in enumerate(PageRankList):
    # print("%d\t%f\t%s" % (i, value, " ".join(IndexList[i]) + " -1"))
    print("%d\t%f" % (i, value))
