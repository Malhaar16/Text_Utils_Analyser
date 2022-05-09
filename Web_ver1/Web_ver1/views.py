from django.http import HttpResponse
from django.shortcuts import render
#Homepage
def index(request):

    return render(request,'index.html')
    #return HttpResponse('''Homepage''')




def analyze(request):
    #Get the text
    text1 = request.POST.get('text','default')

#Check the checkbox
    # Punctuation
    text2 = request.POST.get('removepunc','off')

    #Captial letter String
    text3 = request.POST.get('fullcap','off')

    #remove new line
    text4 = request.POST.get('removenewline','off')


    if text2 == "on":
        punctuations = ''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
        analysed = ""
        for char in text1:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':'Remove Punctuations','analysed_text':analysed}

        text1 = analysed
        #return  render(request,'analyze.html',params)
    if text3 == "on":
        analysed = ""
        for i in text1:
            analysed = analysed + i.upper()


        params = {'purpose':'Upper Case','analysed_text':analysed}
        text1 = analysed
        #return render(request,'analyze.html',params)

    if text4 == "on":
        analysed = ""
        for i in text1:
            if i != "\n" and i !="\r":
                analysed = analysed + i

        params = {'purpose':'Remove New Line','analysed_text':analysed}
        text1 = analysed



    if text2 != "on" and text3 != "on" and text4 != "on" :
        return HttpResponse('Select at least one operation')



    return render(request, 'analyze.html', params)

def about_us(request):
    return render(request,"about_us.html")

