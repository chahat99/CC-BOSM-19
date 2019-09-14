from google.oauth2 import id_token
from django.http import JsonResponse, HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import *
from google.auth.transport import requests as google_request
from django.shortcuts import render
import SportsCrypt.keyconfig as senv
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import login as auth_login

# team edit view


def renderLogin(request):
    return render(request, 'google_sign-in.html')


def renderToken(request):
    return HttpResponse('Logged in')


@login_required
def question1(request):
    return render(request, 'question-1.html')


@login_required
def question2(request):
    return render(request, 'question-2.html')


@login_required
def question3(request):
    return render(request, 'question-3.html')


@login_required
def question4(request):
    return render(request, 'question-4.html')


@login_required
def questionmain(request):
    return render(request, 'question-main.html')


@login_required
def formteam(request):
    return render(request, 'Code.html')


@login_required
def startgame(request):
    return render(request, 'StartGame.html')


@login_required
def teamname(request):
    return render(request, 'TeamName.html')


def renderFile(request, filename):
    try:
        print(request.user.username)
    except Exception:
        print('not logged in')
    return render(request, filename)


@csrf_exempt
def getData(request):
    if request.method == 'POST':
        print(request.body)
        return JsonResponse({'flag': 1})
    if request.method == 'GET':
        return JsonResponse({'question': 'dummy', 'team_name': 'dummy'})


