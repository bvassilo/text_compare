import math
import numpy
from os import scandir
from os.path import isfile, join
from sklearn.feature_extraction.text import CountVectorizer
from operator import itemgetter
from collections import namedtuple
#from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity(x, y):

    dotP = numpy.dot(x, y.T)[0,0]
    magx = numpy.dot(x, x.T)[0,0] 
    magy = numpy.dot(y, y.T)[0,0]
    
    return dotP / math.sqrt(magx * magy)

def filereader(x):
    # "/Users/Bill/Desktop/text_files/"
    onlyfiles = [f for f in scandir(x) if isfile(join(x, f))]
    if len(onlyfiles) == 0:
        print("Empty directory")
        return 0
    
    for i,file in enumerate(onlyfiles):
        with open(onlyfiles[i], 'r' ) as f:
            onlyfiles[i] = f.read()
    
    return onlyfiles

def main():
    path = input("Enter a valid path to your files directory please: ")
    documents = filereader(path)
    if documents == 0: 
        print("Terminating")
        return 0

    n = len(documents)
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(documents)
    dictionary = count_vectorizer.vocabulary_
    result = namedtuple('result', 'similarity doc1 doc2')
    max_k = 0
    top_k = 0
    top_k = float(input("How many of the most similar texts you want to print: "))
    max_k = math.factorial(n)/(math.factorial(2) * math.factorial(n-2))

    max_k = int(round(max_k))

    result_list = [0 for x in range(max_k)]
    results = [[0 for x in range(n)] for x in range(n)]
    count = 0
    for i,file1 in enumerate(documents):
        for j,file2 in enumerate(documents):
            results[i][j]= cosine_similarity(count_matrix[i], count_matrix[j])
            if i < j: 
                result_list[count] = [result(similarity = results[i][j], doc1 = i, doc2 = j)]
                count+=1
    
    sorted(result_list, key=itemgetter(0))
    

    # print (results)
    while top_k > max_k:
        if top_k > max_k:
            print ("Impossible to print so many results")
        else:
            print ("ok i will")
            
    
   

main()

 # documents = ("Shipment of gold damaged in a fire", "Delivery of silver arrived in a silver truck", "Shipment of gold arrived in a truck")
    