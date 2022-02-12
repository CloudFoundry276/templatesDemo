from django.shortcuts import render


# Create your views here.
def renderTemplate(request):
    my_dict = {"name": "John Smith"}
    return render(request, 'templatesApp/firstTemplate.html', context=my_dict)


def renderEmployee(request):
    my_emp = {"id": 123, "name": "Marry Smith", "sal": 10000}
    return render(request, 'templatesApp/employeeTemplate.html', my_emp)
