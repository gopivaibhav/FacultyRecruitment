from time import process_time_ns
from django.shortcuts import render, redirect
import datetime, sys

from django.utils.timezone import activate
from recruitment.models import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
import csv

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail

from django.http import HttpResponse
from django.urls import reverse

from .utils import render_to_pdf  # created in step 4


def getData(application_number):
    return {
                'applicant_data': {
                    'application_number': (application_number).strip(),
                    'date': (Applicant.objects.filter(application_no=application_number)[0].date),
                    'post': (Applicant.objects.filter(application_no=application_number)[0].post).strip(),
                    'department': (Applicant.objects.filter(application_no=application_number)[0].department).strip(),
                    'reserach_domain': (Applicant.objects.filter(application_no=application_number)[0].Research_Domain).strip(),
                    'profile_photo': (Applicant.objects.filter(application_no=application_number)[0].profile_picture)
                },
                'general_data': {
                    'full_name': (General.objects.filter(applicant=application_number)[0].full_name).strip() or "N/A",
                    'DOB': (General.objects.filter(applicant=application_number)[0].DOB),
                    'father_name': (General.objects.filter(applicant=application_number)[0].father_name).strip(),
                    'address_perm': (General.objects.filter(applicant=application_number)[0].address_perm).strip(),
                    'telephone_perm': (General.objects.filter(applicant=application_number)[0].telephone_perm).strip() or "N/A",
                    'pin_perm': (General.objects.filter(applicant=application_number)[0].pin_perm).strip(),
                    'address_mail': (General.objects.filter(applicant=application_number)[0].address_mail).strip(),
                    'telephone_mail': (General.objects.filter(applicant=application_number)[0].telephone_mail).strip() or "N/A",
                    'pin_mail': (General.objects.filter(applicant=application_number)[0].pin_mail).strip(),
                    'mobile_code': (General.objects.filter(applicant=application_number)[0].mobile_code).strip(),                    
                    'mobile_number': (General.objects.filter(applicant=application_number)[0].mobile_number).strip(),
                    'email': (General.objects.filter(applicant=application_number)[0].email).strip(),
                    'gender': (General.objects.filter(applicant=application_number)[0].gender).strip(),
                    'marital_status': (General.objects.filter(applicant=application_number)[0].marital_status).strip(),
                    'nationality': (General.objects.filter(applicant=application_number)[0].nationality).strip(),
                    'state': (General.objects.filter(applicant=application_number)[0].state).strip(),
                    'category': (General.objects.filter(applicant=application_number)[0].category).strip(),
                    'reservation': (General.objects.filter(applicant=application_number)[0].reservation).strip(),
                    'certificate': (General.objects.filter(applicant=application_number)[0].reservation_certificate),
                },
                'otherinformation_data': {
                    'membership': OtherInfo.objects.filter(applicant=application_number)[0].membership,
                    'responsibilities': OtherInfo.objects.filter(applicant=application_number)[0].responsibilities,
                    'Any_other_relevant_information': OtherInfo.objects.filter(applicant=application_number)[0].Any_other_relevant_information,
                    'academic_year_break': OtherInfo.objects.filter(applicant=application_number)[0].academic_year_break,
                    # 'college_punishment': OtherInfo.objects.filter(applicant=application_number)[0].college_punishment,
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
                    'resume': Declaration.objects.filter(applicant=application_number)[0].resume,
                    'receipt': Declaration.objects.filter(applicant=application_number)[0].receipt,
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
                    'PhD_details': PhD.objects.filter(applicant=application_number)[0].PhD_details
                },
                'PhDOngoing': {
                    'PhD_title': PhDOngoing.objects.filter(applicant=application_number)[0].PhD_title,
                    'Research_Domain': PhDOngoing.objects.filter(applicant=application_number)[0].Research_Domain,
                    'Institute_Name': PhDOngoing.objects.filter(applicant=application_number)[0].Institute_Name,
                    'University_Name': PhDOngoing.objects.filter(applicant=application_number)[0].University_Name,
                    'Registration_Date': PhDOngoing.objects.filter(applicant=application_number)[0].Registration_Date,
                },
                'ThesisSubmitted': list(ThesisSubmitted.objects.filter(applicant=application_number)),
                'PhDAwarded': list(PhDAwarded.objects.filter(applicant=application_number)),
                'AcademicDetails': list(EducationalQualifications.objects.filter(applicant=application_number)),
                'ProfessionalDetails': list(EmploymentExp.objects.filter(applicant=application_number)),
                'BooksDetails': list(Books.objects.filter(applicant=application_number)),
                'ChaptersDetails': list(Chapters.objects.filter(applicant=application_number)),
                'NewspapersArticlesDetails': list(NewspaperArticle.objects.filter(applicant=application_number)),
                'SeminarArticles': list(SeminarArticles.objects.filter(applicant=application_number)),
                'ResearchExperienceDetails': list(ResearchExp.objects.filter(applicant=application_number))
            }

