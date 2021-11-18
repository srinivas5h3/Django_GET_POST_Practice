from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Check GET & POST'
    }
    return render(request, 'index.html', context)
    
def cal(request):
    val1= int(request.POST["num1"])
    val2= int(request.POST["num2"])
    val3=request.POST["symbol"]
    if val3 == '+':
        res=val1 + val2
    elif val3 == '-':
        res=val1 - val2
    elif val3 == '*':
        res=val1 * val2
    elif val3 == '/':
        try:
            res=val1 / val2
        except:
            res="error"
    

    value = {
        'Result' : res,
        'title' : 'Check GET & POST'
    }
    
    return render(request, 'index.html', value)