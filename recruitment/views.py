from django.shortcuts import render
import datetime
import pprint, re
from recruitment.models import *

def handle_uploaded_file(f, application_number, name):
    with open(f'uploads/{application_number}/{name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

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
        Applicant.objects.create(**applicant_data)
        num_of_academic_records = len(list(filter(lambda s: 'mark' in s,list(data.keys()))))
        academic_data = []
        for i in range(1,num_of_academic_records+1):
            academic_details = {}
            academic_details['applicant'] = Applicant.objects.get(application_no=application_number)
            academic_details['degree'] = data['degree'+str(i)]
            academic_details['area_of_qualification'] = data['qual' + str(i)]
            academic_details['category_of_university'] = data['cat_univ' + str(i)]
            academic_details['institute'] = data['institute' + str(i)]
            academic_details['status'] = data['status' + str(i)]
            academic_details['year_of_passing'] = data['pass' + str(i)]
            if re.search(r'[12]\d{3}',data['pass'+str(i)]) is None:
                return render(request, 'recruitment/form.html',{'message':'Enter the year in Academic details in yyyy format.'})
            academic_details['percentage']  = data['marks' + str(i)]
            academic_data.append(academic_details)
        for academic_details in academic_data:
             Academic_detail.objects.create(**academic_details)

        num_of_professional_records = len(list(filter(lambda s: 'org' in s, list(data.keys()))))
        professional_data =  []
        for i in range(1,num_of_professional_records+1):
            professional_details = {}
            professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
            professional_details['organisation'] = data['org' + str(i)]
            professional_details['designation']  = data['desig' + str(i)]
            professional_details['from_year'] = data['proffrom' + str(i)]
            professional_details['to_year'] = data['profto' + str(i)]
            if re.search(r'[12]\d{3}',data['proffrom'+str(i)]) is None:
                return render(request, 'recruitment/form.html',{'message':'Enter the year in professional details in yyyy format.'})
            if re.search(r'[12]\d{3}',data['profto'+str(i)]) is None:
                return render(request, 'recruitment/form.html',{'message':'Enter the year in professional details in yyyy format.'})
            if int(data['profrom' + str(i)] > int(data['profto' + str(i)])):
                return render(request, 'recruitment/form.html',{'message':'From Year can not be after To year in Professional details.'})
            professional_details['role'] = data['roles' + str(i)]
            professional_details['emoluments'] = data['pay' + str(i)]
            professional_details['pay_scale'] = data['emol' + str(i)]
            professional_data.append(professional_details)
        for professional_details in professional_data:
            Professional_detail.objects.create(**professional_details)
        other_details = {}
        other_details['applicant'] = Applicant.objects.get(application_no=application_number)
        other_details['awards_and_recognition'] = data['awards']
        other_details['reference'] = '\n'.join([data['ref1'],data['ref2'], data['ref3'],])
        other_details['statement_of_objective'] = data['objective']
        other_details['any_other_relevant_information'] = data['other_relevant_info']
        Other_important_details.objects.create(**other_details)
        #publication = request.FILES['publications']
        #pic = request.FILES['propic']
        #cert = request.FILES['cert']
        #handle_uploaded_file(publication, application_number, 'publications')
        #handle_uploaded_file(pic, application_number, 'pic')
        #handle_uploaded_file(cert, application_number, 'certificate')
        return render(request, 'recruitment/form.html',{'message':'Congrats! Your application number is '+ application_number})
    return render(request, 'recruitment/form.html', {})