def generate_pdf(request,application_number, *args, **kwargs):
    # application_number = "2021-12-06009"; # for testing purpose
    # print(application_number, Applicant.objects.filter(application_no=application_number)[0].post)
    try:
        if request.user.is_anonymous:
            return HttpResponseRedirect('/')
        elif General.objects.filter(applicant=application_number)[0].email != request.user.email:
            return HttpResponseRedirect('/accounts/profile')
        elif not General.objects.filter(applicant=application_number)[0].is_completed:
            # print(list(EducationalQualifications.objects.filter(applicant=application_number)),sep='\n');
            sendData = {
                    'application_number': (application_number).strip(),
                    'date': (Applicant.objects.filter(application_no=application_number)[0].date),
                    'post': (Applicant.objects.filter(application_no=application_number)[0].post).strip(),
                    'department': (Applicant.objects.filter(application_no=application_number)[0].department).strip(),
                    'reserach_domain': (Applicant.objects.filter(application_no=application_number)[0].Research_Domain).strip(),
                    'profile_photo': (Applicant.objects.filter(application_no=application_number)[0].profile_picture),
                    'doctorate':(General.objects.filter(applicant=application_number)[0].full_name.split()[0]) or 'N/A',
                    'full_name': ' '.join(General.objects.filter(applicant=application_number)[0].full_name.split()[1:]) or "N/A",
                    'DOB': (General.objects.filter(applicant=application_number)[0].DOB).strftime('%Y-%m-%d'),
                    'father_name': (General.objects.filter(applicant=application_number)[0].father_name).strip(),
                    'address_perm': (General.objects.filter(applicant=application_number)[0].address_perm).strip(),
                    'telephone_perm': (General.objects.filter(applicant=application_number)[0].telephone_perm).strip() or "N/A",
                    'pin_perm': (General.objects.filter(applicant=application_number)[0].pin_perm).strip(),
                    'address_mail': (General.objects.filter(applicant=application_number)[0].address_mail).strip(),
                    'telephone_mail': (General.objects.filter(applicant=application_number)[0].telephone_mail).strip() or "N/A",
                    'pin_mail': (General.objects.filter(applicant=application_number)[0].pin_mail).strip(),
                    'mobile_code':(General.objects.filter(applicant=application_number)[0].mobile_code).strip(),
                    'mobile_number': (General.objects.filter(applicant=application_number)[0].mobile_number).strip(),
                    'email': (General.objects.filter(applicant=application_number)[0].email).strip(),
                    'gender': (General.objects.filter(applicant=application_number)[0].gender).strip(),
                    'marital_status': (General.objects.filter(applicant=application_number)[0].marital_status).strip(),
                    'nationality': (General.objects.filter(applicant=application_number)[0].nationality).strip(),
                    'state': (General.objects.filter(applicant=application_number)[0].state).strip(),
                    'category': (General.objects.filter(applicant=application_number)[0].category).strip(),
                    'reservation': (General.objects.filter(applicant=application_number)[0].reservation).strip(),
                    'certificate': (General.objects.filter(applicant=application_number)[0].reservation_certificate),
                    'AcademicDetails': list(EducationalQualifications.objects.filter(applicant=application_number)),
                    'ProfessionalDetails': list(EmploymentExp.objects.filter(applicant=application_number)),
                    'ResearchExperienceDetails': list(ResearchExp.objects.filter(applicant=application_number)),
                    'BooksDetails': list(Books.objects.filter(applicant=application_number)),
                    'ChaptersDetails': list(Chapters.objects.filter(applicant=application_number)),
                    'NewspapersArticlesDetails': list(NewspaperArticle.objects.filter(applicant=application_number)),
                    'SeminarArticles': list(SeminarArticles.objects.filter(applicant=application_number)),
                    'ongoing_phd': Thesis.objects.filter(applicant=application_number)[0].ongoing_phd,
                    'completed_phd': Thesis.objects.filter(applicant=application_number)[0].completed_phd,
                    'administrative_details': AdministrativeDetails.objects.filter(applicant=application_number)[0].administrative_details,
                    'ThesisSubmitted': list(ThesisSubmitted.objects.filter(applicant=application_number)),
                    'PhDAwarded': list(PhDAwarded.objects.filter(applicant=application_number)),
                    'PhDOngoing': list(PhDOngoing.objects.filter(applicant=application_number)),
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
                    'Patent': {
                        'patent_details': Patent.objects.filter(applicant=application_number)[0].patent_details,
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
                    'otherinformation_data': {
                        'membership': OtherInfo.objects.filter(applicant=application_number)[0].membership,
                        'responsibilities': OtherInfo.objects.filter(applicant=application_number)[0].responsibilities,
                        'Any_other_relevant_information': OtherInfo.objects.filter(applicant=application_number)[0].Any_other_relevant_information,
                        'academic_year_break': OtherInfo.objects.filter(applicant=application_number)[0].academic_year_break,
                        'judicial_punishment': OtherInfo.objects.filter(applicant=application_number)[0].judicial_punishment,
                        'unfit_for_position': OtherInfo.objects.filter(applicant=application_number)[0].unfit_for_position,
                        'awards_and_recognition': OtherInfo.objects.filter(applicant=application_number)[0].awards_and_recognition,
                        'reference1': OtherInfo.objects.filter(applicant=application_number)[0].reference1,
                        'reference2': OtherInfo.objects.filter(applicant=application_number)[0].reference2,
                        'reference3': OtherInfo.objects.filter(applicant=application_number)[0].reference3,
                    },
                    'signed_data': {
                        'place': Declaration.objects.filter(applicant=application_number)[0].place,
                        'date': Declaration.objects.filter(applicant=application_number)[0].date,
                        'signature': Declaration.objects.filter(applicant=application_number)[0].signature,
                        'resume': Declaration.objects.filter(applicant=application_number)[0].resume,
                        'payment_id' : Declaration.objects.filter(applicant=application_number)[0].payment_id,
                        'receipt': Declaration.objects.filter(applicant=application_number)[0].receipt,
                    }
                }
            if(PhD.objects.filter(applicant=application_number).count() != 0):
                sendData['PhD'] = {
                    'PhD_awarded': PhD.objects.filter(applicant=application_number)[0].PhD_awarded,
                    'PhD_details': PhD.objects.filter(applicant=application_number)[0].PhD_details
                }
            # if(PhDOngoing.objects.filter(applicant=application_number).count() != 0):
            #     sendData['PhDOngoing'] = {
            #         'PhD_title': PhDOngoing.objects.filter(applicant=application_number)[0].PhD_title,
            #         'Research_Domain': PhDOngoing.objects.filter(applicant=application_number)[0].Research_Domain,
            #         'Institute_Name': PhDOngoing.objects.filter(applicant=application_number)[0].Institute_Name,
            #         'University_Name': PhDOngoing.objects.filter(applicant=application_number)[0].University_Name,
            #         'Registration_Date': PhDOngoing.objects.filter(applicant=application_number)[0].Registration_Date,
            #                             'PhD_title': PhDOngoing.objects.filter(applicant=application_number)[0].PhD_title,
            #         'Research_Domain': PhDOngoing.objects.filter(applicant=application_number)[0].Research_Domain,
            #         'Institute_Name': PhDOngoing.objects.filter(applicant=application_number)[0].Institute_Name,
            #         'University_Name': PhDOngoing.objects.filter(applicant=application_number)[0].University_Name,
            #         'Registration_Date': PhDOngoing.objects.filter(applicant=application_number)[0].Registration_Date,
            #     }
            if(len(sendData['AcademicDetails']) == 0):
                sendData['counter'] = [1, 2, 3, 4]
            return render(request, 'recruitment/editForm.html', sendData)
        else:
            pdf = render_to_pdf('recruitment/pdfTest.html', getData(application_number))
            print(getData('2023-02-27001')['applicant_data']['profile_photo'])
            return HttpResponse(pdf, content_type='application/pdf')
    except:
        if request.user.is_anonymous:
            return HttpResponseRedirect('/')
        else: 
            print(sys.exc_info())
            return render(request, 'recruitment/profile.html', {"messages":["No access to view other applications"]})
    

# def mail(request):
#     subject = "Alert! Someone is trying to login as admin at Faculty Recruitment Portal"
#     msg     = 'This is an auto generated message.\n\nIt is to inform you that someone is trying to login as admin at Faculty Recruitment Portal and failed three times!' + '\nkindly, secure your server!\n'
#     to      = 'lcs2020014@iiitl.ac.in'
#     res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
#     # if(res == 1):
#     #     msg = "Mail Sent Successfully"
#     # else:
#     #     msg = "Mail could not sent"
#     # return HttpResponse(msg)
#     return HttpResponseRedirect('/admin/')


def error404(request, exception):
    return render(request, 'recruitment/error404.html', {})


def loginPage(request):
    return render(request, 'account/login.html', {})


# def handler404(request):
#     response = render_to_response('recruitment/error404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Recruitment' + \
        str(datetime.datetime.now()) + '.csv'
    writer = csv.writer(response)
    heading_data = ['Application_number',
                    'Post',
                    'Department',
                    'Research Domain',
                    'Full Name',
                    'Date of Birth',
                    'Father\'s Name',
                    'Address',
                    'Pin Code',
                    'Telephone No.',
                    'Country Code'
                    'Mobile No.',
                    'Email ID',
                    'Gender',
                    'Marital Status',
                    'Nationality',
                    'Category',
                    'Reservation Claimed',
                    'Reservation Certificate',
                    'PhD Awarded',
                    'PhD Status',
                    'Title of Ongoing PhD',
                    'Research Domain of Ongoing PhD',
                    'Institute Name of Ongoing PhD',
                    'University Name of Ongoing PhD',
                    'Registration Date of Ongoing PhD',
                    'Supporting Documents of Ongoing PhD',
                    ]
    heading_data.append('Total Number of Thesis Submitted')
    for i in range(1, 6):
        heading_data.append('Title of Thesis Submitted- ' + str(i))
        heading_data.append('Research Domain of Thesis Submitted- ' + str(i))
        heading_data.append('Institute Name of Thesis Submitted- ' + str(i))
        heading_data.append('University Name of Thesis Submitted- ' + str(i))
        heading_data.append('Registration Date of Thesis Submitted- ' + str(i))
        heading_data.append('Submission Date of Thesis Submitted- ' + str(i))
        heading_data.append(
            'Supporting Documents of Thesis Submitted- ' + str(i))

     # Awarded phd's columns
    heading_data.append('Total NUmber of PhD\'s Awarded')
    for i in range(1, 6):
        heading_data.append('Title of Awarded PhD- ' + str(i))
        heading_data.append('Research Domain of Awarded PhD- ' + str(i))
        heading_data.append('Institute Name of Awarded PhD- ' + str(i))
        heading_data.append('University Name of Awarded PhD- ' + str(i))
        heading_data.append('Registration Date of Awarded PhD- ' + str(i))
        heading_data.append('Defense Date of Awarded PhD- ' + str(i))
        heading_data.append('Supporting Documents of Awarded PhD- ' + str(i))

    # Education Qualifications columns
    heading_data += [
        'Institute / University Name - X or equivalent',
        'Percentage / CGPA(10) / GPA(5) - X or equivalent',
        'Subjects Taken - X or equivalent',
        'Year of Passing - X or equivalent',
        'Supporting Documents - X or Equivalent',

        'Institute / University Name - XII or equivalent',
        'Percentage / CGPA(10) / GPA(5) - XII or equivalent',
        'Subjects Taken - XII or equivalent',
        'Year of Passing - XII or equivalent',
        'Supporting Documents - XII or Equivalent',

        'Institute / University Name - Bachelor\'s Degree or equivalent',
        'Percentage / CGPA(10) / GPA(5) - Bachelor\'s Degree or equivalent',
        'Subjects Taken - Bachelor\'s Degree or equivalent',
        'Year of Passing - Bachelor\'s Degree or equivalent',
        'Supporting Documents - Bachelor\'s Degree or Equivalent',

        'Institute / University Name - Master\'s Degree or equivalent',
        'Percentage / CGPA(10) / GPA(5) - Master\'s Degree or equivalent',
        'Subjects Taken - Master\'s Degree or equivalent',
        'Year of Passing - Master\'s Degree or equivalent',
        'Supporting Documents - Master\'s Degree or Equivalent',
    ]

    for i in range(1, 6):
        heading_data.append(
            'Name of Employer/Status of Institute/University- ' + str(i))
        heading_data.append('Post held/Designation- ' + str(i))
        heading_data.append('Period Of Employment From- ' + str(i))
        heading_data.append('Period Of Employment To- ' + str(i))
        heading_data.append('Basic Salary- ' + str(i))
        heading_data.append('Nature of Duty- ' + str(i))
        heading_data.append('Supporting Documents- ' + str(i))
    for i in range(1, 6):
        heading_data.append('Research Experience- ' + str(i) + 'From')
        heading_data.append('Research Experience- ' + str(i) + 'To')
        heading_data.append('Research Experience- ' +
                            str(i) + 'Number of Months')
        heading_data.append('Research Experience- ' +
                            str(i) + 'Supporting Documents')
    for i in range(1, 6):
        heading_data.append('Title of the Book- ' + str(i))
        heading_data.append(
            'Whether First Author or Co-author of Book- ' + str(i))
        heading_data.append('Name of Publisher of Book- ' + str(i))
        heading_data.append('Month & year of publication of Book- ' + str(i))
        heading_data.append('ISBN/ISSN No. of Book- ' + str(i))
        heading_data.append('Supporting Documents of Book- ' + str(i))
    for i in range(1, 6):
        heading_data.append('Title of the Chapter- ' + str(i))
        heading_data.append('Title of the Book- ' + str(i))
        heading_data.append(
            'Whether First Author or Co-author of Chapter- ' + str(i))
        heading_data.append('Name of Publisher of Chapter- ' + str(i))
        heading_data.append(
            'Month & year of publication of Chapter- ' + str(i))
        heading_data.append('ISBN/ISSN No. of Chapter- ' + str(i))
        heading_data.append('Supporting Documents of Chapter- ' + str(i))
    for i in range(1, 6):
        heading_data.append(
            'Title of research article/paper published in Journal- ' + str(i))
        heading_data.append('Name of journal- ' + str(i))
        heading_data.append(
            'Whether First Author or Co-author of research article/paper published in Journal- ' + str(i))
        heading_data.append(
            'Date Of Issue  of research article/paper published in Journal-- ' + str(i))
        heading_data.append(
            'Volume no. & Page nos.  of research article/paper published in Journal-- ' + str(i))
        heading_data.append(
            'Whether Referred/Non-referred  of research article/paper published in Journal-- ' + str(i))
        heading_data.append(
            'Impact Factor  of research article/paper published in Journal-- ' + str(i))
        heading_data.append(
            'Supporting Documents  of research article/paper published in Journal-- ' + str(i))
    for i in range(1, 6):
        heading_data.append(
            'Title/Subject of paper presented in Seminar- ' + str(i))
        heading_data.append(
            'Subject of Conference /Seminar/Symposium/ Workshop  presented in Seminar- -  ' + str(i))
        heading_data.append(
            'Organizing Institution & Name of City/Country presented in Seminar- ' + str(i))
        heading_data.append(
            'Starting Date of research article/paper presented in Seminar- ' + str(i))
        heading_data.append(
            'Ending Date of research article/paper presented in Seminar- ' + str(i))
        heading_data.append(
            'Whether the proceedings published or not presented in Seminar- ' + str(i))
        heading_data.append(
            'Supporting Documents presented in Seminar- ' + str(i))
    heading_data += [
        'Number of Ongoing PhDs',
        'Number of Completed PhDs',
        'Enter the details of Administrative Positions held in the past 5 years',
        'Total number of sponsored projects',
        'Number of ongoing sponsored projects',
        'Number of completed sponsored projects',
        'Supporting Documents of sponsored projects',
        'Total number of experiments/ computational projects',
        'Number of ongoing experiments/ computational projects',
        'Number of completed experiments/ computational projects',
        'Supporting Documents of experiments/ computational projects',
        'Patent Details',
        'Ph.D Defence Date',
        'Total Experience',
        'Post PhD Experience',
        'Total Ph.D Students Supervised (Degree Awarded)',
        'Total Ongoing Ph.D Supervision',
        'Total number of sponsored projects (Ongoing + Completed)',
        'Number of ongoing sponsored projects',
        'Total number of experiments/ computational projects',
        'Total Number of Publications in SCI / ABDC Journals',
        'Total Number of Publications in SCI / ABDC Journals (Post PhD)',
        'Membership/Fellowship of other institutions/professionals societies',
        'Other activities/Responsibilities',
        'Any other relevant information',
        'Academic Year Break',
        'Awards and Recognitions',
        'Have you been punished during your services or convicted by a court of law ?',
        'Were you at any time declared medically unfit or asked to submit your resignation or discharged or dismissed?',
        'Details regarding First Reference',
        'Details regarding Second Reference',
        'Details regarding Third Reference',
        'Place of Candidate',
        'Date',
        'Signature of Candidate',
        'Resume of Candidate',
        'Payment Receipt',
        'View More of Candidate'
    ]

    writer.writerow(heading_data)    # adding all the headings

    for i in list(Applicant.objects.all()):
        applicant_data = []
        if(General.objects.filter(applicant=i).exists() == False or SponsoredProject.objects.filter(applicant=i).exists() == False):
            continue
        else:
            applicant_data += [i.application_no,
                           Applicant.objects.filter(application_no=i)[0].post,
                           Applicant.objects.filter(application_no=i)[
                               0].department,
                           Applicant.objects.filter(application_no=i)[
                               0].Research_Domain,
                           General.objects.filter(applicant=i)[0].full_name,
                           General.objects.filter(applicant=i)[0].DOB,
                           General.objects.filter(applicant=i)[0].father_name,
                           General.objects.filter(applicant=i)[0].address_perm,
                           General.objects.filter(applicant=i)[
                               0].telephone_perm,
                           General.objects.filter(applicant=i)[0].pin_perm,
                           General.objects.filter(applicant=i)[
                               0].mobile_code,
                           General.objects.filter(applicant=i)[
                               0].mobile_number,
                           General.objects.filter(applicant=i)[0].email,
                           General.objects.filter(applicant=i)[0].gender,
                           General.objects.filter(applicant=i)[
                               0].marital_status,
                           General.objects.filter(applicant=i)[0].nationality,
                           General.objects.filter(applicant=i)[0].state,
                           General.objects.filter(applicant=i)[0].category,
                           General.objects.filter(applicant=i)[0].reservation,
                           PhD.objects.filter(applicant=i)[0].PhD_awarded,
                           ]

        # phd tables : ongoing, thesis submitted, awarded and not awarded

        if(PhD.objects.filter(applicant=i)[0].PhD_awarded == "No"):
            for j in range(0, 79):
                applicant_data.append("N/A")

        else:
            applicant_data.append(
                PhD.objects.filter(applicant=i)[0].PhD_details)
            if(PhD.objects.filter(applicant=i)[0].PhD_details == "Ongoing"):
                applicant_data += [
                    PhDOngoing.objects.filter(applicant=i)[0].PhD_title,
                    PhDOngoing.objects.filter(applicant=i)[0].Research_Domain,
                    PhDOngoing.objects.filter(applicant=i)[0].Institute_Name,
                    PhDOngoing.objects.filter(applicant=i)[0].University_Name,
                    PhDOngoing.objects.filter(applicant=i)[
                        0].Registration_Date,
                    PhDOngoing.objects.filter(applicant=i)[
                        0].supporting_documents.url,
                ]
                for j in range(0, 72):
                    applicant_data.append("N/A")

            elif(PhD.objects.filter(applicant=i)[0].PhD_details == "Thesis Submitted"):
                for j in range(0, 6):
                    applicant_data.append("N/A")
                # total no. of thesis submitted
                applicant_data.append(
                    len(list(ThesisSubmitted.objects.filter(applicant=i))))
                if(len(list(ThesisSubmitted.objects.filter(applicant=i))) <= 5):
                    for j in range(0, len(list(ThesisSubmitted.objects.filter(applicant=i)))):
                        applicant_data.append(
                            ThesisSubmitted.objects.filter(applicant=i)[j].PhD_title)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Research_Domain)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Institute_Name)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].University_Name)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Registration_Date)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Submission_Date)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].supporting_documents.url)
                    for j in range(len(list(ThesisSubmitted.objects.filter(applicant=i))), 5):
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                else:
                    for j in range(0, 5):
                        applicant_data.append(
                            ThesisSubmitted.objects.filter(applicant=i)[j].PhD_title)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Research_Domain)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Institute_Name)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].University_Name)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Registration_Date)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].Submission_Date)
                        applicant_data.append(ThesisSubmitted.objects.filter(
                            applicant=i)[j].supporting_documents.url)
                for j in range(0, 36):
                    applicant_data.append("N/A")

            elif(PhD.objects.filter(applicant=i)[0].PhD_details == "Awarded"):
                for j in range(0, 42):
                    applicant_data.append("N/A")
                # total no. phd awarded
                applicant_data.append(
                    len(list(PhDAwarded.objects.filter(applicant=i))))
                if(len(list(PhDAwarded.objects.filter(applicant=i))) <= 5):
                    for j in range(0, len(list(PhDAwarded.objects.filter(applicant=i)))):
                        applicant_data.append(
                            PhDAwarded.objects.filter(applicant=i)[j].PhD_title)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Research_Domain)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Institute_Name)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].University_Name)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Registration_Date)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Defense_Date)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].supporting_documents.url)
                    for j in range(len(list(PhDAwarded.objects.filter(applicant=i))), 5):
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                        applicant_data.append("N/A")
                else:
                    for j in range(0, 5):
                        applicant_data.append(
                            PhDAwarded.objects.filter(applicant=i)[j].PhD_title)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Research_Domain)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Institute_Name)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].University_Name)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Registration_Date)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].Submission_Date)
                        applicant_data.append(PhDAwarded.objects.filter(
                            applicant=i)[j].supporting_documents.url)

        # print(EducationalQualifications.objects.filter(applicant=i))
        # for j in range(0,len(list(EducationalQualifications.objects.filter(applicant=i)))):
            # print(EducationalQualifications.objects.filter(applicant=i)[j].equivalent_to)

        if(len(list(EducationalQualifications.objects.filter(applicant=i))) == 0):
            for j in range(0, 20):
                applicant_data.append("N/A")

        else:
            tableLength = len(
                list(EducationalQualifications.objects.filter(applicant=i)))
            temp = 0
            condition = True
            # class 10th
            if(condition and EducationalQualifications.objects.filter(applicant=i)[temp].equivalent_to == "Class 10th"):
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].name)
                applicant_data.append(EducationalQualifications.objects.filter(applicant=i)[
                                      temp].obtained + ' (' + EducationalQualifications.objects.filter(applicant=i)[temp].marks + ')')
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].subjects)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].year_of_passing)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].supporting_documents.url)
                temp += 1
                if(temp == tableLength):
                    condition = False

            else:
                for j in range(0, 5):
                    applicant_data.append("N/A")

            # class 12th or Diploma
            if(condition and (EducationalQualifications.objects.filter(applicant=i)[temp].equivalent_to == "Class 12th" or EducationalQualifications.objects.filter(applicant=i)[temp].equivalent_to == "Diploma")):
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].name)
                applicant_data.append(EducationalQualifications.objects.filter(applicant=i)[
                                      temp].obtained + ' (' + EducationalQualifications.objects.filter(applicant=i)[temp].marks + ')')
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].subjects)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].year_of_passing)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].supporting_documents.url)
                temp += 1
                if(temp == tableLength):
                    condition = False
            else:
                for j in range(0, 5):
                    applicant_data.append("N/A")

            # Bachelors
            if(condition and EducationalQualifications.objects.filter(applicant=i)[temp].equivalent_to == "Bachelors"):
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].name)
                applicant_data.append(EducationalQualifications.objects.filter(applicant=i)[
                                      temp].obtained + ' (' + EducationalQualifications.objects.filter(applicant=i)[temp].marks + ')')
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].subjects)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].year_of_passing)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].supporting_documents.url)
                temp += 1
                if(temp == tableLength):
                    condition = False
            else:
                for j in range(0, 5):
                    applicant_data.append("N/A")

            # Masters
            if(condition and EducationalQualifications.objects.filter(applicant=i)[temp].equivalent_to == "Masters"):
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].name)
                applicant_data.append(EducationalQualifications.objects.filter(applicant=i)[
                                      temp].obtained + ' (' + EducationalQualifications.objects.filter(applicant=i)[temp].marks + ')')
                applicant_data.append(
                    EducationalQualifications.objects.filter(applicant=i)[temp].subjects)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].year_of_passing)
                applicant_data.append(EducationalQualifications.objects.filter(
                    applicant=i)[temp].supporting_documents.url)
                temp += 1
                if(temp == tableLength):
                    condition = False
            else:
                for j in range(0, 5):
                    applicant_data.append("N/A")

        if(len(list(EmploymentExp.objects.filter(applicant=i))) <= 5):
            for j in range(0, len(list(EmploymentExp.objects.filter(applicant=i)))):
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].name)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].post)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].from_year)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].to_year)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].salary)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].nature)
                applicant_data.append(EmploymentExp.objects.filter(
                    applicant=i)[j].supporting_documents.url)
            for j in range(len(list(EmploymentExp.objects.filter(applicant=i))), 5):
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
        else:
            for j in range(0, 5):
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].name)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].post)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].from_year)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].to_year)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].salary)
                applicant_data.append(
                    EmploymentExp.objects.filter(applicant=i)[j].nature)
                applicant_data.append(EmploymentExp.objects.filter(
                    applicant=i)[j].supporting_documents.url)
        if(len(list(ResearchExp.objects.filter(applicant=i))) <= 5):
            for j in range(0, len(list(ResearchExp.objects.filter(applicant=i)))):
                applicant_data.append(
                    ResearchExp.objects.filter(applicant=i)[j].From)
                applicant_data.append(
                    ResearchExp.objects.filter(applicant=i)[j].to)
                applicant_data.append(ResearchExp.objects.filter(
                    applicant=i)[j].number_of_months)
                applicant_data.append(ResearchExp.objects.filter(
                    applicant=i)[j].supporting_documents.url)
            for j in range(len(list(ResearchExp.objects.filter(applicant=i))), 5):
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
        else:
            for j in range(0, 5):
                applicant_data.append(
                    ResearchExp.objects.filter(applicant=i)[j].From)
                applicant_data.append(
                    ResearchExp.objects.filter(applicant=i)[j].to)
                applicant_data.append(ResearchExp.objects.filter(
                    applicant=i)[j].number_of_months)
                applicant_data.append(ResearchExp.objects.filter(
                    applicant=i)[j].supporting_documents.url)
        if(len(list(Books.objects.filter(applicant=i))) <= 5):
            for j in range(0, len(list(Books.objects.filter(applicant=i)))):
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].title)
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].author)
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].publisher)
                applicant_data.append(Books.objects.filter(
                    applicant=i)[j].date_publish)
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].isbn)
                applicant_data.append(Books.objects.filter(
                    applicant=i)[j].supporting_documents.url)
            for j in range(len(list(Books.objects.filter(applicant=i))), 5):
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
        else:
            for j in range(0, 5):
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].title)
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].author)
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].publisher)
                applicant_data.append(Books.objects.filter(
                    applicant=i)[j].date_publish)
                applicant_data.append(
                    Books.objects.filter(applicant=i)[j].isbn)
                applicant_data.append(Books.objects.filter(
                    applicant=i)[j].supporting_documents.url)
        if(len(list(Chapters.objects.filter(applicant=i))) <= 5):
            for j in range(0, len(list(Chapters.objects.filter(applicant=i)))):
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].book_title)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].chapter)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].author)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].publisher)
                applicant_data.append(Chapters.objects.filter(
                    applicant=i)[j].date_of_publisher)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].isbn_issn)
                applicant_data.append(Chapters.objects.filter(
                    applicant=i)[j].supporting_documents.url)
            for j in range(len(list(Chapters.objects.filter(applicant=i))), 5):
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
        else:
            for j in range(0, 5):
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].book_title)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].chapter)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].author)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].publisher)
                applicant_data.append(Chapters.objects.filter(
                    applicant=i)[j].date_of_publisher)
                applicant_data.append(
                    Chapters.objects.filter(applicant=i)[j].isbn_issn)
                applicant_data.append(Chapters.objects.filter(
                    applicant=i)[j].supporting_documents.url)
        if(len(list(NewspaperArticle.objects.filter(applicant=i))) <= 5):
            for j in range(0, len(list(NewspaperArticle.objects.filter(applicant=i)))):
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].article_title)
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].journal_name)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].author)
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].date_published)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].vol_no)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].referred)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].naas)
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].supporting_documents.url)
            for j in range(len(list(NewspaperArticle.objects.filter(applicant=i))), 5):
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
        else:
            for j in range(0, 5):
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].article_title)
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].journal_name)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].author)
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].date_published)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].vol_no)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].referred)
                applicant_data.append(
                    NewspaperArticle.objects.filter(applicant=i)[j].naas)
                applicant_data.append(NewspaperArticle.objects.filter(
                    applicant=i)[j].supporting_documents.url)
        if(len(list(SeminarArticles.objects.filter(applicant=i))) <= 5):
            for j in range(0, len(list(SeminarArticles.objects.filter(applicant=i)))):
                applicant_data.append(SeminarArticles.objects.filter(
                    applicant=i)[j].article_title)
                applicant_data.append(SeminarArticles.objects.filter(
                    applicant=i)[j].seminar_subject)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].location)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].From)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].to)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].published)
                applicant_data.append(SeminarArticles.objects.filter(
                    applicant=i)[j].supporting_documents.url)
            for j in range(len(list(SeminarArticles.objects.filter(applicant=i))), 5):
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
                applicant_data.append("N/A")
        else:
            for j in range(0, 5):
                applicant_data.append(SeminarArticles.objects.filter(
                    applicant=i)[j].article_title)
                applicant_data.append(SeminarArticles.objects.filter(
                    applicant=i)[j].seminar_subject)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].location)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].From)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].to)
                applicant_data.append(
                    SeminarArticles.objects.filter(applicant=i)[j].published)
                applicant_data.append(SeminarArticles.objects.filter(
                    applicant=i)[j].supporting_documents.url)

        applicant_data += [
            Thesis.objects.filter(applicant=i)[0].ongoing_phd,
            Thesis.objects.filter(applicant=i)[0].completed_phd,
            AdministrativeDetails.objects.filter(
                applicant=i)[0].administrative_details,
            SponsoredProject.objects.filter(applicant=i)[0].spo_tot_number,
            SponsoredProject.objects.filter(applicant=i)[0].spo_ongoing,
            SponsoredProject.objects.filter(applicant=i)[0].spo_completed,
            SponsoredProject.objects.filter(applicant=i)[0].spo_file,
            Experiments.objects.filter(applicant=i)[0].exp_tot_number,
            Experiments.objects.filter(applicant=i)[0].exp_ongoing,
            Experiments.objects.filter(applicant=i)[0].exp_completed,
            Experiments.objects.filter(applicant=i)[0].exp_file,
            Patent.objects.filter(applicant=i)[0].patent_details,
            Summary.objects.filter(applicant=i)[0].defence_date,
            Summary.objects.filter(applicant=i)[0].total_exp,
            Summary.objects.filter(applicant=i)[0].exp_post_phd,
            Summary.objects.filter(applicant=i)[0].total_phd_students,
            Summary.objects.filter(applicant=i)[0].ongoing_phd_supervision,
            Summary.objects.filter(applicant=i)[0].total_projects,
            Summary.objects.filter(applicant=i)[0].ongoing_projects,
            Summary.objects.filter(applicant=i)[0].computational_projects,
            Summary.objects.filter(applicant=i)[0].SCI_journal,
            Summary.objects.filter(applicant=i)[0].SCI_journal_post_phd,
            OtherInfo.objects.filter(applicant=i)[0].membership,
            OtherInfo.objects.filter(applicant=i)[0].responsibilities,
            OtherInfo.objects.filter(applicant=i)[
                0].Any_other_relevant_information,
            OtherInfo.objects.filter(applicant=i)[0].academic_year_break,
            OtherInfo.objects.filter(applicant=i)[0].awards_and_recognition,
            OtherInfo.objects.filter(applicant=i)[0].judicial_punishment,
            OtherInfo.objects.filter(applicant=i)[0].unfit_for_position,
            OtherInfo.objects.filter(applicant=i)[0].reference1,
            OtherInfo.objects.filter(applicant=i)[0].reference2,
            OtherInfo.objects.filter(applicant=i)[0].reference3,
            Declaration.objects.filter(applicant=i)[0].place,
            Declaration.objects.filter(applicant=i)[0].date,
            Declaration.objects.filter(applicant=i)[0].signature,
            Declaration.objects.filter(applicant=i)[0].resume,
            Declaration.objects.filter(applicant=i)[0].receipt,
            'https://iiitl.pythonanywhere.com/admin/user/' + str(i),
        ]

        writer.writerow(applicant_data)  # adding data of particular applicant

    return response


