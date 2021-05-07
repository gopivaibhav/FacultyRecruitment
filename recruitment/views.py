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

def viewMore(request, application_number):
    return render(request, 'recruitment/view-more.html', {'data':Applicant.objects.filter(application_no=application_number)})

def submission_form(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # Applicant
        applicant_data = {}
        number = len(Applicant.objects.filter(date=datetime.datetime.now().date()))
        application_number = str(datetime.datetime.now().date())+str(number+1).zfill(3) 
        applicant_data['application_no'] = application_number
        applicant_data['date'] = datetime.datetime.now().date()
        applicant_data['advertisement_no'] = 'Rolling Advertisement No.1'
        applicant_data['post'] = data['AppPost']
        applicant_data['department'] = data['Dept']
        applicant_data['Research_Domain'] = data['research_domain']
        applicant_data['profile_picture'] = request.FILES['profile_photo']
        Applicant.objects.create(**applicant_data)
        # General
        general_data={}
        general_data['full_name'] = data['saluation'] + data['name'].strip()
        general_data['DOB'] = data['dateofbirth']
        general_data['father_name'] = data['fathername']
        general_data['address_perm'] = data['permanentaddress']
        general_data['telephone_perm'] = data['permanentpincode']
        general_data['pin_perm'] = data['permanenttelephone']
        general_data['address_mail'] = data['mailingaddress']
        general_data['telephone_mail'] = data['mailingtelephone']
        general_data['pin_mail'] = data['mailingpincode']
        general_data['mobile_number'] = data['mobilecode'] + data['mobile']
        general_data['email'] = data['email']
        general_data['gender'] = data['gender']
        general_data['marital_status'] = data['maritalstatus']
        general_data['nationality'] = data['nationality']
        general_data['state'] = data['domicile_state']
        general_data['category'] = data['category']
        general_data['reservation'] = data['reservation']
        general_data['reservation_certificate'] = request.FILES['reservation_certificate']
        general_data['present_employer'] = data['present_employer']
        general_data['applicant'] = Applicant.objects.get(application_no=application_number) 
        General.objects.create(**general_data)
        # Other Information
        otherinformation_data = {}
        otherinformation_data['membership'] = data['miscTa1']
        otherinformation_data['responsibilities'] = data['miscTa2']
        otherinformation_data['Any_other_relevant_information'] = data['miscTa3']
        otherinformation_data['academic_year_break'] = data['miscTa4']
        otherinformation_data['college_punishment'] = data['miscTa5']
        otherinformation_data['judicial_punishment'] = data['miscTa6']
        otherinformation_data['unfit_for_position'] = data['miscTa7']
        otherinformation_data['reference1'] = data['miscTa8']
        otherinformation_data['reference2'] = data['miscTa9']
        otherinformation_data['reference3'] = data['miscTa10']
        otherinformation_data['applicant'] = Applicant.objects.get(application_no=application_number) 
        OtherInfo.objects.create(**otherinformation_data)
        # Signature 
        signed_data= {}
        signed_data['place'] = data['signPlace']
        signed_data['date'] = data['signDate']
        signed_data['signature'] = request.FILES['signUpload']
        signed_data['applicant'] = Applicant.objects.get(application_no=application_number)
        Declaration.objects.create(**signed_data)
        # Page 4
        # Thesis
        thesis_data = {}
        thesis_data['ongoing_phd'] = data['ongoing_phd']
        thesis_data['completed_phd'] = data['completed_phd']
        thesis_data['applicant'] = Applicant.objects.get(application_no=application_number)
        Thesis.objects.create(**thesis_data)
        # Administrative Details
        administrative_details_data = {}
        administrative_details_data['administrative_details'] = data['administrative_details']
        administrative_details_data['applicant'] = Applicant.objects.get(application_no=application_number)
        AdministrativeDetails.objects.create(**administrative_details_data)
        # Patent
        patent_data = {}
        patent_data['patent_details'] = data['patent_details']
        patent_data['applicant'] = Applicant.objects.get(application_no=application_number)
        Patent.objects.create(**patent_data)
        # Summary
        summary_data = {}
        summary_data['defence_date'] = data['phd_defence_date']
        summary_data['total_exp'] = data['tot_exp']
        summary_data['exp_post_phd'] = data['exp_post_phd']
        summary_data['total_phd_students'] = data['total_phd_students']
        summary_data['ongoing_phd_supervision'] = data['ongoing_phd_supervision']
        summary_data['total_projects'] = data['total_projects']
        summary_data['ongoing_projects'] = data['ongoing_projects']
        summary_data['computational_projects'] = data['computational_projects']
        summary_data['SCI_journal'] = data['SCI_journal']
        summary_data['SCI_journal_post_phd'] = data['SCI_journal_post_phd']
        summary_data['applicant'] = Applicant.objects.get(application_no=application_number)
        Summary.objects.create(**summary_data)
        # Sponsored Projects
        sponsored_projects_data = {}
        sponsored_projects_data['spo_tot_number'] = data['spo_tot_number']
        sponsored_projects_data['spo_ongoing'] = data['spo_ongoing']
        sponsored_projects_data['spo_completed'] = data['spo_completed']
        sponsored_projects_data['spo_file'] = request.FILES['spofile']
        sponsored_projects_data['applicant'] = Applicant.objects.get(application_no=application_number)
        SponsoredProject.objects.create(**sponsored_projects_data)
        # Experiments
        experiments_data = {}
        experiments_data['exp_tot_number'] = data['exp_tot_number']
        experiments_data['exp_ongoing'] = data['exp_ongoing']
        experiments_data['exp_completed'] = data['exp_completed']
        experiments_data['exp_file'] = request.FILES['expfile']
        experiments_data['applicant'] = Applicant.objects.get(application_no=application_number)
        Experiments.objects.create(**experiments_data)
        # PHD
        phd_data = {}
        phd_data['PhD_awarded'] = data['awarded_phd']
        phd_data['title_of_thesis'] = data['phdThesis']
        phd_data['applicant'] = Applicant.objects.get(application_no=application_number)
        PhD.objects.create(**phd_data)
        # Academic Details
        num_of_academic_records = list(filter(lambda s: 'course' in s,list(data.keys())))
        num_of_academic_records_length = len(num_of_academic_records)
        last_academic_record = num_of_academic_records[num_of_academic_records_length-1]
        number_academic_record = last_academic_record[6]
        academic_data = []
        for i in range(1,int(number_academic_record)+1):
            if not 'course' + str(i):
                continue
            academic_details = {}
            academic_details['degree'] = data.get('course'+str(i),False)
            academic_details['name'] = data.get('course'+str(i)+'-name',False)
            academic_details['marks'] = data.get('course'+str(i)+'-percentage',False)
            academic_details['subjects'] = data.get('course'+str(i)+'-subject',False)
            academic_details['year_of_passing'] = data.get('yearOfPassing'+str(i),False)
            ans = 'course' + str(i) + '-file'
            academic_details['supporting_documents'] = request.FILES[ans]
            academic_details['applicant'] = Applicant.objects.get(application_no=application_number)
            EducationalQualifications.objects.create(**academic_details)
            # if re.search(r'[12]\d{3}',data.get('yearOfPassing-'+str(i),False)) is None:
            #     return render(request, 'recruitment/form.html',{'message':'Enter the year in Academic details in yyyy format.'})
            # if 0 <= float(data.get('course-'+str(i)+'-marks',False)) <= 100:
            #     academic_details['marks']  = data.get('course-'+str(i)+'-marks',False)
            # else:
            #     return render(request, 'recruitment/form.html',{'message':'Enter your percentage in Academic details a value between 0 to 100.'})
        # Professional
        num_of_professional_records = list(filter(lambda s: 'org' in s, list(data.keys())))
        last_professional_record = num_of_professional_records[len(num_of_professional_records)-1]
        number_professional_record = last_professional_record[3]
        for i in range(1,int(number_professional_record)+1):
            professional_details = {}
            professional_details['name'] = data.get('org' + str(i) + '-name',False)
            professional_details['post'] = data.get('org' + str(i) + '-post',False)
            professional_details['from_year'] = data.get('org' + str(i) + '-from',False)
            professional_details['to_year'] = data.get('org' + str(i) + '-to',False)
            professional_details['salary'] = data.get('org' + str(i) + '-salary',False)
            professional_details['nature'] = data.get('org' + str(i) + '-nature',False)
            ans = 'org' + str(i) + '-file'
            professional_details['supporting_documents'] = request.FILES[ans]
            professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
            EmploymentExp.objects.create(**professional_details)

        # Books
        num_of_books_records = list(filter(lambda s: 'books' in s, list(data.keys())))
        last_book_record = num_of_books_records[len(num_of_books_records)-1]
        number_books_record = last_book_record[5]
        books_data = []
        for i in range(1,int(number_books_record)+1):
            books_details = {}
            books_details['title'] = data.get('books' + str(i) + '-title',False)
            books_details['author'] = data.get('books' + str(i) + '-author',False)     
            books_details['publisher'] = data.get('books' + str(i) + '-publisher',False) 
            books_details['date_publish'] = data.get('books' + str(i) + '-date',False)
            books_details['isbn'] = data.get('books' + str(i) + '-number',False)
            ans = 'books' + str(i) + '-file'
            books_details['supporting_documents'] = request.FILES[ans]
            books_details['applicant'] = Applicant.objects.get(application_no=application_number)
            Books.objects.create(**books_details)
        # Chapters
        num_of_chapters_records = list(filter(lambda s: 'chapters' in s, list(data.keys())))
        last_chapter_record = num_of_chapters_records[len(num_of_chapters_records)-1]
        number_chapter_record = last_chapter_record[8]   
        for i in range(1,int(number_chapter_record)+1):
            chapter_details = {}
            chapter_details['book_title'] = data.get('chapters' + str(i) + '-book_title',False)
            chapter_details['chapter'] = data.get('chapters' + str(i) + '-chapter',False)    
            chapter_details['author'] = data.get('chapters' + str(i) + '-author',False)
            chapter_details['publisher'] = data.get('chapters' + str(i) + '-publisher',False)
            chapter_details['date_of_publisher'] = data.get('chapters' + str(i) + '-date_of_publisher',False)
            chapter_details['isbn_issn'] = data.get('chapters' + str(i) + '-number',False)
            chapter_details['supporting_documents'] = request.FILES['chapters'+str(i)+'-file']
            chapter_details['applicant'] = Applicant.objects.get(application_no=application_number)
            Chapters.objects.create(**chapter_details)
        # Newspapers Articles
        num_of_news_articles_records = list(filter(lambda s: 'news_articles' in s, list(data.keys())))
        last_news_articles_record = num_of_news_articles_records[len(num_of_news_articles_records)-1]
        number_news_articles_record = last_news_articles_record[13]
        for i in range(1, int(number_news_articles_record)+1):
            news_articles_details = {}
            news_articles_details['article_title'] = data.get('news_articles' + str(i) + '-article_title',False)
            news_articles_details['journal_name'] = data.get('news_articles' + str(i) + '-journal_name',False)
            news_articles_details['author'] = data.get('news_articles' + str(i) + '-author',False)
            news_articles_details['date_published'] = data.get('news_articles' + str(i) + '-date_published',False)
            news_articles_details['vol_no'] = data.get('news_articles' + str(i) + '-page')
            news_articles_details['referred'] = data.get('news_articles' + str(i) + '-referred',False)
            news_articles_details['naas'] = data.get('news_articles' + str(i) + '-impact',False)
            news_articles_details['supporting_documents'] = request.FILES['news_articles'+str(i)+'-file']
            news_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
            NewspaperArticle.objects.create(**news_articles_details)
        # Seminar Articles
        num_of_seminar_articles =  list(filter(lambda s: 'semi_articles' in s, list(data.keys())))
        last_semi_articles_record = num_of_seminar_articles[len(num_of_seminar_articles)-1]
        number_semi_articles_record = last_semi_articles_record[13]
        for i in range(1,int(number_semi_articles_record)+1):
            seminar_articles_details = {}
            seminar_articles_details['article_title'] = data.get('semi_articles' + str(i) + '-article_title',False)
            seminar_articles_details['seminar_subject'] = data.get('semi_articles' + str(i) + '-seminar_subject',False)
            seminar_articles_details['location'] = data.get('semi_articles' + str(i) + '-location',False)
            seminar_articles_details['From'] = data.get('semi_articles' + str(i) + '-from',False)
            seminar_articles_details['to'] = data.get('semi_articles' + str(i) + 'to',False)
            seminar_articles_details['published'] = data.get('semi_articles' + str(i) + '-published',False)
            ans = 'semi_articles'+str(i)+'-file'
            seminar_articles_details['supporting_documents'] = request.FILES[ans]
            seminar_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
            SeminarArticles.objects.create(**seminar_articles_details)

        # Research Experience
        num_of_research_exp = list(filter(lambda s: 'exper' in s, list(data.keys())))
        last_research_exp_record = num_of_research_exp[len(num_of_research_exp) - 1]
        number_research_exp_record = last_research_exp_record[5]
        for i in range(1,int(number_research_exp_record)):
            research_exp_details = {}
            research_exp_details['From'] = data.get('exper' + str(i) + '-from')
            research_exp_details['to'] = data.get('exper' + str(i) + '-to')
            research_exp_details['number_of_months'] = data.get('exper' + str(i) + '-month')
            ans = 'exper' + str(i) + '-file'
            research_exp_details['supporting_documents'] = request.FILES[ans]
            research_exp_details['applicant'] = Applicant.objects.get(application_no=application_number)
            ResearchExp.objects.create(**research_exp_details)
                             
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
        # Applicant.objects.create(**applicant_data)
        # academic_detail['applicant'] = Applicant.objects.get(application_no=application_number)
        # for academic_detail in academic_data:
        #     EducationalQualifications.objects.create(**academic_detail)
        
        # professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # for professional_details in professional_data:
        #     EmploymentExp.objects.create(**professional_details) 
        # books_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # for books_details in books_data:
        #     Books.objects.create(**books_details)
        # chapter_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # for chapter_details in chapters_data:
        #     Chapters.objects.create(**chapter_details)
        # news_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # for news_articles_details in news_articles_data:
        #     NewspaperArticle.objects.create(**news_articles_details)
        # seminar_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
        # for seminar_articles_details in seminar_articles_data:
        #     SeminarArticles.objects.create(**seminar_articles_details)    
        return render(request, 'recruitment/form.html',{'message':'Congrats! Your application number is '+ application_number})
    return render(request, 'recruitment/form.html', {})
