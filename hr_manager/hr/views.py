from django.shortcuts import redirect, render
from django.http import HttpResponse, QueryDict
from .models import Employee, Employer
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


# def homepage(req):
#     return render(
#         req,
#         'homepage.html',
#     )


# def employers(req):
#     all_employers = Employer.objects.all()
#     return render(
#         req,
#         'employers.html',
#         {
#             'employers': all_employers
#         }
#     )


# def users(req):
#     all_users = User.objects.all()
#     return render(
#         req,
#         'users.html',
#         {
#             'users': all_users
#         }
#     )


# def employees(req, id_employer):
#     all_users = User.objects.all()
#     all_employers = Employer.objects.all()
#     all_emplyees = Employee.objects.all()

#     curent_employer = all_employers.filter(id=id_employer).first()

#     people_hired_qs = all_emplyees.values_list('user', flat=True)

#     employees_for_current_employer = all_emplyees.filter(
#         employer=curent_employer)
#     qs = employees_for_current_employer.values_list('user', flat=True)
#     users_hired = all_users.filter(id__in=qs)

#     users_not_hired = all_users.exclude(id__in=people_hired_qs)

#     new_user_list = []
#     new_user_list.extend(
#         list(
#             map(
#                 lambda hired_user: {'id': hired_user.id, 'first_name': hired_user.first_name,
#                                     'last_name': hired_user.last_name, 'email': hired_user.email, 'hired': True},
#                 users_hired
#             )
#         )
#     )
#     new_user_list.extend(
#         list(
#             map(
#                 lambda not_hired_user: {'id': not_hired_user.id, 'first_name': not_hired_user.first_name,
#                                         'last_name': not_hired_user.last_name, 'email': not_hired_user.email, 'hired': False},
#                 users_not_hired
#             )
#         )
#     )

#     return render(
#         req,
#         'employees.html',
#         {
#             'curent_employer': curent_employer,
#             'users': new_user_list,
#             'employers': all_employers,

#         }
#     )


# def employees_redirect(req):
#     return redirect('/employees/0')


# @ csrf_exempt
# def fire_employee(req):
#     try:
#         if(req.method != 'POST'):
#             raise Exception('Method not allowed')

#         body = json.loads(req.body.decode('utf-8'))
#         user = User.objects.get(id=int(body['user_id']))
#         employer = Employer.objects.get(id=int(body['employer_id']))

#         curent_employee = Employee.objects.filter(
#             user=user, employer=employer).first()
#         curent_employee.delete()

#     except Exception:
#         pass
#     finally:
#         return redirect('/employees/'+str(employer.id))


# @ csrf_exempt
# def add_new_employee(req):
#     try:
#         if(req.method != 'POST'):
#             raise Exception('Method not allowed')

#         body = json.loads(req.body.decode('utf-8'))

#         user = User.objects.get(id=int(body['user_id']))
#         employer = Employer.objects.get(id=int(body['employer_id']))
#         new_employee = Employee(user=user, employer=employer)

#         new_employee.save()
#     except Exception as e:
#         print('this is a test \n\n\n\n')
#         print(e)
#     finally:
#         return redirect('/employees'+str(employer.id))


# @ csrf_exempt
# def merge_employer(req):
#     try:

#         if (req.method != 'POST'):
#             return HttpResponse('Method not allowed')
#         # new_employer = Employer()
#         query_dict = QueryDict(req.body.decode('utf-8'))
#         try:
#             new_employer = Employer.objects.get(id=int(query_dict.get('id')))
#         except Exception:
#             new_employer = Employer()
#         finally:
#             new_employer.name = query_dict.get('name')
#             new_employer.wage = query_dict.get('wage')
#             new_employer.save()
#     except Exception:
#         pass
#     finally:
#         return redirect('/employers')


# @ csrf_exempt
# def delete_employer_asd(req, employer_id):
#     try:
#         if(req.method != 'DELETE'):
#             return HttpResponse('Method not allowed')
#         employer = Employer.objects.get(id=employer_id)
#         employer.delete()
#     except Exception:
#         pass
#     finally:
#         return redirect('/employers')


# @ csrf_exempt
# def merge_user(req):
#     try:
#         if (req.method != 'POST'):
#             return HttpResponse('Method not allowed')

#         query_dict = QueryDict(req.body.decode('utf-8'))
#         try:
#             new_user = User.objects.get(id=int(query_dict.get('id')))
#         except Exception:
#             new_user = User()
#         finally:
#             new_user.first_name = query_dict.get('fname')
#             new_user.last_name = query_dict.get('lname')
#             new_user.email = query_dict.get('email')
#             new_user.save()

#     except Exception:
#         pass
#     finally:
#         return redirect('/users')


# @ csrf_exempt
# def delete_user(req, user_id):
#     try:
#         if(req.method != 'DELETE'):
#             return HttpResponse('Method not allowed')
#         user = User.objects.get(id=user_id)
#         user.delete()
#     except Exception:
#         pass
#     finally:
#         return redirect('/users')


# @ csrf_exempt
# def hire_user(req):
#     try:
#         if(req.method != 'POST'):
#             return HttpResponse('Method not allowed')
#         query_dict = QueryDict(req.body.decode('utf-8'))
#         employee = Employee()
#         employee.user_id = query_dict.get('user_id')
#         employee.employer_id = query_dict.get('employer_id')
#         employee.save()
#     except Exception:
#         pass
#     finally:
#         return redirect('/employees')