def adminLogin(request):
    context = {
        'could_not_log_in': False,
        'abc': 1,
        'three': False,
    }
    if(request.method == 'POST'):
        tryme = int(request.POST.get('chances'))
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)

        tryme = tryme + 1
        tryme = tryme % 4

        if(user is not None and user.is_superuser == 1):
            login(request, user)
            return HttpResponseRedirect('profile/')
        else:
            context = {
                'could_not_log_in': True,
                'abc': tryme,
            }
        if(tryme == 0):
            subject = "Alert! Someone is trying to login as admin at Faculty Recruitment Portal"
            msg = 'This is an auto generated message.\n\nIt is to inform you that someone is trying to login as admin at Faculty Recruitment Portal and failed three times!' + '\nkindly, secure your server!\n'
            to = ['lit2019058@iiitl.ac.in', 'recruitment_faculty@iiitl.ac.in']
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
            tryme = 1
            context = {
                'could_not_log_in': True,
                'abc': 1,
                'three': True,
            }
        else:
            print('tryme', tryme)
    return render(request, 'recruitment/adminLogin.html', context)


def profile(request):
    if(request.user.is_superuser == 1):
        return HttpResponseRedirect('/admin/')
    return render(request, 'recruitment/profile.html', {})


def home(request):
    return render(request, 'recruitment/index.html', {})

