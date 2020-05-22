from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    fulltext=request.GET['fulltext']
    data=fulltext.split()
    worddict={}
    for word in data:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sorteddict=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fulltext':fulltext,'datacount':len(data),'countdata':sorteddict})
