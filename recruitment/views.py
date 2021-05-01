from django.shortcuts import render
import datetime
import  re
from recruitment.models import *

def handle_uploaded_file(f, application_number, name):
    with open(f'uploads/{application_number}/{name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def login(request):
    return render(request, 'recruitment/login.html',{})

def home(request):
    return render(request, 'recruitment/index.html',{})

def admin(request):
    return render(request, 'recruitment/admin.html',{})

def submission_form(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # Applicant
        applicant_data = {}
        number = len(Applicant.objects.filter(date=datetime.datetime.now().date()))
        application_number = str(datetime.datetime.now().date())+str(number+1).zfill(3) 
        applicant_data['application_no'] = application_number
        applicant_data['date'] = datetime.datetime.now().date()
        applicant_data['post'] = data['AppPost']
        applicant_data['department'] = data['Dept']
        applicant_data['Research_Domain'] = data['research_domain']
        Applicant.objects.create(**applicant_data)
        # General
        general_data={}
        general_data['full_name'] = data['name'].strip()
        general_data['DOB'] = data['dateofbirth']
        general_data['father_name'] = data['fathername']
        general_data['address_perm'] = data['permanentaddress']
        general_data['telephone_perm'] = data['permanentpincode']
        general_data['pin_perm'] = data['permanenttelephone']
        general_data['address_mail'] = data['mailingaddress']
        general_data['telephone_mail'] = data['mailingtelephone']
        general_data['pin_mail'] = data['mailingpincode']
        general_data['mobile_number'] = data['mobilecode'] + data['mobile']
        # general_data['email'] = data['email']
        # general_data['gender'] = data['gender']
        general_data['marital_status'] = data['maritalstatus']
        general_data['nationality'] = data['nationality']
        general_data['state'] = data['domicile_state']
        general_data['category'] = data['category']
        general_data['reservation'] = data['reservation_certificate']
        general_data['present_employer'] = data['present_employer']
        general_data['applicant'] = Applicant.objects.get(application_no=application_number) 
        General.objects.create(**general_data)
        # Other Information
        otherinformation_data = {}
        otherinformation_data['membership'] = data['miscTa1']
        otherinformation_data['responsibilities'] = data['miscTa2']
        otherinformation_data['academic_year_break'] = data['miscTa4']
        otherinformation_data['college_punishment'] = data['miscTa5']
        otherinformation_data['judicial_punishment'] = data['miscTa6']
        otherinformation_data['unfit_for_position'] = data['miscTa7']
        otherinformation_data['references'] = data['miscTa8']
        otherinformation_data['applicant'] = Applicant.objects.get(application_no=application_number) 
        OtherInfo.objects.create(**otherinformation_data)
        # Educational Qualifictaions
        num_of_academic_records = len(list(filter(lambda s: 'mark' in s,list(data.keys()))))
        academic_data = []
        for i in range(1,num_of_academic_records+1):
        # #page4
        # #model:Thesis
        # applicant_data['ongoing_phd'] = data['ongoing_phd']
        # applicant_data['completed_phd'] = data['completed_phd']
        # #model:AdministrativeDetails
        # applicant_data['administrative_details'] = data['administrative_details']
        # #model:Patent
        # applicant_data['patent_details'] = data['patent_details']
        # #model:MembershipDetails
        # applicant_data['member_details'] = data['member_details']
        # #model:Summary
        # applicant_data['defence_date'] = data['phd_defence_date']
        # applicant_data['total_exp'] = data['total_exp']
        # applicant_data['exp_post_phd'] = data['exp_post_phd']
        # applicant_data['total_phd_students'] = data['total_phd_students']
        # applicant_data['ongoing_phd_supervision'] = data['ongoing_phd_supervision']
        # applicant_data['total_projects'] = data['total_projects']
        # applicant_data['ongoing_projects'] = data['ongoing_projects']
        # applicant_data['computational_projects'] = data['computational_projects']
        # applicant_data['SCI_journal'] = data['SCI_journal']
        # applicant_data['SCI_journal_post_phd'] = data['SCI_journal_post_phd']
        # #model:SponsoredProject
        # applicant_data['spo_tot_number'] = data['spo_tot_number']
        # applicant_data['spo_ongoing'] = data['spo_ongoing']
        # applicant_data['spo_completed'] = data['spo_completed']
        # #model:Experiments
        # applicant_data['exp_tot_number'] = data['exp_tot_number']
        # applicant_data['exp_ongoing'] = data['exp_ongoing']
        # applicant_data['exp_completed'] = data['exp_completed']

        # num_of_academic_records = len(list(filter(lambda s: 'mark' in s,list(data.keys()))))
        # academic_data = []
        # for i in range(1,num_of_academic_records+1):
        #     academic_details = {}
        #     academic_details['degree'] = data.get('degree'+str(i),False)
        #     academic_details['area_of_qualification'] = data.get('qual' + str(i),False)
        #     academic_details['category_of_university'] = data.get('cat_univ' + str(i),False)
        #     academic_details['institute'] = data.get('institute' + str(i),False)
        #     academic_details['status'] = data.get('status' + str(i),False)
        #     academic_details['year_of_passing'] = data.get('pass' + str(i),False)
        #     if re.search(r'[12]\d{3}',data.get('pass'+str(i),False)) is None:
        #         return render(request, 'recruitment/form.html',{'message':'Enter the year in Academic details in yyyy format.'})
        #     if 0 <= float(data.get('marks' + str(i),False)) <= 100:
        #         academic_details['percentage']  = data.get('marks' + str(i),False)
        #     else:
        #         return render(request, 'recruitment/form.html',{'message':'Enter your percentage in Academic details a value between 0 to 100.'})
        #     academic_data.append(academic_details)
       
        # num_of_professional_records = len(list(filter(lambda s: 'org' in s, list(data.keys()))))
        # professional_data =  []
        # for i in range(1,num_of_professional_records+1):
        #     professional_details = {}
        #     professional_details['organisation'] = data.get('org' + str(i),False)
        #     professional_details['designation']  = data.get('desig' + str(i),False)
        #     professional_details['from_year'] = data.get('proffrom' + str(i),False)
        #     professional_details['to_year'] = data.get('profto' + str(i),False)
        #     if re.search(r'[12]\d{3}',data.get('proffrom'+str(i),False)) is None:
        #         return render(request, 'recruitment/form.html',{'message':'Enter the year in professional details in yyyy format.'})
        #     if re.search(r'[12]\d{3}',data.get('profto'+str(i),False)) is None:
        #         return render(request, 'recruitment/form.html',{'message':'Enter the year in professional details in yyyy format.'})
        #     if int(data['proffrom' + str(i)]) > int(data['profto' + str(i)]):
        #         return render(request, 'recruitment/form.html',{'message':'From Year can not be after To year in Professional details.'})
        #     professional_details['role'] = data.get('roles' + str(i),False)
        #     professional_details['emoluments'] = data.get('pay' + str(i),False)
        #     if re.search(r'\d+', data['pay'+str(i)]) is None or re.search(r'\d+', data['pay'+str(i)]) is  None:
        #         return render(request, 'recruitment/form.html',{'message':'Enter the pay scale and emoluments in professional details as integers without commas.'})
        #     professional_details['pay_scale'] = data.get('emol' + str(i),False)
        #     professional_data.append(professional_details)
        # other_details = {}
        # other_details['awards_and_recognition'] = data['awards']
        # other_details['reference'] = '\n'.join([data['ref1'],data['ref2'], data['ref3'],])
        # other_details['statement_of_objective'] = data['objective']
        # other_details['any_other_relevant_information'] = data['other_relevant_info']
        # #publication = request.FILES['publications']
        # #pic = request.FILES['propic']
        # #cert = request.FILES['cert']
        # #handle_uploaded_file(publication, application_number, 'publications')
        # #handle_uploaded_file(pic, application_number, 'pic')
        # #handle_uploaded_file(cert, application_number, 'certificate')
        # #Storing data
        # # Applicant.objects.create(**applicant_data)
        # # academic_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # # for academic_details in academic_data:
        # #     Academic_detail.objects.create(**academic_details)
        
        # # professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # # for professional_details in professional_data:
        # #     Professional_detail.objects.create(**professional_details) 
        
        # # other_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # # Other_important_details.objects.create(**other_details)

        return render(request, 'recruitment/form.html',{'message':'Congrats! Your application number is '+ application_number})
    return render(request, 'recruitment/form.html', {})
