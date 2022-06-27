from datetime import datetime
import re
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from ayush.models import user_signup,login_log,rooms,password_history
from ayush.serializer import signupSerializer,logSerializer,roomSerializer,delSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from django.core.mail import send_mail as sm
from ayush.serializer import passSerializer


@csrf_exempt
@api_view(['POST','PUT'])
def signup(request):
    if request.method=='POST' or request.method=='PUT':
        python_data=request.data
        if not python_data['username'] or not python_data['firstname'] or not python_data['lastname'] or not python_data['phonenumber'] or not python_data['email'] or not python_data['password'] or not python_data['type'] :
            return Response({'msg':'invalid field'},status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            email=python_data['email']
            existing_email=user_signup.objects.filter(Q(email=email)|Q(username=python_data['username']))
            print(existing_email)
            if existing_email.exists():
                return Response({'msg':'email or username already exist!!!'},status=status.HTTP_226_IM_USED)
        except :
            return Response({'msg':'something went wrong!!'},status=status.HTTP_403_FORBIDDEN)
        if re.match('.+[@].+\.co',python_data['email']) and re.match('[A-Z].+',python_data['firstname']) and re.match('[A-Z].+',python_data['lastname']) and re.match('[0-9]{10}',python_data['phonenumber']) and re.match('[A-Za-z0-9]{8}',python_data['password']):
            python_data['password']=str(make_password(python_data['password'],salt=None,hasher='default'))
            print(python_data['password'])
            serial=signupSerializer(data=python_data)
            if serial.is_valid():
                serial.save()
                return Response({'msg':'successfully added!!'},status=status.HTTP_201_CREATED)
            return Response({'msg':serial.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({'msg':'invalid pattern'},status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response({'msg':'Invalid method'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST','PUT'])
def login_fun(request):
    if request.method == 'POST' or request.method=='PUT':
        email=request.data['email']
        password=request.data['password']
        check_login=user_signup.objects.get(email=email)
        if check_login:
            if check_password(password,check_login.password):
                user=check_login.username
                sin=user_signup.objects.get(username=user)
                try:
                    log=login_log.objects.get(username=sin.id)
                    print(log)
                    coun=log.login_count
                    coun+=1
                    sin.status_user=True
                    sin.save()
                    login_log.objects.filter(username=sin.id).update(username=sin,login_count=coun)
                    return Response({'msg':'welcome user!!'},status=status.HTTP_200_OK)
                except:
                    sin.status_user=True
                    sin.save()
                    login_log.objects.update_or_create(username=sin)
                    return Response({'msg':'congrats on your first login!!'},status=status.HTTP_200_OK)         
            return Response({'msg':'invalid password'},status=status.HTTP_404_NOT_FOUND)
        return Response({'msg':'invalid email'},status=status.HTTP_404_NOT_FOUND)
    return Response({'msg':'invalid method'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_room(request,pk=None):
    if request.method=='GET':
        id=pk
        if id is None:
            room_list=rooms.objects.all()  
            if room_list:
                rooms_li=roomSerializer(room_list,many=True) 
                print(rooms_li) 
                return Response({'msg':rooms_li.data},status=status.HTTP_200_OK)
            return Response({'msg':'no rooms has been added yet'},status=status.HTTP_204_NO_CONTENT) 
        else:
            try:
                room_contact=rooms.objects.get(id=pk)
                print(room_contact.username_id)
                owner=user_signup.objects.get(id=room_contact.username_id)
                serial=signupSerializer(owner)
                print(serial.data)
                # Response.set_cookie('previousitem',id)
                # print(request.COOKIES['previousitem'])
                return Response({'Owner Contact':serial.data},status=status.HTTP_200_OK)
            except:
                # HttpResponse.set_cookie('previousitem',id)
                # print(request.COOKIES['previousitem'])
                return Response({'msg':'couldn\'t able to load data !!'},status=status.HTTP_404_NOT_FOUND)
        
              
            
@api_view(['POST','PUT','GET'])
def set_room(request):
    if request.method=='POST' or request.method=='PUT':
        data=request.data
        user=data['username']
        try:
            sin=user_signup.objects.get(username=user) 
        except:
            return Response({'msg':'couldn\'t get the data!!'})  
        if sin.status_user:
            data['username']=sin.id
            print(data)
            serial=roomSerializer(data=data)     
            if serial.is_valid():
                serial.save()
                return Response({'msg':'hello your room has been added'},status=status.HTTP_200_OK)
            return Response({'msg':serial.errors},status=status.HTTP_403_FORBIDDEN)
        return Response({'msg':'you need to login first'},status=status.HTTP_204_NO_CONTENT)
    if request.method=='GET':
        room_list=rooms.objects.all()  
        if room_list:
            rooms_li=roomSerializer(room_list,many=True) 
            print(rooms_li) 
            return Response({'msg':rooms_li.data},status=status.HTTP_200_OK)
        return Response({'msg':'no rooms has been added yet'},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST','PUT'])
def forget_password(request):
    if request.method=='POST':
        email=request.data['email']
        try:
            user=user_signup.objects.get(email=email)
        except:
            return Response({'msg':'couldn\'t fetched!!'})
        print(user.password)
        res = sm(
        subject = 'Password recovery',
        message = f'Hello {user.username} your encrpted password is {user.password} use it in your reset password and set new password',
        from_email = 'cm.b.49ayush.shukla@gmail.com',
        recipient_list = [email],
        fail_silently=False,
        )
        return Response({'msg':'email sent!!'},status=status.HTTP_200_OK)    
    if request.method=='GET':
        return Response({'msg':'please provide your email to get password'})
    
@api_view(['GET','POST','PUT'])
def reset_password(request):
    if request.method=='GET':
        return Response({'msg':'enter your mailed password as password and set new password and username'})
    
    if request.method=='POST' or request.method=='PUT':
        password=request.data['password']
        new_pass=request.data['new_password']
        user=request.data['username']
        yo=user_signup.objects.get(username=user)
        if password==yo.password:
            new_pass=make_password(new_pass,salt=None,hasher='default')
            yo.password=new_pass
            yo.save()
            try:
                pass1=password_history.objects.get(username=user)
                coun=pass1.no_changed
                coun+=1
                pass1.no_changed=coun
                pass1.save()
                return Response({'msg':'password history saved'},status=status.HTTP_200_OK)
            except:
                password_history.objects.create(username=yo)
            return Response({'msg':'yo password has been set!!!'})
        return Response({'msg':'password didnt changed something went wrong!!'},status=status.HTTP_200_OK)
    
@api_view(['POST','PUT','GET'])
def password_hist(request):
    if request.method=='GET':
        return Response({'msg':'provide your username to fetch your password history'})
    
    if request.method=='POST' or request.method=='PUT':
        user=request.data['username']
        try:
            detail=user_signup.objects.get(username=user)
            pass1=password_history.objects.get(username_id=detail.id)
            python_data=passSerializer(pass1)
            print(python_data)
            print('aysuh')
            return Response(python_data.data,status=status.HTTP_200_OK)
        except :
            return Response({'msg':'you havent changed your password yet!!'},status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET','POST','PUT'])
def logout(request):
    if request.method=='POST' or request.method=='PUT':
        user=request.data['username']
        try: 
            id=user_signup.objects.get(username=user)
            if id.status_user:            
                login_log.objects.filter(username=id.id).update(last_logout=datetime.now())
                id.status_user=False
                id.save()
                return Response({'msg':'you have been successfully logged out!!'},status=status.HTTP_200_OK)
            return Response({'msg':'you need to login first'},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'msg':'something went wrong'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
    if request.method=='GET':
        return Response({'msg':'provide your username to logout!!!'},status=status.HTTP_200_OK)

@api_view(['GET','POST','PUT'])
def delete_account(request):
    if request.method=='GET':
        return Response({'msg':'please give your username and password to delete your account'},status=status.HTTP_200_OK)
    
    if request.method=='POST' or request.method=='PUT':
        user=request.data['username']
        password=request.data['password']
        check_login=user_signup.objects.get(username=user)
        if check_login:
            if check_password(password,check_login.password):
                user_detail=signupSerializer(check_login)
                print(user_detail.data)
                serial=delSerializer(data=user_detail.data)
                if serial.is_valid():
                    serial.save()
                    check_login.delete()
                    return Response({'msg':'your account has been successfully deleted'},status=status.HTTP_200_OK)
                return Response({'msg':serial.errors},status=status.HTTP_403_FORBIDDEN)
            return Response({'msg':'password invalid!!'},status=status.HTTP_403_FORBIDDEN)
        return Response({'msg':'username invalid!!'},status=status.HTTP_403_FORBIDDEN)
    
    
        
    
    
        



