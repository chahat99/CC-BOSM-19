from google.oauth2 import id_token
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import *
import SportsCrypt.keyconfig as senv

import json

# team edit view

@csrf_exempt
def login(request):

    if request.method == 'POST':

        try:
            authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        except KeyError:
            return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        if authorization != senv.AUTHORIZATION:
            return JsonResponse({"message": "Invalid Request Source", "status": 0})

        try:                # just to decode JSON properly
            data = json.loads(request.body.decode('utf8').replace("'", '"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

        try:
            token = data['token']
        except KeyError as missing_data:
            return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), "status": 0})

        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), senv.CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            email = idinfo['email']

            try:
                participant = Participant.objects.get(email=email)
            except User.DoesNotExist:
                participant = Participant.objects.create(email=email)
            #     user = User.objects.create(username=username)
            # except Exception as e:
            #     print(str(e))
            #     return JsonResponse({"message": "User creation Failed!", "status": 0})
            
            # try:
            #     participant = Participant.objects.get(user=user)
            # except Participant.DoesNotExist:
            #     participant = Participant.objects.create(user=user, email=email)

        except ValueError:
            # Invalid token
            return JsonResponse({"message": "Invalid ID Token passed!", "status": 0})

@csrf_exempt
def team_register(request):
    if request.method == 'POST':
        try:
            authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        except KeyError:
            return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        if authorization != senv.AUTHORIZATION:
            return JsonResponse({"message": "Invalid Request Source", "status": 0})

        try:                # just to decode JSON properly
            data = json.loads(request.body.decode('utf8').replace("'", '"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

        team_name = data['team_name']
        participants = data['participant_list']

        for participant in participants:
            try:
                user = User.objects.get(username=username)
                return JsonResponse({"message": "User already exists", "status": 0})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username)
