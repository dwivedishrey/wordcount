from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
     return render(request,'home.html')
def count(request):
    fulltexts=request.GET['fulltext']
    wordlist=fulltexts.split()
    worddicitionary ={}
    for word in wordlist:
        if word in worddicitionary:
            worddicitionary[word]+=1
        else:
            worddicitionary[word]=1
    sortedwords=sorted(worddicitionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltexts,'count':len(wordlist),'sortedwords':sortedwords})
