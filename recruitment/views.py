from django.shortcuts import render
import datetime
import  re
from recruitment.models import *

def handle_uploaded_file(f, application_number, name):
    with open(f'uploads/{application_number}/{name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
    return render(request, 'recruitment/index.html',{})

def admin(request):
    return render(request, 'recruitment/admin.html',{})

def submission_form(request):
    if request.method == 'POST':
        data = request.POST.copy()
        applicant_data = {}
        number = len(Applicant.objects.filter(date=datetime.datetime.now().date()))
        application_number = str(datetime.datetime.now().date())+str(number+1).zfill(3) 
        applicant_data['application_no'] = application_number
        applicant_data['date'] = datetime.datetime.now().date()
        applicant_data['post'] = data['AppPost']
        applicant_data['department'] = data['Dept']
        applicant_data['research_domain'] = data['research_domain']
        applicant_data['full_name'] = data['fname'].strip() + ' ' + data['mname'].strip() + ' '  + data['lname'].strip()
        applicant_data['DOB'] = data['DOB']
        applicant_data['father_name'] = data['fathername']
        applicant_data['address_mail'] = data['mailadd']
        applicant_data['pin_mail'] = data['mailadd_pin']
        applicant_data['telephone_mail'] = data['mailadd_tele']
        applicant_data['address_perm'] = data['permadd']
        applicant_data['pin_perm'] = data['permadd_pin']
        applicant_data['telephone_perm'] = data['permadd_tele']
        applicant_data['mobile_number'] = data['phnum']
        applicant_data['email'] = data['email']
        applicant_data['gender'] = data['gender']
        applicant_data['marital_status'] = data['marital_stauts']
        applicant_data['nationality'] = data['nationality']
        applicant_data['state'] = data['state']
        applicant_data['category'] = data['category']
        applicant_data['reservation'] = data['reservecat']
        applicant_data['present_employer'] = data['present_employer']
        # other misc changes portions
        applicant_data['membership'] = data['membership']
        applicant_data['present_employer'] = data['present_employer']
        applicant_data['responsibilities'] = data['responsibilities']
        applicant_data['academic_year_break'] = data['academic_year_break']
        applicant_data['college_punishment'] = data['college_punishment']
        applicant_data['judicial_punishment'] = data['judicial_punishment']
        applicant_data['unfit_for_position'] = data['medical_unfit']
        applicant_data['references'] = data['references']
        #page4
        #model:Thesis
        applicant_data['ongoing_phd'] = data['ongoing_phd']
        applicant_data['completed_phd'] = data['completed_phd']
        #model:AdministrativeDetails
        applicant_data['administrative_details'] = data['administrative_details']
        #model:Patent
        applicant_data['patent_details'] = data['patent_details']
        #model:MembershipDetails
        applicant_data['member_details'] = data['member_details']
        #model:Summary
        applicant_data['defence_date'] = data['phd_defence_date']
        applicant_data['total_exp'] = data['total_exp']
        applicant_data['exp_post_phd'] = data['exp_post_phd']
        applicant_data['total_phd_students'] = data['total_phd_students']
        applicant_data['ongoing_phd_supervision'] = data['ongoing_phd_supervision']
        applicant_data['total_projects'] = data['total_projects']
        applicant_data['ongoing_projects'] = data['ongoing_projects']
        applicant_data['computational_projects'] = data['computational_projects']
        applicant_data['SCI_journal'] = data['SCI_journal']
        applicant_data['SCI_journal_post_phd'] = data['SCI_journal_post_phd']
        #model:SponsoredProject
        applicant_data['spo_tot_number'] = data['spo_tot_number']
        applicant_data['spo_ongoing'] = data['spo_ongoing']
        applicant_data['spo_completed'] = data['spo_completed']
        #model:Experiments
        applicant_data['exp_tot_number'] = data['exp_tot_number']
        applicant_data['exp_ongoing'] = data['exp_ongoing']
        applicant_data['exp_completed'] = data['exp_completed']

        num_of_academic_records = len(list(filter(lambda s: 'mark' in s,list(data.keys()))))
        academic_data = []
        for i in range(1,num_of_academic_records+1):
            academic_details = {}
            academic_details['degree'] = data.get('degree'+str(i),False)
            academic_details['area_of_qualification'] = data.get('qual' + str(i),False)
            academic_details['category_of_university'] = data.get('cat_univ' + str(i),False)
            academic_details['institute'] = data.get('institute' + str(i),False)
            academic_details['status'] = data.get('status' + str(i),False)
            academic_details['year_of_passing'] = data.get('pass' + str(i),False)
            if re.search(r'[12]\d{3}',data.get('pass'+str(i),False)) is None:
                return render(request, 'recruitment/form.html',{'message':'Enter the year in Academic details in yyyy format.'})
            if 0 <= float(data.get('marks' + str(i),False)) <= 100:
                academic_details['percentage']  = data.get('marks' + str(i),False)
            else:
                return render(request, 'recruitment/form.html',{'message':'Enter your percentage in Academic details a value between 0 to 100.'})
            academic_data.append(academic_details)
       
        num_of_professional_records = len(list(filter(lambda s: 'org' in s, list(data.keys()))))
        professional_data =  []
        for i in range(1,num_of_professional_records+1):
            professional_details = {}
            professional_details['organisation'] = data.get('org' + str(i),False)
            professional_details['designation']  = data.get('desig' + str(i),False)
            professional_details['from_year'] = data.get('proffrom' + str(i),False)
            professional_details['to_year'] = data.get('profto' + str(i),False)
            if re.search(r'[12]\d{3}',data.get('proffrom'+str(i),False)) is None:
                return render(request, 'recruitment/form.html',{'message':'Enter the year in professional details in yyyy format.'})
            if re.search(r'[12]\d{3}',data.get('profto'+str(i),False)) is None:
                return render(request, 'recruitment/form.html',{'message':'Enter the year in professional details in yyyy format.'})
            if int(data['proffrom' + str(i)]) > int(data['profto' + str(i)]):
                return render(request, 'recruitment/form.html',{'message':'From Year can not be after To year in Professional details.'})
            professional_details['role'] = data.get('roles' + str(i),False)
            professional_details['emoluments'] = data.get('pay' + str(i),False)
            if re.search(r'\d+', data['pay'+str(i)]) is None or re.search(r'\d+', data['pay'+str(i)]) is  None:
                return render(request, 'recruitment/form.html',{'message':'Enter the pay scale and emoluments in professional details as integers without commas.'})
            professional_details['pay_scale'] = data.get('emol' + str(i),False)
            professional_data.append(professional_details)
        other_details = {}
        other_details['awards_and_recognition'] = data['awards']
        other_details['reference'] = '\n'.join([data['ref1'],data['ref2'], data['ref3'],])
        other_details['statement_of_objective'] = data['objective']
        other_details['any_other_relevant_information'] = data['other_relevant_info']
        #publication = request.FILES['publications']
        #pic = request.FILES['propic']
        #cert = request.FILES['cert']
        #handle_uploaded_file(publication, application_number, 'publications')
        #handle_uploaded_file(pic, application_number, 'pic')
        #handle_uploaded_file(cert, application_number, 'certificate')
        #Storing data
        Applicant.objects.create(**applicant_data)
        academic_details['applicant'] = Applicant.objects.get(application_no=application_number)
        for academic_details in academic_data:
            Academic_detail.objects.create(**academic_details)
        
        professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
        for professional_details in professional_data:
            Professional_detail.objects.create(**professional_details) 
        
        other_details['applicant'] = Applicant.objects.get(application_no=application_number)
        Other_important_details.objects.create(**other_details)

        return render(request, 'recruitment/form.html',{'message':'Congrats! Your application number is '+ application_number})
    return render(request, 'recruitment/form.html', {})
