from django.shortcuts import render
import datetime
import  re
from recruitment.models import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def error404(request,exception):
    return render(request, 'recruitment/error404.html', {});
def handler404(request):
    response = render_to_response('recruitment/error404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def adminLogin(request):
    context = {
        'could_not_log_in': False,
    }
    if(request.method == 'POST'):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if(user is not None and user.is_superuser == 1):
            login(request,user)
            return HttpResponseRedirect('profile/')
        else:
            context = {
                'could_not_log_in': True,
            }
    return render(request,'recruitment/login.html',context)

def profile(request):
    if(request.user.is_superuser == 1):
        return HttpResponseRedirect('/admin/')
    return render(request,'recruitment/profile.html',{})

def home(request):
    return render(request, 'recruitment/index.html',{})

def admin(request):
    if(request.user.is_superuser != 1):
        return HttpResponseRedirect('/')
    admin_data = {}
    appli_data = []
    for i in list(General.objects.all()):
        presAppli = {}
        presAppli['application_no'] = (i.applicant)
        presAppli['applicant_name'] = (i.full_name)
        presAppli['applied_post'] = Applicant.objects.filter(application_no=i.applicant)[0].post
        presAppli['applied_department'] = Applicant.objects.filter(application_no=i.applicant)[0].department
        presAppli['applied_date'] = Applicant.objects.filter(application_no=i.applicant)[0].date
        appli_data.append(presAppli)
    admin_data['allData'] = appli_data
    print(admin_data)
    return render(request, 'recruitment/admin.html', {'data' :admin_data})

def viewMore(request, application_number):
    # print (list(EmploymentExp.objects.filter(applicant=application_number)))
    return render(request, 'recruitment/view-more.html', {
        'applicant_data': {
            'application_number': application_number,
            'date' : Applicant.objects.filter(application_no=application_number)[0].date,
            'post': Applicant.objects.filter(application_no=application_number)[0].post,
            'department': Applicant.objects.filter(application_no=application_number)[0].department,
            'reserach_domain': Applicant.objects.filter(application_no=application_number)[0].Research_Domain,
            'profile_photo': Applicant.objects.filter(application_no=application_number)[0].profile_picture
        },
        'general_data': {
            'full_name': General.objects.filter(applicant=application_number)[0].full_name,
            'DOB': General.objects.filter(applicant=application_number)[0].DOB,
            'father_name': General.objects.filter(applicant=application_number)[0].father_name,
            'address_perm': General.objects.filter(applicant=application_number)[0].address_perm,
            'telephone_perm': General.objects.filter(applicant=application_number)[0].telephone_perm,
            'pin_perm': General.objects.filter(applicant=application_number)[0].pin_perm,
            'address_mail': General.objects.filter(applicant=application_number)[0].address_mail,
            'telephone_mail': General.objects.filter(applicant=application_number)[0].telephone_mail,
            'pin_mail': General.objects.filter(applicant=application_number)[0].pin_mail,
            'mobile_number': General.objects.filter(applicant=application_number)[0].mobile_number,
            'email': General.objects.filter(applicant=application_number)[0].email,
            'gender': General.objects.filter(applicant=application_number)[0].gender,
            'marital_status': General.objects.filter(applicant=application_number)[0].marital_status,
            'nationality': General.objects.filter(applicant=application_number)[0].nationality,
            'state': General.objects.filter(applicant=application_number)[0].state,
            'category': General.objects.filter(applicant=application_number)[0].category,
            'reservation': General.objects.filter(applicant=application_number)[0].reservation,
            'certificate': General.objects.filter(applicant=application_number)[0].reservation_certificate,
            'employer': General.objects.filter(applicant=application_number)[0].present_employer
        },
        'otherinformation_data': {
            'membership': OtherInfo.objects.filter(applicant=application_number)[0].membership,
            'responsibilities': OtherInfo.objects.filter(applicant=application_number)[0].responsibilities,
            'Any_other_relevant_information': OtherInfo.objects.filter(applicant=application_number)[0].Any_other_relevant_information,
            'academic_year_break': OtherInfo.objects.filter(applicant=application_number)[0].academic_year_break,
            'college_punishment': OtherInfo.objects.filter(applicant=application_number)[0].college_punishment,
            'judicial_punishment': OtherInfo.objects.filter(applicant=application_number)[0].judicial_punishment,
            'unfit_for_position': OtherInfo.objects.filter(applicant=application_number)[0].unfit_for_position,
            'reference1': OtherInfo.objects.filter(applicant=application_number)[0].reference1,
            'reference2': OtherInfo.objects.filter(applicant=application_number)[0].reference2,
            'reference3': OtherInfo.objects.filter(applicant=application_number)[0].reference3,
        },
        'signed_data': {
            'place': Declaration.objects.filter(applicant=application_number)[0].place,
            'date': Declaration.objects.filter(applicant=application_number)[0].date,
            'signature': Declaration.objects.filter(applicant=application_number)[0].signature,
        },
        'thesis_data': {
            'ongoing_phd': Thesis.objects.filter(applicant=application_number)[0].ongoing_phd,
            'completed_phd': Thesis.objects.filter(applicant=application_number)[0].completed_phd
        },
        'administrative_details_data': {
            'administrative_details': AdministrativeDetails.objects.filter(applicant=application_number)[0].administrative_details
        },
        'Summary': {
            'defence_date': Summary.objects.filter(applicant=application_number)[0].defence_date,
            'total_exp': Summary.objects.filter(applicant=application_number)[0].total_exp,
            'exp_post_phd': Summary.objects.filter(applicant=application_number)[0].exp_post_phd,
            'total_phd_students': Summary.objects.filter(applicant=application_number)[0].total_phd_students,
            'ongoing_phd_supervision': Summary.objects.filter(applicant=application_number)[0].ongoing_phd_supervision,
            'total_projects': Summary.objects.filter(applicant=application_number)[0].total_projects,
            'ongoing_projects': Summary.objects.filter(applicant=application_number)[0].ongoing_projects,
            'computational_projects': Summary.objects.filter(applicant=application_number)[0].computational_projects,
            'SCI_journal': Summary.objects.filter(applicant=application_number)[0].SCI_journal,
            'SCI_journal_post_phd': Summary.objects.filter(applicant=application_number)[0].SCI_journal_post_phd
        },
        'Patent': {
            'patent_details': Patent.objects.filter(applicant=application_number)[0].patent_details,
        },
        'SponsoredProjects': {
            'spo_tot_number': SponsoredProject.objects.filter(applicant=application_number)[0].spo_tot_number,
            'spo_ongoing': SponsoredProject.objects.filter(applicant=application_number)[0].spo_ongoing,
            'spo_completed': SponsoredProject.objects.filter(applicant=application_number)[0].spo_completed,
            'spo_file': SponsoredProject.objects.filter(applicant=application_number)[0].spo_file,
        },
        'Experiments': {
            'exp_tot_number': Experiments.objects.filter(applicant=application_number)[0].exp_tot_number,
            'exp_ongoing': Experiments.objects.filter(applicant=application_number)[0].exp_ongoing,
            'exp_completed': Experiments.objects.filter(applicant=application_number)[0].exp_completed,
            'exp_file': Experiments.objects.filter(applicant=application_number)[0].exp_file
        },
        'PhD': {
            'PhD_awarded': PhD.objects.filter(applicant=application_number)[0].PhD_awarded,
            'title_of_thesis': PhD.objects.filter(applicant=application_number)[0].title_of_thesis,
        },
        'AcademicDetails': list(EducationalQualifications.objects.filter(applicant=application_number)),
        'ProfessionalDetails': list(EmploymentExp.objects.filter(applicant=application_number)),
        'BooksDetails': list(Books.objects.filter(applicant=application_number)),
        'ChaptersDetails': list(Chapters.objects.filter(applicant=application_number)),
        'NewspapersArticlesDetails': list(NewspaperArticle.objects.filter(applicant=application_number)),
        'SeminarArticles': list(SeminarArticles.objects.filter(applicant=application_number)),
        'ResearchExperienceDetails': list(ResearchExp.objects.filter(applicant=application_number))
    })

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
        general_data['pin_perm'] = data['permanentpincode']
        general_data['telephone_perm'] = data['permanenttelephone']
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
        if(data.get('reservation') == 'YES'):
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
        signed_data['date'] = datetime.datetime.now().date()
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
        if(data.get('spo_tot_number') != "0"):
            sponsored_projects_data['spo_file'] = request.FILES['spofile']
        else:
            sponsored_projects_data['spo_file'] = "N/A"
        sponsored_projects_data['applicant'] = Applicant.objects.get(application_no=application_number)
        SponsoredProject.objects.create(**sponsored_projects_data)
        # Experiments
        experiments_data = {}
        experiments_data['exp_tot_number'] = data['exp_tot_number']
        experiments_data['exp_ongoing'] = data['exp_ongoing']
        experiments_data['exp_completed'] = data['exp_completed']
        if(data.get('exp_tot_number') != "0"):
            experiments_data['exp_file'] = request.FILES['expfile']
        else:
            experiments_data['exp_file'] = "N/A"
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
        for i in range(1,int(number_academic_record)+1):
            if (data.get('course'+str(i),False) == False):
                continue
            else:
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
            if (data.get('org' + str(i) + '-name') == ""):
                professional_details = {}
                professional_details['name'] = "N/A"
                professional_details['post'] = "N/A"
                professional_details['from_year'] = "N/A"
                professional_details['to_year'] = "N/A"
                professional_details['salary'] = "N/A"
                professional_details['nature'] = "N/A"
                professional_details['supporting_documents'] = "N/A"
                professional_details['applicant'] = Applicant.objects.get(application_no=application_number)
                EmploymentExp.objects.create(**professional_details)
            else:
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
        # books_data = []
        for i in range(1,int(number_books_record)+1):
            if(data.get('books' + str(i) + '-title') == ""):
                books_details = {}
                books_details['title'] = "N/A"
                books_details['author'] =  "N/A"   
                books_details['publisher'] = "N/A"
                books_details['date_publish'] = "N/A"
                books_details['isbn'] = "N/A"
                books_details['supporting_documents'] = "N/A"
                books_details['applicant'] = Applicant.objects.get(application_no=application_number)
                Books.objects.create(**books_details)
            else:
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
            if(data.get('chapters' + str(i) + '-book_title') == ""):
                chapter_details = {}
                chapter_details['book_title'] = "N/A"
                chapter_details['chapter'] = "N/A"
                chapter_details['author'] = "N/A"
                chapter_details['publisher'] = "N/A"
                chapter_details['date_of_publisher'] = "N/A" 
                chapter_details['isbn_issn'] = "N/A"
                chapter_details['supporting_documents'] = "N/A"
                chapter_details['applicant'] = Applicant.objects.get(application_no=application_number)
                Chapters.objects.create(**chapter_details)
            else:
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
            if(data.get('news_articles' + str(i) + '-article_title') == ""):
                news_articles_details = {}
                news_articles_details['article_title'] = "N/A"
                news_articles_details['journal_name'] = "N/A"
                news_articles_details['author'] = "N/A"
                news_articles_details['date_published'] = "N/A"
                news_articles_details['vol_no'] = "N/A"
                news_articles_details['referred'] = "N/A"
                news_articles_details['naas'] = "N/A"
                news_articles_details['supporting_documents'] = "N/A"
                news_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
                NewspaperArticle.objects.create(**news_articles_details)
            else:
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
            if(data.get('semi_articles' + str(i) + '-article_title') == ""):
                seminar_articles_details = {}
                seminar_articles_details['article_title'] = "N/A"
                seminar_articles_details['seminar_subject'] = "N/A"
                seminar_articles_details['location'] = "N/A"
                seminar_articles_details['From'] = "N/A"
                seminar_articles_details['to'] = "N/A"
                seminar_articles_details['published'] = "N/A"
                seminar_articles_details['supporting_documents'] = "N/A"
                seminar_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
                SeminarArticles.objects.create(**seminar_articles_details)
            else:
                seminar_articles_details = {}
                seminar_articles_details['article_title'] = data.get('semi_articles' + str(i) + '-article_title',False)
                seminar_articles_details['seminar_subject'] = data.get('semi_articles' + str(i) + '-seminar_subject',False)
                seminar_articles_details['location'] = data.get('semi_articles' + str(i) + '-location',False)
                seminar_articles_details['From'] = data.get('semi_articles' + str(i) + '-from',False)
                seminar_articles_details['to'] = data.get('semi_articles' + str(i) + '-to',False)
                seminar_articles_details['published'] = data.get('semi_articles' + str(i) + '-published',False)
                seminar_articles_details['supporting_documents'] = "N/A"
                seminar_articles_details['applicant'] = Applicant.objects.get(application_no=application_number)
                SeminarArticles.objects.create(**seminar_articles_details)
        # Research Experience
        num_of_research_exp = list(filter(lambda s: 'exper' in s, list(data.keys())))
        last_research_exp_record = num_of_research_exp[len(num_of_research_exp) - 1]
        number_research_exp_record = last_research_exp_record[5]
        for i in range(1,int(number_research_exp_record)+1):
            if(data.get('exper' + str(i) + '-from') == ""):
                research_exp_details = {}
                research_exp_details['From'] = "N/A"
                research_exp_details['to'] = "N/A"
                research_exp_details['number_of_months'] = "N/A"
                research_exp_details['supporting_documents'] = "N/A"
                research_exp_details['applicant'] = Applicant.objects.get(application_no=application_number)
                ResearchExp.objects.create(**research_exp_details)
            else:
                research_exp_details = {}
                research_exp_details['From'] = data.get('exper' + str(i) + '-from',False)
                research_exp_details['to'] = data.get('exper' + str(i) + '-to',False)
                research_exp_details['number_of_months'] = data.get('exper' + str(i) + '-months',False)
                ans = 'exper' + str(i) + '-file'
                research_exp_details['supporting_documents'] = request.FILES[ans]
                research_exp_details['applicant'] = Applicant.objects.get(application_no=application_number)
                ResearchExp.objects.create(**research_exp_details)                      
        return HttpResponseRedirect('/accounts/profile/')
    return render(request, 'recruitment/form.html', {})