def viewApplications(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/')
    else:
        userApplications=[]
        for i in General.objects.all():
            # if(i.email== "manishreddy6305@gmail.com"): #testing in dev
            if(i.email== request.user.email):
                presAppli = {}
                presAppli['application_no'] = (i.applicant)
                presAppli['is_completed'] = (i.is_completed)
                presAppli['applied_post'] = Applicant.objects.filter(
                    application_no=i.applicant)[0].post
                presAppli['applied_department'] = Applicant.objects.filter(
                    application_no=i.applicant)[0].department
                presAppli['applied_date'] = Applicant.objects.filter(
                    application_no=i.applicant)[0].date
                userApplications.append(presAppli)
        isEmpty = 1
        if len(userApplications):
            isEmpty = 0
        return render(request, 'recruitment/userApplications.html', {'isEmpty' : isEmpty, 'applications':userApplications})

def admin(request):
    if(request.user.is_superuser != 1):
        return HttpResponseRedirect('/')
    admin_data = {}
    appli_data = []
    for i in list(General.objects.all()):
        presAppli = {}
        presAppli['application_no'] = (i.applicant)
        presAppli['applicant_name'] = (i.full_name)
        presAppli['applied_post'] = Applicant.objects.filter(
            application_no=i.applicant)[0].post
        presAppli['applied_department'] = Applicant.objects.filter(
            application_no=i.applicant)[0].department
        presAppli['applied_date'] = Applicant.objects.filter(
            application_no=i.applicant)[0].date
        presAppli['status']=Applicant.objects.filter(
            application_no=i.applicant)[0].status
        appli_data.append(presAppli)
    admin_data['allData'] = appli_data
    return render(request, 'recruitment/admin.html', {'data': admin_data})


def viewMore(request, application_number):
    # print (list(EmploymentExp.objects.filter(applicant=application_number)))
    return render(request, 'recruitment/view-more.html', {
        'applicant_data': {
            'application_number': application_number,
            'date': Applicant.objects.filter(application_no=application_number)[0].date,
            'post': Applicant.objects.filter(application_no=application_number)[0].post,
            'department': Applicant.objects.filter(application_no=application_number)[0].department,
            'reserach_domain': Applicant.objects.filter(application_no=application_number)[0].Research_Domain,
            'profile_photo': Applicant.objects.filter(application_no=application_number)[0].profile_picture,
            'status': Applicant.objects.filter(application_no=application_number)[0].status
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
            'mobile_code': General.objects.filter(applicant=application_number)[0].mobile_code,
            'mobile_number': General.objects.filter(applicant=application_number)[0].mobile_number,
            'email': General.objects.filter(applicant=application_number)[0].email,
            'gender': General.objects.filter(applicant=application_number)[0].gender,
            'marital_status': General.objects.filter(applicant=application_number)[0].marital_status,
            'nationality': General.objects.filter(applicant=application_number)[0].nationality,
            'state': General.objects.filter(applicant=application_number)[0].state,
            'category': General.objects.filter(applicant=application_number)[0].category,
            'reservation': General.objects.filter(applicant=application_number)[0].reservation,
            'certificate': General.objects.filter(applicant=application_number)[0].reservation_certificate,
        },
        'otherinformation_data': {
            'membership': OtherInfo.objects.filter(applicant=application_number)[0].membership,
            'responsibilities': OtherInfo.objects.filter(applicant=application_number)[0].responsibilities,
            'Any_other_relevant_information': OtherInfo.objects.filter(applicant=application_number)[0].Any_other_relevant_information,
            'academic_year_break': OtherInfo.objects.filter(applicant=application_number)[0].academic_year_break,
            # 'college_punishment': OtherInfo.objects.filter(applicant=application_number)[0].college_punishment,
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
            'resume': Declaration.objects.filter(applicant=application_number)[0].resume,
            'receipt': Declaration.objects.filter(applicant=application_number)[0].receipt,
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
            'PhD_details': PhD.objects.filter(applicant=application_number)[0].PhD_details
        },
        'PhDOngoing': {
            'PhD_title': PhDOngoing.objects.filter(applicant=application_number)[0].PhD_title,
            'Research_Domain': PhDOngoing.objects.filter(applicant=application_number)[0].Research_Domain,
            'Institute_Name': PhDOngoing.objects.filter(applicant=application_number)[0].Institute_Name,
            'University_Name': PhDOngoing.objects.filter(applicant=application_number)[0].University_Name,
            'Registration_Date': PhDOngoing.objects.filter(applicant=application_number)[0].Registration_Date,
        },
        'ThesisSubmitted': list(ThesisSubmitted.objects.filter(applicant=application_number)),
        'PhDAwarded': list(PhDAwarded.objects.filter(applicant=application_number)),
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
        # print("submission_form")
        # Applicant
        applicant_data = {}
        number = len(Applicant.objects.filter(
            date=datetime.datetime.now().date()))
        application_number = str(
            datetime.datetime.now().date())+str(number+1).zfill(3)
        applicant_data['application_no'] = application_number
        applicant_data['date'] = datetime.datetime.now().date()
        applicant_data['advertisement_no'] = 'Rolling Advertisement No.1'
        applicant_data['post'] = data['AppPost']
        applicant_data['department'] = data['Dept']
        applicant_data['Research_Domain'] = data['research_domain']
        applicant_data['profile_picture'] = request.FILES['profile_photo']
        Applicant.objects.create(**applicant_data)

        # General
        general_data = {}
        general_data['full_name'] = data['saluation'] + data['name'].strip()
        general_data['DOB'] = data['dateofbirth']
        general_data['father_name'] = data['fathername']
        general_data['address_perm'] = data['permanentaddress']
        general_data['pin_perm'] = data['permanentpincode']
        general_data['telephone_perm'] = data['permanenttelephone']
        general_data['address_mail'] = data['mailingaddress']
        general_data['telephone_mail'] = data['mailingtelephone']
        general_data['pin_mail'] = data['mailingpincode']
        general_data['mobile_code'] = str(data['mobilecode'])
        general_data['mobile_number'] = str(data['mobile'])
        general_data['email'] = data['email']
        general_data['gender'] = data['gender']
        general_data['marital_status'] = data['maritalstatus']
        general_data['nationality'] = data['nationality']
        general_data['state'] = data['domicile_state']
        general_data['category'] = data['category']
        general_data['reservation'] = data['reservation']
        general_data['is_completed'] = True
        if(data.get('reservation') == 'Yes'):
            if( 'reservation_certificate' in request.FILES):
                general_data['reservation_certificate'] = request.FILES['reservation_certificate'] 
        general_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        General.objects.create(**general_data)

        # Other Information
        otherinformation_data = {}
        otherinformation_data['membership'] = data['miscTa1']
        otherinformation_data['responsibilities'] = data['miscTa2']
        otherinformation_data['Any_other_relevant_information'] = data['miscTa3']
        otherinformation_data['academic_year_break'] = data['miscTa4']
        otherinformation_data['awards_and_recognition'] = data['miscTa5']
        otherinformation_data['judicial_punishment'] = data['miscTa6']
        otherinformation_data['unfit_for_position'] = data['miscTa7']
        otherinformation_data['reference1'] = data['miscTa8']
        otherinformation_data['reference2'] = data['miscTa9']
        otherinformation_data['reference3'] = data['miscTa10']
        otherinformation_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        OtherInfo.objects.create(**otherinformation_data)

        # Signature
        signed_data = {}
        signed_data['place'] = data['signPlace']
        signed_data['date'] = datetime.datetime.now().date()
        if('signUpload' in request.FILES):
            signed_data['signature'] = request.FILES['signUpload']
        if('resumeUpload' in request.FILES):
            signed_data['resume'] = request.FILES['resumeUpload']
        if('receipt' in request.FILES):
            signed_data['receipt'] = request.FILES['receipt']
        signed_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        Declaration.objects.create(**signed_data)

        # Page 4
        # Thesis
        thesis_data = {}
        thesis_data['ongoing_phd'] = data['ongoing_phd']
        thesis_data['completed_phd'] = data['completed_phd']
        thesis_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        Thesis.objects.create(**thesis_data)

        # Administrative Details
        administrative_details_data = {}
        administrative_details_data['administrative_details'] = data['administrative_details']
        administrative_details_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        AdministrativeDetails.objects.create(**administrative_details_data)

        # Patent
        patent_data = {}
        patent_data['patent_details'] = data['patent_details']
        patent_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        Patent.objects.create(**patent_data)

        # Summary
        summary_data = {}
        if(data['phd_defence_date'] == ''):
            summary_data['defence_date'] = 'N/A'
        else:
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
        summary_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        Summary.objects.create(**summary_data)
        # Sponsored Projects
        sponsored_projects_data = {}
        sponsored_projects_data['spo_tot_number'] = data['spo_tot_number']
        sponsored_projects_data['spo_ongoing'] = data['spo_ongoing']
        sponsored_projects_data['spo_completed'] = data['spo_completed']
        if(data.get('spo_tot_number') != "0"):
            if('spofile' in request.FILES):
                sponsored_projects_data['spo_file'] = request.FILES['spofile']
        else:
            sponsored_projects_data['spo_file'] = "N/A"
        sponsored_projects_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        SponsoredProject.objects.create(**sponsored_projects_data)
        # Experiments
        experiments_data = {}
        experiments_data['exp_tot_number'] = data['exp_tot_number']
        experiments_data['exp_ongoing'] = data['exp_ongoing']
        experiments_data['exp_completed'] = data['exp_completed']
        if(data.get('exp_tot_number') != "0"):
            if('expfile' in request.FILES):
                experiments_data['exp_file'] = request.FILES['expfile']
        else:
            experiments_data['exp_file'] = "N/A"
        experiments_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        Experiments.objects.create(**experiments_data)

        # Educational Qualifications
        phd_data = {}
        phd_data['PhD_awarded'] = data['awarded_phd']
        phd_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        if(data['awarded_phd'] == "No"):
            phd_data['PhD_details'] = "N/A"
            PhD.objects.create(**phd_data)
            ongoing_data = {}
            ongoing_data['PhD_title'] = "N/A"
            ongoing_data['Research_Domain'] = "N/A"
            ongoing_data['Institute_Name'] = "N/A"
            ongoing_data['University_Name'] = "N/A"
            ongoing_data['Registration_Date'] = "N/A"
            ongoing_data['supporting_documents'] = "N/A"
            ongoing_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            PhDOngoing.objects.create(**ongoing_data)
            submitted_data = {}
            submitted_data['PhD_title'] = "N/A"
            submitted_data['Research_Domain'] = "N/A"
            submitted_data['Institute_Name'] = "N/A"
            submitted_data['University_Name'] = "N/A"
            submitted_data['Registration_Date'] = "N/A"
            submitted_data['Submission_Date'] = "N/A"
            submitted_data['supporting_documents'] = "N/A"
            submitted_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            ThesisSubmitted.objects.create(**submitted_data)
            awarded_data = {}
            awarded_data['PhD_title'] = "N/A"
            awarded_data['Research_Domain'] = "N/A"
            awarded_data['Institute_Name'] = "N/A"
            awarded_data['University_Name'] = "N/A"
            awarded_data['Registration_Date'] = "N/A"
            awarded_data['Defense_Date'] = "N/A"
            awarded_data['supporting_documents'] = "N/A"
            awarded_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            PhDAwarded.objects.create(**awarded_data)
        else:
            phd_data['PhD_details'] = data['phd']
            phd_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            PhD.objects.create(**phd_data)
            if(data['phd'] == "Ongoing"):
                ongoing_data = {}
                ongoing_data['PhD_title'] = data['ongoing1-title']
                ongoing_data['Research_Domain'] = data['ongoing1-domain']
                ongoing_data['Institute_Name'] = data['ongoing1-institute']
                ongoing_data['University_Name'] = data['ongoing1-university']
                ongoing_data['Registration_Date'] = data['ongoing1-date']
                ongoing_data['supporting_documents'] = request.FILES['ongoing1-file']
                ongoing_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                PhDOngoing.objects.create(**ongoing_data)
                submitted_data = {}
                submitted_data['PhD_title'] = "N/A"
                submitted_data['Research_Domain'] = "N/A"
                submitted_data['Institute_Name'] = "N/A"
                submitted_data['University_Name'] = "N/A"
                submitted_data['Registration_Date'] = "N/A"
                submitted_data['Submission_Date'] = "N/A"
                submitted_data['supporting_documents'] = "N/A"
                submitted_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                ThesisSubmitted.objects.create(**submitted_data)
                awarded_data = {}
                awarded_data['PhD_title'] = "N/A"
                awarded_data['Research_Domain'] = "N/A"
                awarded_data['Institute_Name'] = "N/A"
                awarded_data['University_Name'] = "N/A"
                awarded_data['Registration_Date'] = "N/A"
                awarded_data['Defense_Date'] = "N/A"
                awarded_data['supporting_documents'] = "N/A"
                awarded_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                PhDAwarded.objects.create(**awarded_data)
            elif(data['phd'] == "Thesis Submitted"):
                ongoing_data = {}
                ongoing_data['PhD_title'] = "N/A"
                ongoing_data['Research_Domain'] = "N/A"
                ongoing_data['Institute_Name'] = "N/A"
                ongoing_data['University_Name'] = "N/A"
                ongoing_data['Registration_Date'] = "N/A"
                ongoing_data['supporting_documents'] = "N/A"
                ongoing_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                PhDOngoing.objects.create(**ongoing_data)
                num_of_submitted_records = list(
                    filter(lambda s: 'thesis' in s, list(data.keys())))
                num_of_submitted_records_length = len(num_of_submitted_records)
                last_awarded_record = num_of_submitted_records[num_of_submitted_records_length-1]
                number_awarded_record = last_awarded_record[6]
                for i in range(1, int(number_awarded_record)+1):
                    if(data.get('thesis'+str(i) + '-title', False) == False):
                        continue
                    else:
                        submitted_data = {}
                        submitted_data['PhD_title'] = data.get(
                            'thesis' + str(i) + '-title')
                        submitted_data['Research_Domain'] = data.get(
                            'thesis' + str(i) + '-domain')
                        submitted_data['Institute_Name'] = data.get(
                            'thesis' + str(i) + '-institute')
                        submitted_data['University_Name'] = data.get(
                            'thesis' + str(i) + '-university')
                        submitted_data['Registration_Date'] = data.get(
                            'thesis' + str(i) + '-regdate')
                        submitted_data['Submission_Date'] = data.get(
                            'thesis' + str(i) + '-subdate')
                        ans = 'thesis' + str(i) + '-file'
                        submitted_data['supporting_documents'] = request.FILES[ans]
                        submitted_data['applicant'] = Applicant.objects.get(
                            application_no=application_number)
                        ThesisSubmitted.objects.create(**submitted_data)
                awarded_data = {}
                awarded_data['PhD_title'] = "N/A"
                awarded_data['Research_Domain'] = "N/A"
                awarded_data['Institute_Name'] = "N/A"
                awarded_data['University_Name'] = "N/A"
                awarded_data['Registration_Date'] = "N/A"
                awarded_data['Defense_Date'] = "N/A"
                awarded_data['supporting_documents'] = "N/A"
                awarded_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                PhDAwarded.objects.create(**awarded_data)
            elif(data['phd'] == "Awarded"):
                ongoing_data = {}
                ongoing_data['PhD_title'] = "N/A"
                ongoing_data['Research_Domain'] = "N/A"
                ongoing_data['Institute_Name'] = "N/A"
                ongoing_data['University_Name'] = "N/A"
                ongoing_data['Registration_Date'] = "N/A"
                ongoing_data['supporting_documents'] = "N/A"
                ongoing_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                PhDOngoing.objects.create(**ongoing_data)
                submitted_data = {}
                submitted_data['PhD_title'] = "N/A"
                submitted_data['Research_Domain'] = "N/A"
                submitted_data['Institute_Name'] = "N/A"
                submitted_data['University_Name'] = "N/A"
                submitted_data['Registration_Date'] = "N/A"
                submitted_data['Submission_Date'] = "N/A"
                submitted_data['supporting_documents'] = "N/A"
                submitted_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                ThesisSubmitted.objects.create(**submitted_data)
                num_of_awarded_records = list(
                    filter(lambda s: 'awarded' in s, list(data.keys())))
                num_of_awarded_records_length = len(num_of_awarded_records)
                last_awarded_record = num_of_awarded_records[num_of_awarded_records_length-1]
                number_awarded_record = last_awarded_record[7]
                for i in range(1, int(number_awarded_record)+1):
                    if(data.get('awarded'+str(i) + '-title', False) == False):
                        continue
                    else:
                        awarded_data = {}
                        awarded_data['PhD_title'] = data.get(
                            'awarded'+str(i)+'-title', False)
                        awarded_data['Research_Domain'] = data.get(
                            'awarded'+str(i)+'-domain', False)
                        awarded_data['Institute_Name'] = data.get(
                            'awarded'+str(i)+'-institute', False)
                        awarded_data['University_Name'] = data.get(
                            'awarded'+str(i)+'-university', False)
                        awarded_data['Registration_Date'] = data.get(
                            'awarded'+str(i)+'-regdate', False)
                        awarded_data['Defense_Date'] = data.get(
                            'awarded'+str(i)+'-defdate', False)
                        ans = 'awarded'+str(i)+'-file'
                        awarded_data['supporting_documents'] = request.FILES[ans]
                        awarded_data['applicant'] = Applicant.objects.get(
                            application_no=application_number)
                        PhDAwarded.objects.create(**awarded_data)

        # Academic Details
        num_of_academic_records = list(
            filter(lambda s: 'course' in s, list(data.keys())))
        num_of_academic_records_length = len(num_of_academic_records)
        last_academic_record = num_of_academic_records[num_of_academic_records_length-1]
        number_academic_record = last_academic_record[6]
        file_list = list(EducationalQualifications.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        academic_details_check = EducationalQualifications.objects.filter(applicant_id = application_number).count()
        # print("Reached here")
        if(academic_details_check != 0):
            # print("deleteing all records")
            EducationalQualifications.objects.filter(applicant_id = application_number).delete()
        
        for i in range(1, int(number_academic_record)+1):
            if (data.get('course'+str(i), False) == "" or data.get('course'+str(i), False) == False):
                continue
            else:
                academic_details = {}
                academic_details['degree'] = data.get('course'+str(i), False)
                academic_details['equivalent_to'] = data.get(
                    'course' + str(i) + '-equivalent', False)
                academic_details['name'] = data.get(
                    'course'+str(i)+'-name', False)
                academic_details['marks'] = data.get(
                    'course'+str(i)+'-percentage', False)
                academic_details['obtained'] = data.get(
                    'course'+str(i)+'-obtained', False)
                academic_details['subjects'] = data.get(
                    'course'+str(i)+'-subject', False)
                academic_details['year_of_passing'] = data.get(
                    'yearOfPassing'+str(i), False)
                ans = 'course' + str(i) + '-file'
                if(i<=len(file_list)):
                    academic_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    academic_details['supporting_documents'] = request.FILES[ans]
                academic_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                EducationalQualifications.objects.create(**academic_details)
            # if re.search(r'[12]\d{3}',data.get('yearOfPassing-'+str(i),False)) is None:
            #     return render(request, 'recruitment/form.html',{'message':'Enter the year in Academic details in yyyy format.'})
            # if 0 <= float(data.get('course-'+str(i)+'-marks',False)) <= 100:
            #     academic_details['marks']  = data.get('course-'+str(i)+'-marks',False)
            # else:
            #     return render(request, 'recruitment/form.html',{'message':'Enter your percentage in Academic details a value between 0 to 100.'})

        # Professional
        num_of_professional_records = list(
            filter(lambda s: 'org' in s, list(data.keys())))
        last_professional_record = num_of_professional_records[len(
            num_of_professional_records)-1]
        number_professional_record = last_professional_record[3]
        
        file_list = list(EmploymentExp.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        professional_details_check = EmploymentExp.objects.filter(applicant_id = application_number).count()
        if(professional_details_check != 0):
            EmploymentExp.objects.filter(applicant_id = application_number).delete()

        for i in range(1, int(number_professional_record)+1):
            if (data.get('org' + str(i) + '-name') == ""):
                professional_details = {}
                professional_details['name'] = "N/A"
                professional_details['post'] = "N/A"
                professional_details['from_year'] = "N/A"
                professional_details['to_year'] = "N/A"
                professional_details['salary'] = "N/A"
                professional_details['nature'] = "N/A"
                professional_details['supporting_documents'] = "N/A"
                professional_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                EmploymentExp.objects.create(**professional_details)
            else:
                professional_details = {}
                professional_details['name'] = data.get(
                    'org' + str(i) + '-name', False)
                professional_details['post'] = data.get(
                    'org' + str(i) + '-post', False)
                professional_details['from_year'] = data.get(
                    'org' + str(i) + '-from', False)
                professional_details['to_year'] = data.get(
                    'org' + str(i) + '-to', False)
                professional_details['salary'] = data.get(
                    'org' + str(i) + '-salary', False)
                professional_details['nature'] = data.get(
                    'org' + str(i) + '-nature', False)
                ans = 'org' + str(i) + '-file'
                if(i<=len(file_list)):
                    professional_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    professional_details['supporting_documents'] = request.FILES[ans]
                professional_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                EmploymentExp.objects.create(**professional_details)

        # Books
        num_of_books_records = list(
            filter(lambda s: 'books' in s, list(data.keys())))
        # print(num_of_books_records)
        last_book_record = num_of_books_records[len(num_of_books_records)-1]
        number_books_record = last_book_record[5]
        # books_data = []
        for i in range(1, int(number_books_record)+1):
            if(data.get('books' + str(i) + '-title') == ""):
                books_details = {}
                books_details['title'] = "N/A"
                books_details['author'] = "N/A"
                books_details['publisher'] = "N/A"
                books_details['date_publish'] = "N/A"
                books_details['isbn'] = "N/A"
                books_details['supporting_documents'] = "N/A"
                books_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                Books.objects.create(**books_details)
            else:
                books_details = {}
                books_details['title'] = data.get(
                    'books' + str(i) + '-title', False)
                books_details['author'] = data.get(
                    'books' + str(i) + '-author', False)
                books_details['publisher'] = data.get(
                    'books' + str(i) + '-publisher', False)
                books_details['date_publish'] = data.get(
                    'books' + str(i) + '-date', False)
                books_details['isbn'] = data.get(
                    'books' + str(i) + '-number', False)
                ans = 'books' + str(i) + '-file'
                books_details['supporting_documents'] = request.FILES[ans]
                books_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                Books.objects.create(**books_details)

        # Chapters
        num_of_chapters_records = list(
            filter(lambda s: 'chapters' in s, list(data.keys())))
        last_chapter_record = num_of_chapters_records[len(
            num_of_chapters_records)-1]
        number_chapter_record = last_chapter_record[8]
        for i in range(1, int(number_chapter_record)+1):
            if(data.get('chapters' + str(i) + '-book_title') == ""):
                chapter_details = {}
                chapter_details['book_title'] = "N/A"
                chapter_details['chapter'] = "N/A"
                chapter_details['author'] = "N/A"
                chapter_details['publisher'] = "N/A"
                chapter_details['date_of_publisher'] = "N/A"
                chapter_details['isbn_issn'] = "N/A"
                chapter_details['supporting_documents'] = "N/A"
                chapter_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                Chapters.objects.create(**chapter_details)
            else:
                chapter_details = {}
                chapter_details['book_title'] = data.get(
                    'chapters' + str(i) + '-book_title', False)
                chapter_details['chapter'] = data.get(
                    'chapters' + str(i) + '-chapter', False)
                chapter_details['author'] = data.get(
                    'chapters' + str(i) + '-author', False)
                chapter_details['publisher'] = data.get(
                    'chapters' + str(i) + '-publisher', False)
                chapter_details['date_of_publisher'] = data.get(
                    'chapters' + str(i) + '-date_of_publisher', False)
                chapter_details['isbn_issn'] = data.get(
                    'chapters' + str(i) + '-number', False)
                chapter_details['supporting_documents'] = request.FILES['chapters' +
                                                                        str(i)+'-file']
                chapter_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                Chapters.objects.create(**chapter_details)

        # Newspapers Articles
        num_of_news_articles_records = list(
            filter(lambda s: 'news_articles' in s, list(data.keys())))
        last_news_articles_record = num_of_news_articles_records[len(
            num_of_news_articles_records)-1]
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
                news_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                NewspaperArticle.objects.create(**news_articles_details)
            else:
                news_articles_details = {}
                news_articles_details['article_title'] = data.get(
                    'news_articles' + str(i) + '-article_title', False)
                news_articles_details['journal_name'] = data.get(
                    'news_articles' + str(i) + '-journal_name', False)
                news_articles_details['author'] = data.get(
                    'news_articles' + str(i) + '-author', False)
                news_articles_details['date_published'] = data.get(
                    'news_articles' + str(i) + '-date_published', False)
                news_articles_details['vol_no'] = data.get(
                    'news_articles' + str(i) + '-page')
                news_articles_details['referred'] = data.get(
                    'news_articles' + str(i) + '-referred', False)
                news_articles_details['naas'] = data.get(
                    'news_articles' + str(i) + '-impact', False)
                news_articles_details['supporting_documents'] = request.FILES['news_articles'+str(
                    i)+'-file']
                news_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                NewspaperArticle.objects.create(**news_articles_details)

        # Seminar Articles
        num_of_seminar_articles = list(
            filter(lambda s: 'semi_articles' in s, list(data.keys())))
        last_semi_articles_record = num_of_seminar_articles[len(
            num_of_seminar_articles)-1]
        number_semi_articles_record = last_semi_articles_record[13]
        for i in range(1, int(number_semi_articles_record)+1):
            if(data.get('semi_articles' + str(i) + '-article_title') == ""):
                seminar_articles_details = {}
                seminar_articles_details['article_title'] = "N/A"
                seminar_articles_details['seminar_subject'] = "N/A"
                seminar_articles_details['location'] = "N/A"
                seminar_articles_details['From'] = "N/A"
                seminar_articles_details['to'] = "N/A"
                seminar_articles_details['published'] = "N/A"
                seminar_articles_details['supporting_documents'] = "N/A"
                seminar_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                SeminarArticles.objects.create(**seminar_articles_details)
            else:
                seminar_articles_details = {}
                seminar_articles_details['article_title'] = data.get(
                    'semi_articles' + str(i) + '-article_title', False)
                seminar_articles_details['seminar_subject'] = data.get(
                    'semi_articles' + str(i) + '-seminar_subject', False)
                seminar_articles_details['location'] = data.get(
                    'semi_articles' + str(i) + '-location', False)
                seminar_articles_details['From'] = data.get(
                    'semi_articles' + str(i) + '-from', False)
                seminar_articles_details['to'] = data.get(
                    'semi_articles' + str(i) + '-to', False)
                seminar_articles_details['published'] = data.get(
                    'semi_articles' + str(i) + '-published', False)
                seminar_articles_details['supporting_documents'] = "N/A"
                seminar_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                SeminarArticles.objects.create(**seminar_articles_details)

        # Research Experience
        num_of_research_exp = list(
            filter(lambda s: 'exper' in s, list(data.keys())))
        last_research_exp_record = num_of_research_exp[len(
            num_of_research_exp) - 1]
        number_research_exp_record = last_research_exp_record[5]
        
        file_list = list(ResearchExp.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        research_exp_check = ResearchExp.objects.filter(applicant_id = application_number).count()
        if(research_exp_check != 0):
            ResearchExp.objects.filter(applicant_id = application_number).delete()

        for i in range(1, int(number_research_exp_record)+1):
            if(data.get('exper' + str(i) + '-from') == ""):
                research_exp_details = {}
                research_exp_details['From'] = "N/A"
                research_exp_details['to'] = "N/A"
                research_exp_details['number_of_months'] = "N/A"
                research_exp_details['supporting_documents'] = "N/A"
                research_exp_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                ResearchExp.objects.create(**research_exp_details)
            else:
                research_exp_details = {}
                research_exp_details['From'] = data.get(
                    'exper' + str(i) + '-from', False)
                research_exp_details['to'] = data.get(
                    'exper' + str(i) + '-to', False)
                research_exp_details['number_of_months'] = data.get(
                    'exper' + str(i) + '-months', False)
                ans = 'exper' + str(i) + '-file'
                if(i<=len(file_list)):
                    research_exp_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    research_exp_details['supporting_documents'] = request.FILES[ans]
                research_exp_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                ResearchExp.objects.create(**research_exp_details)

        #  Messages!
        messages.success(
            request, 'Congratulations, your application has been submitted successfully!')
        messages.success(
            request, 'Your application number is :  ' + application_number)
        messages.success(request, '( Kindly note this for future reference )')

        # Confirmation E-mail
        confsubject = "Thanks for applying to IIIT Lucknow!"
        confmsg = 'Hi ' + str(general_data["full_name"]) + ',\nThanks for applying to IIIT Lucknow, we have received your application. Your application number is ' + application_number + ', save this for future reference.\n' + \
            'Due to high volumes of applications we receive, it may take some time to respond you back, but we encourage you to continue exploring our culture and stories at iiitl.ac.in' + \
            '\nFor more information or queries related to the recruitment process drop an mail to rectt.faculty@iiitl.ac.in.' + \
            '\n\nBest Regards,\nIIIT Lucknow'

        confto = general_data["email"]
        confres = send_mail(confsubject, confmsg,
                            settings.EMAIL_HOST_USER, [confto])

        return HttpResponseRedirect('/accounts/profile/')
    return render(request, 'recruitment/form.html', {})


def handleDraft(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # Applicant
        applicant_data = {}
        number = len(Applicant.objects.filter(
            date=datetime.datetime.now().date()))
        if "formId" in data:
            application_number = data['formId']
        else:
            application_number = str(
                datetime.datetime.now().date())+str(number+1).zfill(3)
            applicant_data['application_no'] = application_number
        applicant_data['date'] = datetime.datetime.now().date()
        applicant_data['advertisement_no'] = 'Rolling Advertisement No.1'
        if "AppPost" in data:
            applicant_data['post'] = data['AppPost']
        if "Dept" in data:
            applicant_data['department'] = data['Dept']
        applicant_data['Research_Domain'] = data['research_domain']
        if('profile_photo' in request.FILES):
            applicant_data['profile_picture'] = request.FILES['profile_photo']
        applicant_check = Applicant.objects.filter(application_no = application_number).count()
        if(applicant_check == 0):
            applicant_data['application_no'] = application_number
            Applicant.objects.create(**applicant_data)
        else:
            Applicant.objects.filter(application_no = application_number).update(**applicant_data)

        # General
        general_data = {}
        general_data['full_name'] = data['saluation'] + data['name'].strip()
        general_data['DOB'] = data['dateofbirth']
        general_data['father_name'] = data['fathername']
        general_data['address_perm'] = data['permanentaddress']
        general_data['pin_perm'] = data['permanentpincode']
        general_data['telephone_perm'] = data['permanenttelephone']
        general_data['address_mail'] = data['mailingaddress']
        general_data['telephone_mail'] = data['mailingtelephone']
        general_data['pin_mail'] = data['mailingpincode']
        general_data['mobile_code'] = str(data['mobilecode'])
        general_data['mobile_number'] = str(data['mobile'])
        general_data['email'] = data['email']
        if "gender" in data:
            general_data['gender'] = data['gender']
        if "maritalstatus" in data:
            general_data['marital_status'] = data['maritalstatus']
        general_data['nationality'] = data['nationality']
        if "domicile_state" in data:
            general_data['state'] = data['domicile_state']
        if "category" in data:
            general_data['category'] = data['category']
        if "reservation" in data:
            general_data['reservation'] = data['reservation']
        if(data['checkBtn'] == 'draft'):
            general_data['is_completed'] = False
        else:
            general_data['is_completed'] = True
        if(data.get('reservation') == 'Yes'):
            if( 'reservation_certificate' in request.FILES):
                general_data['reservation_certificate'] = request.FILES['reservation_certificate']
        general_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        general_check = General.objects.filter(applicant_id = application_number).count()
        if(general_check == 0):
            general_data['applicant_id'] = application_number
            General.objects.create(**general_data)
        else:
            General.objects.filter(applicant_id = application_number).update(**general_data)
        # print(general_data)

        # Other Information
        otherinformation_data = {}
        otherinformation_data['membership'] = data['miscTa1']
        otherinformation_data['responsibilities'] = data['miscTa2']
        otherinformation_data['Any_other_relevant_information'] = data['miscTa3']
        otherinformation_data['academic_year_break'] = data['miscTa4']
        otherinformation_data['awards_and_recognition'] = data['miscTa5']
        otherinformation_data['judicial_punishment'] = data['miscTa6']
        otherinformation_data['unfit_for_position'] = data['miscTa7']
        otherinformation_data['reference1'] = data['miscTa8']
        otherinformation_data['reference2'] = data['miscTa9']
        otherinformation_data['reference3'] = data['miscTa10']
        otherinformation_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        otherinformation_check = OtherInfo.objects.filter(applicant_id = application_number).count()
        # print("Other", otherinformation_check)
        if(otherinformation_check == 0):
            otherinformation_data['applicant_id'] = application_number
            OtherInfo.objects.create(**otherinformation_data)
        else:
            OtherInfo.objects.filter(applicant_id = application_number).update(**otherinformation_data)

        # # Signature
        signed_data = {}
        signed_data['place'] = data['signPlace']
        signed_data['date'] = datetime.datetime.now().date()
        if('signUpload' in request.FILES):
            signed_data['signature'] = request.FILES['signUpload']
        if('resumeUpload' in request.FILES):
            signed_data['resume'] = request.FILES['resumeUpload']
        if('receipt' in request.FILES):
            signed_data['receipt'] = request.FILES['receipt']
        signed_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        signed_data['payment_id']= data['payment_id']
        signed_check = Declaration.objects.filter(applicant_id = application_number).count()
        if(signed_check == 0):
            signed_data['applicant_id'] = application_number
            Declaration.objects.create(**signed_data)
        else:
            Declaration.objects.filter(applicant_id = application_number).update(**signed_data)

        # # Page 4
        # # Thesis
        thesis_data = {}
        thesis_data['ongoing_phd'] = data['ongoing_phd']
        thesis_data['completed_phd'] = data['completed_phd']
        thesis_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        thesis_check = Thesis.objects.filter(applicant_id = application_number).count()
        if(thesis_check == 0):
            thesis_data['applicant_id'] = application_number
            Thesis.objects.create(**thesis_data)
        else:
            Thesis.objects.filter(applicant_id = application_number).update(**thesis_data)

        # # Administrative Details
        administrative_details_data = {}
        administrative_details_data['administrative_details'] = data['administrative_details']
        administrative_details_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        administrative_check = AdministrativeDetails.objects.filter(applicant_id = application_number).count()
        if(administrative_check == 0):
            administrative_details_data['applicant_id'] = application_number
            AdministrativeDetails.objects.create(**administrative_details_data)
        else:
            AdministrativeDetails.objects.filter(applicant_id = application_number).update(**administrative_details_data)

        # # Patent
        patent_data = {}
        patent_data['patent_details'] = data['patent_details']
        patent_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        patent_check = Patent.objects.filter(applicant_id = application_number).count()
        if(patent_check == 0):
            patent_data['applicant_id'] = application_number
            Patent.objects.create(**patent_data)
        else:
            Patent.objects.filter(applicant_id = application_number).update(**patent_data)

        # # Summary
        summary_data = {}
        if(data['phd_defence_date'] == ''):
            summary_data['defence_date'] = 'N/A'
        else:
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
        summary_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        summary_check = Summary.objects.filter(applicant_id = application_number).count()
        if(summary_check == 0):
            summary_data['applicant_id'] = application_number
            Summary.objects.create(**summary_data)
        else:
            Summary.objects.filter(applicant_id = application_number).update(**summary_data)
        
        # # Sponsored Projects
        sponsored_projects_data = {}
        sponsored_projects_data['spo_tot_number'] = data['spo_tot_number']
        sponsored_projects_data['spo_ongoing'] = data['spo_ongoing']
        sponsored_projects_data['spo_completed'] = data['spo_completed']
        # print(data)
        if(data.get('spo_tot_number') != "0"):
            if('spofile' in request.FILES):
                sponsored_projects_data['spo_file'] = request.FILES['spofile']
        else:
            sponsored_projects_data['spo_file'] = "N/A"
        sponsored_projects_data['applicant'] = Applicant.objects.get(
            application_no=application_number)

        sponsored_projects_check = SponsoredProject.objects.filter(applicant_id = application_number).count()
        if(sponsored_projects_check == 0):
            sponsored_projects_data['applicant_id'] = application_number
            SponsoredProject.objects.create(**sponsored_projects_data)
        else:
            SponsoredProject.objects.filter(applicant_id = application_number).update(**sponsored_projects_data)
            # print(SponsoredProject.objects.filter(applicant_id = application_number).first())

        # # Experiments
        experiments_data = {}
        experiments_data['exp_tot_number'] = data['exp_tot_number']
        experiments_data['exp_ongoing'] = data['exp_ongoing']
        experiments_data['exp_completed'] = data['exp_completed']
        if(data.get('exp_tot_number') != "0"):
            if('expfile' in request.FILES):
                experiments_data['exp_file'] = request.FILES['expfile']
        else:
            experiments_data['exp_file'] = "N/A"
        experiments_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        experiments_check = Experiments.objects.filter(applicant_id = application_number).count()
        if(experiments_check == 0):
            experiments_data['applicant_id'] = application_number
            Experiments.objects.create(**experiments_data)
        else:
            Experiments.objects.filter(applicant_id = application_number).update(**experiments_data)

        # # Educational Qualifications
        phd_data = {}
        phd_data['PhD_awarded'] = data['awarded_phd']
        phd_data['applicant'] = Applicant.objects.get(
            application_no=application_number)
        if(data['awarded_phd'] == "No"):
            phd_data['PhD_details'] = "N/A"
            PhD.objects.create(**phd_data)
            ongoing_data = {}
            ongoing_data['PhD_title'] = "N/A"
            ongoing_data['Research_Domain'] = "N/A"
            ongoing_data['Institute_Name'] = "N/A"
            ongoing_data['University_Name'] = "N/A"
            ongoing_data['Registration_Date'] = "N/A"
            ongoing_data['supporting_documents'] = "N/A"
            ongoing_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            # PhDOngoing.objects.create(**ongoing_data)
            submitted_data = {}
            submitted_data['PhD_title'] = "N/A"
            submitted_data['Research_Domain'] = "N/A"
            submitted_data['Institute_Name'] = "N/A"
            submitted_data['University_Name'] = "N/A"
            submitted_data['Registration_Date'] = "N/A"
            submitted_data['Submission_Date'] = "N/A"
            submitted_data['supporting_documents'] = "N/A"
            submitted_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            # ThesisSubmitted.objects.create(**submitted_data)
            awarded_data = {}
            awarded_data['PhD_title'] = "N/A"
            awarded_data['Research_Domain'] = "N/A"
            awarded_data['Institute_Name'] = "N/A"
            awarded_data['University_Name'] = "N/A"
            awarded_data['Registration_Date'] = "N/A"
            awarded_data['Defense_Date'] = "N/A"
            awarded_data['supporting_documents'] = "N/A"
            awarded_data['applicant'] = Applicant.objects.get(
                application_no=application_number)
            # PhDAwarded.objects.create(**awarded_data)
        else:
            if('phd' in data):
                phd_data['PhD_details'] = data['phd']
                phd_data['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                PhD.objects.create(**phd_data)
                if(data['phd'] == "Ongoing"):
                    # ongoing_data = {}
                    # ongoing_data['PhD_title'] = data['ongoing1-title']
                    # ongoing_data['Research_Domain'] = data['ongoing1-domain']
                    # ongoing_data['Institute_Name'] = data['ongoing1-institute']
                    # ongoing_data['University_Name'] = data['ongoing1-university']
                    # ongoing_data['Registration_Date'] = data['ongoing1-date']
                    # ongoing_data['supporting_documents'] = request.FILES['ongoing1-file']
                    # ongoing_data['applicant'] = Applicant.objects.get(
                    #     application_no=application_number)
                    # PhDOngoing.objects.create(**ongoing_data)
                    # submitted_data = {}
                    # submitted_data['PhD_title'] = "N/A"
                    # submitted_data['Research_Domain'] = "N/A"
                    # submitted_data['Institute_Name'] = "N/A"
                    # submitted_data['University_Name'] = "N/A"
                    # submitted_data['Registration_Date'] = "N/A"
                    # submitted_data['Submission_Date'] = "N/A"
                    # submitted_data['supporting_documents'] = "N/A"
                    # submitted_data['applicant'] = Applicant.objects.get(
                        # application_no=application_number)
                    # ThesisSubmitted.objects.create(**submitted_data)
                    # awarded_data = {}
                    # awarded_data['PhD_title'] = "N/A"
                    # awarded_data['Research_Domain'] = "N/A"
                    # awarded_data['Institute_Name'] = "N/A"
                    # awarded_data['University_Name'] = "N/A"
                    # awarded_data['Registration_Date'] = "N/A"
                    # awarded_data['Defense_Date'] = "N/A"
                    # awarded_data['supporting_documents'] = "N/A"
                    # awarded_data['applicant'] = Applicant.objects.get(
                        # application_no=application_number)
                    # PhDAwarded.objects.create(**awarded_data)
                    num_of_submitted_records = list(
                        filter(lambda s: 'ongoing' in s, list(data.keys())))
                    print(num_of_submitted_records)
                    num_of_submitted_records_length = len(num_of_submitted_records)
                    last_awarded_record = num_of_submitted_records[num_of_submitted_records_length-6]
                    file_list = list(PhDOngoing.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
                    PhDOngoing.objects.filter(applicant_id = application_number).delete()
                    number_awarded_record = last_awarded_record[7]
                    # print(last_awarded_record)
                    for i in range(1, int(number_awarded_record)+1):
                        if(data.get('ongoing'+str(i) + '-title', False) == False):
                            continue
                        else:
                            submitted_data = {}
                            submitted_data['PhD_title'] = data.get(
                                'ongoing' + str(i) + '-title')
                            submitted_data['Research_Domain'] = data.get(
                                'ongoing' + str(i) + '-domain')
                            submitted_data['Institute_Name'] = data.get(
                                'ongoing' + str(i) + '-institute')
                            submitted_data['University_Name'] = data.get(
                                'ongoing' + str(i) + '-university')
                            submitted_data['Registration_Date'] = data.get(
                                'ongoing' + str(i) + '-date')
                            ans = 'ongoing' + str(i) + '-file'
                            if(i <= len(file_list)):
                                submitted_data['supporting_documents']=file_list[i-1]
                            if( ans in request.FILES ):
                                submitted_data['supporting_documents'] = request.FILES[ans]
                            submitted_data['applicant'] = Applicant.objects.get(
                                application_no=application_number)
                            PhDOngoing.objects.create(**submitted_data)
                elif(data['phd'] == "Thesis Submitted"):
                    ongoing_data = {}
                    ongoing_data['PhD_title'] = "N/A"
                    ongoing_data['Research_Domain'] = "N/A"
                    ongoing_data['Institute_Name'] = "N/A"
                    ongoing_data['University_Name'] = "N/A"
                    ongoing_data['Registration_Date'] = "N/A"
                    ongoing_data['supporting_documents'] = "N/A"
                    ongoing_data['applicant'] = Applicant.objects.get(
                        application_no=application_number)
                    # PhDOngoing.objects.create(**ongoing_data)
                    num_of_submitted_records = list(
                        filter(lambda s: 'thesis' in s, list(data.keys())))
                    num_of_submitted_records_length = len(num_of_submitted_records)
                    last_awarded_record = num_of_submitted_records[num_of_submitted_records_length-1]
                    file_list = list(ThesisSubmitted.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
                    ThesisSubmitted.objects.filter(applicant_id = application_number).delete()
                    number_awarded_record = last_awarded_record[6]
                    for i in range(1, int(number_awarded_record)+1):
                        if(data.get('thesis'+str(i) + '-title', False) == False):
                            continue
                        else:
                            submitted_data = {}
                            submitted_data['PhD_title'] = data.get(
                                'thesis' + str(i) + '-title')
                            submitted_data['Research_Domain'] = data.get(
                                'thesis' + str(i) + '-domain')
                            submitted_data['Institute_Name'] = data.get(
                                'thesis' + str(i) + '-institute')
                            submitted_data['University_Name'] = data.get(
                                'thesis' + str(i) + '-university')
                            submitted_data['Registration_Date'] = data.get(
                                'thesis' + str(i) + '-regdate')
                            submitted_data['Submission_Date'] = data.get(
                                'thesis' + str(i) + '-subdate')
                            ans = 'thesis' + str(i) + '-file'
                            if(i <= len(file_list)):
                                submitted_data['supporting_documents']=file_list[i-1]
                            if( ans in request.FILES ):
                                submitted_data['supporting_documents'] = request.FILES[ans]
                            submitted_data['applicant'] = Applicant.objects.get(
                                application_no=application_number)
                            ThesisSubmitted.objects.create(**submitted_data)
                    # awarded_data = {}
                    # awarded_data['PhD_title'] = "N/A"
                    # awarded_data['Research_Domain'] = "N/A"
                    # awarded_data['Institute_Name'] = "N/A"
                    # awarded_data['University_Name'] = "N/A"
                    # awarded_data['Registration_Date'] = "N/A"
                    # awarded_data['Defense_Date'] = "N/A"
                    # awarded_data['supporting_documents'] = "N/A"
                    # awarded_data['applicant'] = Applicant.objects.get(
                    #     application_no=application_number)
                    # PhDAwarded.objects.create(**awarded_data)
                elif(data['phd'] == "Awarded"):
                    ongoing_data = {}
                    ongoing_data['PhD_title'] = "N/A"
                    ongoing_data['Research_Domain'] = "N/A"
                    ongoing_data['Institute_Name'] = "N/A"
                    ongoing_data['University_Name'] = "N/A"
                    ongoing_data['Registration_Date'] = "N/A"
                    ongoing_data['supporting_documents'] = "N/A"
                    ongoing_data['applicant'] = Applicant.objects.get(
                        application_no=application_number)
                    # PhDOngoing.objects.create(**ongoing_data)
                    submitted_data = {}
                    submitted_data['PhD_title'] = "N/A"
                    submitted_data['Research_Domain'] = "N/A"
                    submitted_data['Institute_Name'] = "N/A"
                    submitted_data['University_Name'] = "N/A"
                    submitted_data['Registration_Date'] = "N/A"
                    submitted_data['Submission_Date'] = "N/A"
                    submitted_data['supporting_documents'] = "N/A"
                    submitted_data['applicant'] = Applicant.objects.get(
                        application_no=application_number)
                    ThesisSubmitted.objects.create(**submitted_data)
                    num_of_awarded_records = list(
                        filter(lambda s: 'awarded' in s, list(data.keys())))
                    num_of_awarded_records_length = len(num_of_awarded_records)
                    last_awarded_record = num_of_awarded_records[num_of_awarded_records_length-1]
                    number_awarded_record = last_awarded_record[7]
                    file_list = list(PhDAwarded.objects.filter(applicant_id=application_number).values_list('supporting_documents',flat=True))
                    PhDAwarded.objects.filter(applicant_id = application_number).delete()
                    for i in range(1, int(number_awarded_record)+1):
                        if(data.get('awarded'+str(i) + '-title', False) == False):
                            continue
                        else:
                            awarded_data = {}
                            awarded_data['PhD_title'] = data.get(
                                'awarded'+str(i)+'-title', False)
                            awarded_data['Research_Domain'] = data.get(
                                'awarded'+str(i)+'-domain', False)
                            awarded_data['Institute_Name'] = data.get(
                                'awarded'+str(i)+'-institute', False)
                            awarded_data['University_Name'] = data.get(
                                'awarded'+str(i)+'-university', False)
                            awarded_data['Registration_Date'] = data.get(
                                'awarded'+str(i)+'-regdate', False)
                            awarded_data['Defense_Date'] = data.get(
                                'awarded'+str(i)+'-defdate', False)
                            ans = 'awarded'+str(i)+'-file'
                            if( i <= len(file_list)):
                                awarded_data['supporting_documents'] = file_list[i-1]
                            if( ans in request.FILES):
                                awarded_data['supporting_documents'] = request.FILES[ans]
                            awarded_data['applicant'] = Applicant.objects.get(
                                application_no=application_number)
                            PhDAwarded.objects.create(**awarded_data)

        # # Academic Details
        num_of_academic_records = list(
            filter(lambda s: 'course' in s, list(data.keys())))
        
        num_of_academic_records_length = len(num_of_academic_records)
        last_academic_record = num_of_academic_records[num_of_academic_records_length-1]
        number_academic_record = last_academic_record[6]
        # print(list(last_academic_record))
        # print(request.FILES.items())
        # print(num_of_academic_records, last_academic_record, data.get('course'+str(5), False), "Checking print")
        academic_details_check = EducationalQualifications.objects.filter(applicant_id = application_number).count()
        file_list = list(EducationalQualifications.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        # print("Reached here")
        if(academic_details_check != 0):
            # print("deleteing all records")
            EducationalQualifications.objects.filter(applicant_id = application_number).delete()
        # print("Going to create tables for academic details")
        for i in range(1, int(number_academic_record)+1):
            
            if (data.get('course'+str(i), False) == "" or data.get('course'+str(i), False) == False):
                continue
                
            else:
                academic_details = {}
                academic_details['degree'] = data.get('course'+str(i), False)
                academic_details['equivalent_to'] = data.get(
                    'course' + str(i) + '-equivalent', False)
                academic_details['name'] = data.get(
                    'course'+str(i)+'-name', False)
                academic_details['marks'] = data.get(
                    'course'+str(i)+'-percentage', False)
                academic_details['obtained'] = data.get(
                    'course'+str(i)+'-obtained', False)
                academic_details['subjects'] = data.get(
                    'course'+str(i)+'-subject', False)
                academic_details['year_of_passing'] = data.get(
                    'yearOfPassing'+str(i), False)
                ans = 'course' + str(i) + '-file'
                # if(!request.FILES[ans])
                if(i<=len(file_list)):
                    academic_details['supporting_documents'] = file_list[i-1]
                if( ans in request.FILES):
                    academic_details['supporting_documents'] = request.FILES[ans]
                
                academic_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                academic_details['applicant_id'] = application_number
                # print("~~~~~~", academic_details, "~~~~~~")
                # if(academic_details_check  == 0):
                EducationalQualifications.objects.create(**academic_details)
                # else:
                    # academic_details_check = EducationalQualifications.objects.filter(applicant_id = application_number).update(**academic_details)            
            # if re.search(r'[12]\d{3}',data.get('yearOfPassing-'+str(i),False)) is None:
            #     return render(request, 'recruitment/form.html',{'message':'Enter the year in Academic details in yyyy format.'})
            # if 0 <= float(data.get('course-'+str(i)+'-marks',False)) <= 100:
            #     academic_details['marks']  = data.get('course-'+str(i)+'-marks',False)
            # else:
            #     return render(request, 'recruitment/form.html',{'message':'Enter your percentage in Academic details a value between 0 to 100.'})

        # # Professional
        num_of_professional_records = list(
            filter(lambda s: 'org' in s, list(data.keys())))
        last_professional_record = num_of_professional_records[len(
            num_of_professional_records)-1]
        number_professional_record = last_professional_record[3]
        employmentExp_check = EmploymentExp.objects.filter(applicant_id = application_number).count()
        file_list = list(EmploymentExp.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        if(employmentExp_check !=0):
            EmploymentExp.objects.filter(applicant_id = application_number).delete()
        for i in range(1, int(number_professional_record)+1):
            if (data.get('org' + str(i) + '-name') == ""):
                professional_details = {}
                professional_details['name'] = "N/A"
                professional_details['post'] = "N/A"
                professional_details['from_year'] = "N/A"
                professional_details['to_year'] = "N/A"
                professional_details['salary'] = "N/A"
                professional_details['nature'] = "N/A"
                professional_details['supporting_documents'] = "N/A"
                professional_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                professional_details['applicant_id'] = application_number
                EmploymentExp.objects.create(**professional_details)
                # if(employmentExp_check == 0):
                # else:
                #     EmploymentExp.objects.filter(applicant_id = application_number).update(**professional_details)
            else:
                professional_details = {}
                professional_details['name'] = data.get(
                    'org' + str(i) + '-name', False)
                professional_details['post'] = data.get(
                    'org' + str(i) + '-post', False)
                professional_details['from_year'] = data.get(
                    'org' + str(i) + '-from', False)
                professional_details['to_year'] = data.get(
                    'org' + str(i) + '-to', False)
                professional_details['salary'] = data.get(
                    'org' + str(i) + '-salary', False)
                professional_details['nature'] = data.get(
                    'org' + str(i) + '-nature', False)
                ans = 'org' + str(i) + '-file'
                if(i <= len(file_list)):
                    professional_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    professional_details['supporting_documents'] = request.FILES[ans]
                employmentExp_check = EmploymentExp.objects.filter(applicant_id = application_number).count()
                professional_details['applicant_id'] = application_number
                EmploymentExp.objects.create(**professional_details)
                # if(employmentExp_check == 0):
                # else:
                #     EmploymentExp.objects.filter(applicant_id = application_number).update(**professional_details)

        # # Books
        num_of_books_records = list(
            filter(lambda s: 'books' in s, list(data.keys())))
        # print(num_of_books_records)
        last_book_record = num_of_books_records[len(num_of_books_records)-1]
        number_books_record = last_book_record[5]
        # books_data = []
        # print("Boooks Data:", num_of_books_records, "\n\n")
        books_check = Books.objects.filter(applicant_id = application_number).count()
        file_list = list(Books.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))

        if(books_check != 0):
            Books.objects.filter(applicant_id = application_number).delete()
        for i in range(1, int(number_books_record)+1):
            if(data.get('books' + str(i) + '-title') == ""):
                books_details = {}
                books_details['title'] = "N/A"
                books_details['author'] = "N/A"
                books_details['publisher'] = "N/A"
                books_details['date_publish'] = "N/A"
                books_details['isbn'] = "N/A"
                books_details['supporting_documents'] = "N/A"
                books_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                books_details['applicant_id'] = application_number
                Books.objects.create(**books_details)
                # if(books_check == 0):
                # else:
                #     Books.objects.filter(applicant_id = application_number).update(**books_details)
            else:
                books_details = {}
                books_details['title'] = data.get(
                    'books' + str(i) + '-title', False)
                books_details['author'] = data.get(
                    'books' + str(i) + '-author', False)
                books_details['publisher'] = data.get(
                    'books' + str(i) + '-publisher', False)
                books_details['date_publish'] = data.get(
                    'books' + str(i) + '-date', False)
                books_details['isbn'] = data.get(
                    'books' + str(i) + '-number', False)
                ans = 'books' + str(i) + '-file'
                if(i <= len(file_list)):
                    books_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    books_details['supporting_documents'] = request.FILES[ans]
                # books_details['supporting_documents'] = request.FILES[ans]
                books_check = Books.objects.filter(applicant_id = application_number).count()
                books_details['applicant_id'] = application_number
                Books.objects.create(**books_details)
                # if(books_check == 0):
                # else:
                #     Books.objects.filter(applicant_id = application_number).update(**books_details)

        # # Chapters
        num_of_chapters_records = list(
            filter(lambda s: 'chapters' in s, list(data.keys())))
        last_chapter_record = num_of_chapters_records[len(
            num_of_chapters_records)-1]
        number_chapter_record = last_chapter_record[8]
        file_list = list(Chapters.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))

        # print("Chapters Data:", num_of_chapters_records, "\n\n")
        chapter_check = Chapters.objects.filter(applicant_id = application_number).count()
        if(chapter_check != 0):
            Chapters.objects.filter(applicant_id = application_number).delete()
        for i in range(1, int(number_chapter_record)+1):
            if(data.get('chapters' + str(i) + '-book_title') == ""):
                chapter_details = {}
                chapter_details['book_title'] = "N/A"
                chapter_details['chapter'] = "N/A"
                chapter_details['author'] = "N/A"
                chapter_details['publisher'] = "N/A"
                chapter_details['date_of_publisher'] = "N/A"
                chapter_details['isbn_issn'] = "N/A"
                chapter_details['supporting_documents'] = "N/A"
                chapter_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                chapter_details['applicant_id'] = application_number
                Chapters.objects.create(**chapter_details)
                # if(chapter_check == 0):
                # else:
                #     Chapters.objects.filter(applicant_id = application_number).update(**chapter_details)
            else:
                chapter_details = {}
                chapter_details['book_title'] = data.get(
                    'chapters' + str(i) + '-book_title', False)
                chapter_details['chapter'] = data.get(
                    'chapters' + str(i) + '-chapter', False)
                chapter_details['author'] = data.get(
                    'chapters' + str(i) + '-author', False)
                chapter_details['publisher'] = data.get(
                    'chapters' + str(i) + '-publisher', False)
                chapter_details['date_of_publisher'] = data.get(
                    'chapters' + str(i) + '-date_of_publisher', False)
                chapter_details['isbn_issn'] = data.get(
                    'chapters' + str(i) + '-number', False)
                ans = 'chapters' + str(i)+'-file'
                if(i <= len(file_list)):
                    chapter_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    chapter_details['supporting_documents'] = request.FILES[ans]
                
                # chapter_details['supporting_documents'] = request.FILES['chapters' +
                #                                                         str(i)+'-file']
                chapter_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                chapter_check = Chapters.objects.filter(applicant_id = application_number).count()
                chapter_details['applicant_id'] = application_number
                Chapters.objects.create(**chapter_details)
                # if(chapter_check == 0):
                # else:
                #     Chapters.objects.filter(applicant_id = application_number).update(**chapter_details)

        # # Newspapers Articles
        num_of_news_articles_records = list(
            filter(lambda s: 'news_articles' in s, list(data.keys())))
        last_news_articles_record = num_of_news_articles_records[len(
            num_of_news_articles_records)-1]
        number_news_articles_record = last_news_articles_record[13]
        news_articles_check = NewspaperArticle.objects.filter(applicant_id = application_number).count()
        file_list = list(NewspaperArticle.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        if(news_articles_check != 0):
            NewspaperArticle.objects.filter(applicant_id = application_number).delete()
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
                news_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                news_articles_details['applicant_id'] = application_number
                NewspaperArticle.objects.create(**news_articles_details)
                # if(news_articles_check == 0):
                # else:
                #     NewspaperArticle.objects.filter(applicant_id = application_number).update(**news_articles_details)
            else:
                news_articles_details = {}
                news_articles_details['article_title'] = data.get(
                    'news_articles' + str(i) + '-article_title', False)
                news_articles_details['journal_name'] = data.get(
                    'news_articles' + str(i) + '-journal_name', False)
                news_articles_details['author'] = data.get(
                    'news_articles' + str(i) + '-author', False)
                news_articles_details['date_published'] = data.get(
                    'news_articles' + str(i) + '-date_published', False)
                news_articles_details['vol_no'] = data.get(
                    'news_articles' + str(i) + '-page')
                news_articles_details['referred'] = data.get(
                    'news_articles' + str(i) + '-referred', False)
                news_articles_details['naas'] = data.get(
                    'news_articles' + str(i) + '-impact', False)
                ans = 'news_articles'+str(i)+'-file'
                if(i <= len(file_list)):
                    news_articles_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    news_articles_details['supporting_documents'] = request.FILES[ans]
                
                # news_articles_details['supporting_documents'] = request.FILES['news_articles'+str(
                #     i)+'-file']
                news_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                news_articles_check = NewspaperArticle.objects.filter(applicant_id = application_number).count()
                news_articles_details['applicant_id'] = application_number
                NewspaperArticle.objects.create(**news_articles_details)
                # if(news_articles_check == 0):
                # else:
                #     NewspaperArticle.objects.filter(applicant_id = application_number).update(**news_articles_details)

        # # Seminar Articles
        num_of_seminar_articles = list(
            filter(lambda s: 'semi_articles' in s, list(data.keys())))
        last_semi_articles_record = num_of_seminar_articles[len(
            num_of_seminar_articles)-1]
        number_semi_articles_record = last_semi_articles_record[13]
        file_list = list(SeminarArticles.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))

        seminar_articles_check = SeminarArticles.objects.filter(applicant_id = application_number).count()
        if(seminar_articles_check != 0):
            SeminarArticles.objects.filter(applicant_id = application_number).delete()
        for i in range(1, int(number_semi_articles_record)+1):
            if(data.get('semi_articles' + str(i) + '-article_title') == ""):
                seminar_articles_details = {}
                seminar_articles_details['article_title'] = "N/A"
                seminar_articles_details['seminar_subject'] = "N/A"
                seminar_articles_details['location'] = "N/A"
                seminar_articles_details['From'] = "N/A"
                seminar_articles_details['to'] = "N/A"
                seminar_articles_details['published'] = "N/A"
                seminar_articles_details['supporting_documents'] = "N/A"
                seminar_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                seminar_articles_details['applicant_id'] = application_number
                SeminarArticles.objects.create(**seminar_articles_details)
                # if(seminar_articles_check == 0):
                # else:
                #     SeminarArticles.objects.filter(applicant_id = application_number).update(**seminar_articles_details)
            else:
                seminar_articles_details = {}
                seminar_articles_details['article_title'] = data.get(
                    'semi_articles' + str(i) + '-article_title', False)
                seminar_articles_details['seminar_subject'] = data.get(
                    'semi_articles' + str(i) + '-seminar_subject', False)
                seminar_articles_details['location'] = data.get(
                    'semi_articles' + str(i) + '-location', False)
                seminar_articles_details['From'] = data.get(
                    'semi_articles' + str(i) + '-from', False)
                seminar_articles_details['to'] = data.get(
                    'semi_articles' + str(i) + '-to', False)
                seminar_articles_details['published'] = data.get(
                    'semi_articles' + str(i) + '-published', False)
                seminar_articles_details['supporting_documents'] = "N/A"
                ans = 'semi_articles'+str(i)+'-file'
                if(i <= len(file_list)):
                    seminar_articles_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    seminar_articles_details['supporting_documents'] = request.FILES[ans]
                
                seminar_articles_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                seminar_articles_check = SeminarArticles.objects.filter(applicant_id = application_number).count()
                seminar_articles_details['applicant_id'] = application_number
                SeminarArticles.objects.create(**seminar_articles_details)
                # if(seminar_articles_check == 0):
                # else:
                #     SeminarArticles.objects.filter(applicant_id = application_number).update(**seminar_articles_details)

        # # Research Experience
        num_of_research_exp = list(
            filter(lambda s: 'exper' in s, list(data.keys())))
        last_research_exp_record = num_of_research_exp[len(
            num_of_research_exp) - 1]
        number_research_exp_record = last_research_exp_record[5]
        
        
        research_exp_check = ResearchExp.objects.filter(applicant_id = application_number).count()
        file_list=list(ResearchExp.objects.filter(applicant_id = application_number).values_list('supporting_documents',flat=True))
        if(research_exp_check != 0):
            # print("deleteing all records")
            ResearchExp.objects.filter(applicant_id = application_number).delete()
        for i in range(1, int(number_research_exp_record)+1):
            if(data.get('exper' + str(i) + '-from') == ""):
                research_exp_details = {}
                research_exp_details['From'] = "N/A"
                research_exp_details['to'] = "N/A"
                research_exp_details['number_of_months'] = "N/A"
                research_exp_details['supporting_documents'] = "N/A"
                research_exp_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                research_exp_check = ResearchExp.objects.filter(applicant_id = application_number).count()
                research_exp_details['applicant_id'] = application_number
                ResearchExp.objects.create(**research_exp_details)
                # if(research_exp_check == 0):
                # else:
                #     ResearchExp.objects.filter(applicant_id = application_number).update(**research_exp_details)
            else:
                research_exp_details = {}
                research_exp_details['From'] = data.get(
                    'exper' + str(i) + '-from', False)
                research_exp_details['to'] = data.get(
                    'exper' + str(i) + '-to', False)
                research_exp_details['number_of_months'] = data.get(
                    'exper' + str(i) + '-months', False)
                ans = 'exper' + str(i) + '-file'
                if(i <= len(file_list)):
                    research_exp_details['supporting_documents'] = file_list[i-1]
                if(ans in request.FILES):
                    research_exp_details['supporting_documents'] = request.FILES[ans]
                research_exp_details['applicant'] = Applicant.objects.get(
                    application_no=application_number)
                research_exp_check = ResearchExp.objects.filter(applicant_id = application_number).count()
                research_exp_details['applicant_id'] = application_number
                ResearchExp.objects.create(**research_exp_details)
                # if(research_exp_check == 0):
                # else:
                #     ResearchExp.objects.filter(applicant_id = application_number).update(**research_exp_details)
        return HttpResponseRedirect('/viewApplication/' + application_number)
    return render(request, 'recruitment/form.html', {})