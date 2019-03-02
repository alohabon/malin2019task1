# library yang digunakan
import numpy as num
import collections
import csv
from operator import itemgetter

#untuk meyimpan data sementara
datrain = []
datest = []

#untuk membaca file csv yang telah disediakan 
with open('TestsetTugas1ML.csv') as csvfile:
    readTest = csv.DictReader(csvfile, data=',')
    for row in readTest:
        datest.append(row)
    return datest

with open('TrainsetTugas1ML.csv') as csvfile:
    readTrain = csv.DictReader(csvfile, data=',')
    for row in readTrain:
        datrain.append(row[1:])
    return datrain

#untuk menghitung data yes dan no pada 
def kelasYN(datrain):
    daYes = []
    daNo = []
    for row in datrain:
        if(row[9] == '<=50K'):
            daNo.append(row)
        else:
            daYes.append(row)
    return daNo,daYes


def cariprob(datrain):
    prob = []
    for row in datrain:
        hitdata = collections.Counter(row)
        prob1 = []
        for K1,V1 in zip(hitdata.keys(),hitdata.values()):
            prob1.append([k,v/len(row)])
        prob.append(prob1)
    return prob[len(prob)-1]

#nilai probabilitas
def dprob(a,datrain):
    for row in datrain:
        if (row[0] == a):
            return row[1]
    return 0

# untuk menyimpan hasil yang telah di dapatkan
with open('TebakanTugas1ML.csv','w', newline= '') as csvfile:
    fieldnames = ['hasil']
    writerhasil = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writerhasil.writeheader()
    for i in range(len(datest)):
        writerhasil.writerow({'hasil' : datest[i].y})

if __name__ == __main__:
    daYes, daNo = kelasYN(datrain)
    ProbIncome = [len(daYes)/len(datrain), len(daNo)/len(datrain)]
    ProbYes = cariprob(num.transpose(daYes))
    ProbNo = cariprob(num.transpose(daNo))

    hasil = []
    for row in datest:
        ProbabilitasYes = dprob(row[1], dprob[0]) * dprob(row[2], ProbYes[1]) * dprob(row[3], ProbYes[2]) * dprob(row[4], ProbYes[3]) * dprob(row[5], ProbYes[4]) * dprob(row[6], ProbYes[5]) * dprob(row[7], ProbYes[6]) * dprob(row[8], ProbYes[7]) * incomeProb[0]
        ProbabilitasNo = dprob(row[1], dprob[0]) * dprob(row[2], ProbNo[1]) * dprob(row[3], ProbNo[2]) * dprob(row[4], ProbNo[3]) * dprob(row[5], ProbNo[4]) * dprob(row[6], ProbNo[5]) * dprob(row[7], ProbNo[6]) * dprob(row[8], ProbNo[7]) * incomeProb[1]
        if(ProbabilitasYes > ProbabilitasNo):
            print('>50K')
            result.append([row[0], '>50K'])
        else:
            print('<=50K')
            result.append([row[0], '<=50K'])
    return(hasil)
