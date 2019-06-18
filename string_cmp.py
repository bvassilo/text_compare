from math import sqrt, factorial
from numpy import dot
from os import scandir
from os.path import isfile, join
from sklearn.feature_extraction.text import CountVectorizer
def cosine_similarity(x, y):                                                    #calculating the cosine similarity of two vectors
    dotP = dot(x, y.T)[0,0]
    magx = dot(x, x.T)[0,0] 
    magy = dot(y, y.T)[0,0]
    return dotP / sqrt(magx * magy)
def filereader(x):                                                              #function that gets the path for the text files folder and returns a list of the files or read only
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
    n = len(documents)                                                           #calculating the number of the files
    count_vectorizer = CountVectorizer()                                         #initializing the vectorizer
    count_matrix = count_vectorizer.fit_transform(documents)                     #creating the vector matrix containing the vectrors for the similarity function
    dictionary = count_vectorizer.vocabulary_                                    #the dictionary of the files containig all the words from the files
    max_k = 0
    top_k = 0
    top_k = int(input("How many of the most similar texts you want to print: ")) #asking for the amount of the top-k similarities that the user needs to see 
    max_k = factorial(n)/(factorial(2) * factorial(n-2))                         #calculatin the max number of similarities tha we have given that we have the number of files
    max_k = int(round(max_k))                                                       
    result_list = [0 for x in range(max_k)]                                      #initializing the length of the result_list that will hold all the results
    count = 0
    for i,file1 in enumerate(documents):
        for j,file2 in enumerate(documents):
            if i < j: 
                result_list[count] = (cosine_similarity(count_matrix[i], count_matrix[j]),i,j) #filling the result list with the similarity of the docs and the nimbers of the docs
                count+=1
    x = sorted(result_list, key=lambda x: x[0], reverse=True)                    #sorting the result list based on the cosine similarity from lowest to highest number
    if top_k > max_k:                                                            #if the top_k(number of requested results) is bigger than the max_k (the number of the max results)  
        while top_k > max_k:                                                     #then we will keep asking for a top_k until we get one smaller than the max_k
            print ("Impossible to print so many results")
            top_k = int(input("How many of the most similar texts you want to print: "))
    if top_k <= max_k:                                                                        
        for i in range(top_k):
            print ("The top",i+1,"most similar docs is ", x[i])                  #else we normally print the top k results asked with their similarities and the docs that are being compared
main()