from django.shortcuts import render
import pprint
def home(request):
    return render(request, 'recruitment/index.html',{})

def submission_form(request):
    if request.method == 'POST':
        data = request.POST.copy()
        pprint.pprint(data)
    return render(request, 'recruitment/form.html', {})
