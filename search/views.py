from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):

    if request.method == 'POST':
        word=request.POST['searchword']
        dictionary=PyDictionary()
        meanings=dictionary.meaning(word)
        synonyms=dictionary.synonym(word)
        antonyms=dictionary.antonym(word)
        try:
            for i in meanings.keys():
                l=[]
                for j in meanings[i]:
                    j=j.replace('(','')
                    l.append(j)
                meanings[i]=l
            if len(meanings)==0:
                meanings = 'error'
        except:
            meanings='error'
        try:
            if len(synonyms) == 0:
                synonyms='error'
        except:
            synonyms='error'
        try:
            if len(antonyms) == 0:
                antonyms='error'
        except:
            antonyms='error'

        return render(request,'result.html',{'meanings':meanings,'synonyms':synonyms,'antonyms':antonyms})
    else:
        return render(request,'home.html')
