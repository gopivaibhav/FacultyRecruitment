from django.shortcuts import render
import datetime
import pprint
from recruitment.models import *
def home(request):
    return render(request, 'recruitment/index.html',{})

def submission_form(request):
    if request.method == 'POST':
        data = request.POST.copy()
        pprint.pprint(data)
        applicant_data = {}
        number = len(Applicant.objects.filter(date=datetime.datetime.now().date()))
        application_number = str(datetime.datetime.now().date())+str(number+1).zfill(3) 
        applicant_data['application_no'] = application_number
        applicant_data['date'] = datetime.datetime.now().date()
        applicant_data['post'] = data['AppPost']
        applicant_data['name'] = data['fname'].strip() + ' ' + data['mname'].strip() + ' '  + data['lname'].strip()
        applicant_data['phone'] = data['phnum']
        applicant_data['gender'] = data['gender']
        applicant_data['category'] = data['category']
        applicant_data['reservation'] = data['reservecat']
        applicant_data['current_address'] = data['curadd']
        applicant_data['permanent_address'] = data['permadd']
        applicant_data['department'] = data['Dept']
        #print(applicant_data)
        Applicant.objects.create(**applicant_data)
        num_of_academic_records = len(list(filter(lambda s: 'mark' in s,list(data.keys()))))
        for i in range(1,num_of_academic_records+1):
            academic_details = {}
            academic_details['applicant'] = Applicant.objects.get(application_no=application_number)
            academic_details['degree'] = data['degree'+str(i)]
            academic_details['area_of_qualification'] = data['qual' + str(i)]
            academic_details['category_of_university'] = data['cat_univ' + str(i)]
            academic_details['institute'] = data['institute' + str(i)]
            academic_details['status'] = data['status' + str(i)]
            academic_details['year_of_passing'] = data['pass' + str(i)]
            academic_details['percentage']  = data['marks' + str(i)]
            pprint.pprint(academic_details)
            Academic_detail.objects.create(**academic_details)

        num_of_professional_records = len(list(filter(lambda s: 'org' in s, list(data.keys()))))
        for i in range(1,num_of_professional_records+1):
            professional_details = {}
            professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
            professional_details['organisation'] = data['org' + str(i)]
            professional_details['designation']  = data['desig' + str(i)]
            professional_details['from_year'] = data['proffrom' + str(i)]
            professional_details['to_year'] = data['profto' + str(i)]
            professional_details['role'] = data['roles' + str(i)]
            professional_details['emoluments'] = data['pay' + str(i)]
            professional_details['pay_scale'] = data['emol' + str(i)]
        Professional_detail.objects.create(**professional_details)

        return render(request, 'recruitment/form.html',{'message':'Success!'})
    return render(request, 'recruitment/form.html', {})
