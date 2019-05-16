from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def two(request):
    from . import pythonScript

    textNeeded = request.GET["text"]
    textNeeded = textNeeded.upper()

    input = request.GET["calculate"]
    output = pythonScript.multiply(input)
    return render(request, "two.html", {"b":textNeeded, "c":output})

def model_train(request):
    from . import python_model
    python_model.model_train()
    return render(request, "home.html")

def model_predict(request):
    from . import python_model
    a = request.GET["first_value"]
    b = request.GET["second_value"]
    c = request.GET["third_value"]

    prediction = python_model.model_predict(a,b,c)
    return render(request, "home.html",{"result":prediction})