@csrf_exempt
def login(request):

    if request.method == 'POST':

        try:                # just to decode JSON properly
            print(request.body)
            data = json.loads(request.body.decode('utf8').replace("'", '"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

        try:
            token = data['token']
        except KeyError as missing_data:
            return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), "status": 0})

        try:
            idinfo = id_token.verify_oauth2_token(
                token, google_request.Request(), senv.CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            email = idinfo['email']
            try:
                user = User.objects.get(username=email.split('@')[0])
            except User.DoesNotExist:
                user = User.objects.create_user(username=email.split('@')[0])
            except:
                return JsonResponse({"message": "Invalid ID Token passed!", "status": 0})

            auth_login(request, user)
            try:
                participant = Participant.objects.get(user=user, email=email)
                if participant.team:
                    return JsonResponse({"message": "User Login Successful!", "status": 2, "participant_id": participant.unique_id})
                else:
                    return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant_id": participant.unique_id})
            except Participant.DoesNotExist:
                participant = Participant.objects.create(user=user, email=email)
                return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant_id": participant.unique_id})

        except ValueError:
            # Invalid token
            return JsonResponse({"message": "Invalid ID Token passed!", "status": 0})


@csrf_exempt
def create_team(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                participant = Participant.objects.get(user=request.user)
                print("here")
                # if participant.team:
                #     return JsonResponse({"message": "User Login Successful!", "status": 2, "participant_id": participant.unique_id})
                # else:
                #     return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant_id": participant.unique_id})
            except Participant.DoesNotExist:
                print('here1')
                participant = Participant.objects.create(user=request.user)
                # return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant_id": participant.unique_id})
            # try:
            #     authorization = str(request.META['HTTP_X_AUTHORIZATION'])
            # except KeyError:
            #     return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

            # if authorization != senv.AUTHORIZATION:
            #     return JsonResponse({"message": "Invalid Request Source", "status": 0})
            print(request.user.username)
            try:
                print(request.body)
                data = json.loads(request.body.decode('utf8'))
            except Exception:
                return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

            try:
                # part_id = data['participant_id']
                team_name = data['teamname']
            except KeyError as missing_data:
                return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

            try:
                team = Team.objects.create(name=team_name)
                team.participant_count += 1
                team.save()
            except Exception:
                return JsonResponse({'message': 'Team could not be Formed', 'status': 0})

            try:
                print('Hello1')
                participant = Participant.objects.get(user=request.user)
                print('Hello1')
                participant.team = team
                print('Hello1')
                participant.save()
                print('Hello1')
                print(team.name + str(team.code))
                return JsonResponse({'message': 'Team Formed', 'team_name': team.name, 'team_code': team.code, 'status': 1})
            except Exception as e:
                print(str(e))
                return JsonResponse({'message': 'Participant could not be Updated', 'status': 0})
        else:
            print('no user')


@csrf_exempt
def getPinCode(request):
    if request.method == 'GET':
        try:
            if request.user.is_authenticated:
                participant = Participant.objects.get(user=request.user)
                team_code = participant.team.code
                return JsonResponse({'message': 'PinCode Sent', 'pincode': team_code, 'status': 1})
            raise Exception
        except Exception:
            return JsonResponse({'message': 'PinCode Failed',  'status': 0})


@csrf_exempt
def join_team(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                participant = Participant.objects.get(user=request.user)
                print("here")
                # if participant.team:
                #     return JsonResponse({"message": "User Login Successful!", "status": 2, "participant_id": participant.unique_id})
                # else:
                #     return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant_id": participant.unique_id})
            except Participant.DoesNotExist:
                print('here1')
                participant = Participant.objects.create(user=request.user)
            # try:
            #     authorization = str(request.META['HTTP_X_AUTHORIZATION'])
            # except KeyError:
            #     return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

            # if authorization != senv.AUTHORIZATION:
            #     return JsonResponse({"message": "Invalid Request Source", "status": 0})

            try:
                data = json.loads(request.body.decode('utf8'))
            except Exception:
                return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

            try:
                # part_id = data['participant_id']
                code = data['pin']
            except KeyError as missing_data:
                return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

            try:
                team = Team.objects.get(code=code)
            except Team.DoesNotExist:
                return JsonResponse({'message': 'Invalid Team Code', 'status': 0})

            if team.participant_count == 14:
                return JsonResponse({'message': 'Team Participant Limit Reached.', 'status': 0})

            try:
                participant = Participant.objects.get(user=request.user)
            except Participant.DoesNotExist:
                return JsonResponse({'message': 'Invalid Participant ID', 'status': 0})

            try:
                participant.team = team
                participant.save()
                team.participant_count += 1
                team.save()
                return JsonResponse({'message': 'Team Formed', 'team_name': team.name, 'team_code': team.code, 'status': 1})
            except Exception as e:
                return JsonResponse({'message': str(e), 'status': 0})


@csrf_exempt
def question_details(request):
    if request.method == 'GET':
        # try:
        #     authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        # except KeyError:
        #     return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        # if authorization != senv.AUTHORIZATION:
        #     return JsonResponse({"message": "Invalid Request Source", "status": 0})

        # try:
        pk = Participant.objects.get(user=request.user).team.state
        print(pk)
        question = Question.objects.get(myid=pk).question
        print(str(question))
        if pk == 6 or pk == 7 or pk == 8:
            if Answer.objects.get(question__question=question).times_answered <= 2*(9-pk)-1:
                return JsonResponse({"message": "Question Sent Successfully", "Question": question, "status": 1})
            else:

                return JsonResponse({"message": "Question Sent Successfully", "Question": "Answer Limit has been Reached.", "status": 0})
        else:
            return JsonResponse({"message": "Question Sent Successfully", "Question": question, "status": 1})
        # except Exception:
        # return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

        # try:
        #     with transaction.atomic():
        #         participant = Participant.objects.get(user=request.user)
        #         req_question = Question.objects.get(=participant.team.state+1)
        #     return JsonResponse({"question_id": req_question.unique_id, "question_text": req_question.question, "status": 1})
        # except Exception:
        #     return JsonResponse({"message": "No such question exists.", "status": 0})
    else:
        return JsonResponse({"message": "A <POST> request to get the question", "status": 0})


@csrf_exempt
def check_question_answer(request):
    if request.method == 'POST':
        # try:
        #     authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        # except KeyError:
        #     return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        # if authorization != senv.AUTHORIZATION:
        #     return JsonResponse({"message": "Invalid Request Source", "status": 0})
        try:
            data = json.loads(request.body.decode("utf-8").replace("'", '"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})
        try:
            # question_id = data['question_id']
            # participant_id = data['participant_id']
            ans_saved = data['ans']  # there is no answer in the database yet.
        except KeyError as missing_data:
            return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

        try:
            with transaction.atomic():
                participant = Participant.objects.get(user=request.user)
                question_id = participant.team.state
                question = Question.objects.get(myid=question_id)
                answer = Answer.objects.get(question=question)
                print('hehehe')

                team = participant.team
            if question_id == 6 or question_id == 7 or question_id == 8:
                if answer.times_answered < 2*(10-question_id)-1:
                    if ans_saved == answer.answer:
                        team.state += 1
                        team.save()
                        answer.times_answered += 1
                        answer.save()
                        return JsonResponse({"message": "Team answered the question correctly.", "status": 1})
                    else:
                        return JsonResponse({"message": "Answer is incorrect", "status": 0})
                else:
                    return JsonResponse({"message": "Answer Limit Reached.", "status": 0})
            if ans_saved == answer.answer:
                team.state += 1
                team.save()
                answer.times_answered += 1
                answer.save()
                return JsonResponse({"message": "Team answered the question correctly.", "status": 1})
            else:
                return JsonResponse({"message": "Answer is incorrect", "status": 0})
        except Exception as e:
            print(str(e))
            print("njkhsfjhklsdff")
            return JsonResponse({"message": "Check if the question has been answered", "status": 0})


@csrf_exempt
def team_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            part = Participant.objects.get(user=request.user)
            mylist = Participant.objects.filter(team=part.team)
            namelist = []
            count = 0
            for item in mylist:
                count += 1
                namelist.append(item.user.username)
            return JsonResponse({"message": "Team List", "teamlist": namelist, "teamname": part.team.name, "length": count, "status": 1})
        else:
            return JsonResponse({'message': 'Something Failed',  'status': 0})

# @csrf_exempt
# def team_register(request):
#     if request.method == 'POST':
#         try:
#             authorization = str(request.META['HTTP_X_AUTHORIZATION'])
#         except KeyError:
#             return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

#         if authorization != senv.AUTHORIZATION:
#             return JsonResponse({"message": "Invalid Request Source", "status": 0})

#         try:                # just to decode JSON properly
#             data = json.loads(request.body.decode('utf8').replace("'", '"'))
#         except Exception:
#             return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

#         try:
#             team_name = data['team_name']
#             participants = data['participant_list']
#             part_id = data['participant_id']
#         except KeyError as missing_data:
#             return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

#         try:
#             participant1 = Participant.objects.get(unique_id=part_id)
#         except Participant.DoesNotExist:
#             return JsonResponse({"message": "Please login first.", "status": 0})

#         if participant1.team:
#             return JsonResponse({"message": "Your Team is already Registered.", "status": 0})

#         try:
#             with transaction.atomic():
#                 team = Team.objects.create(name=team_name, state=0)
#                 for participant in participants:
#                     participant = Participant.objects.get(email=participant["email"])
#                     if participant.team is not None:
#                         raise Exception
#                     participant.team = team
#                     participant.save()
#             return JsonResponse({"message": "Team registered successfully", "status": 1, "team_name": team.name})
#         except Exception:
#             return JsonResponse({"message": "Participant team already exists.", "status": 0})
