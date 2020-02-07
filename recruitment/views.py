from django.shortcuts import render

def home(request):
    return render(request, 'recruitment/index.html',{})

def submission_form(request):
    if request.method == 'POST':
        print('Data! got')
    return render(request, 'recruitment/form.html', {})
