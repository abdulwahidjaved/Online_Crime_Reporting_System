from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Admin_Details,User_Details,Missing_Complaint,Complaints
import datetime
from datetime import datetime
import numpy as np
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home.html', {})

def ChangePassword(request):
    if request.method == 'POST':
        CurrentPassword = request.POST['CurrentPassword']
        NewPassword = request.POST['NewPassword']
        ConfirmPassword = request.POST['ConfirmPassword']

        uid = request.session['User_id']
        CurrUser = User_Details.objects.all().filter(id=uid)
        if CurrUser[0].Password == CurrentPassword:
            if NewPassword == ConfirmPassword:
                User_Details.objects.filter(id=uid).update(Password=NewPassword)
                messages.info(request,'Passwords Changed Successfully')
                return render(request, 'ChangePassword.html', {})
            else:
                messages.info(request,'New Passwords doesnt match')
                return render(request, 'ChangePassword.html', {})
        else:
            messages.info(request,'Current Password doesnt match')
            return render(request, 'ChangePassword.html', {})
        
    else:
        return render(request, 'ChangePassword.html', {})


def logout(request):
    Session.objects.all().delete()
    messages.info(request,'Account logout')
    return redirect('/')


def Admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['Pass']
        
        if Admin_Details.objects.filter(Username=Username, Password=password).exists():
                user = Admin_Details.objects.get(Username=Username, Password=password)
                request.session['type_id'] = 'Admin'
                request.session['username'] = Username
                request.session['login'] = 'Yes'
                return redirect('/ViewComplaints/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Admin_login/')
    else:
        return render(request, 'Admin_login.html', {})


def User_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if User_Details.objects.filter(Username=Username, Password=password).exists():
            user = User_Details.objects.get(Username=Username, Password=password)
            request.session['User_id'] = str(user.id)
            request.session['Gender'] = str(user.Gender)
            request.session['type_id'] = 'User'
            request.session['username'] = Username
            request.session['login'] = 'Yes'
            return redirect('/Complain/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/User_login/')
    else:
        return render(request, 'User_login.html', {})


def Register(request):
    if request.method == 'POST':           
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Dob = request.POST['Dob']
        Gender = request.POST['Gender']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Password = request.POST['Password']
        final_address = request.POST['Address']
        City = request.POST['City']
        State = request.POST['State']
        register = User_Details( First_name=First_name, Last_name=Last_name, Dob=Dob, Gender=Gender ,Phone= Phone,Email= Email,Username= Username,Password=Password,Address=final_address,City=City,State=State)
        register.save()
        messages.info(request,'User Register Successfully')
        return redirect('/User_login/')
    else:
        return render(request, 'Register.html', {})


def ViewUser(request):
    if request.method == 'POST':
        pass
    else:
        Users = User_Details.objects.all()
        return render(request, 'ViewUser.html', {'Users':Users})



def Complain(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        contact = request.POST['contact']
        emailid = request.POST['emailid']
        doorno = request.POST['doorno']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        Country = request.POST['Country']
        Pincode = request.POST['Pincode']
        ComplaintType = request.POST['ComplaintType']
        Complaint = request.POST['Complaint']
        uid = request.session['User_id']
        CurrDate  = datetime.now().date()


        Comp = Complaints(FullName=Name,Contact=contact,Userid=uid,Email=emailid,Address=doorno+address,City=city,State=state,Country=Country,Pincode=Pincode,Complaint=Complaint,ComplaintType=ComplaintType,Status='Raised',DateofComplaint=CurrDate)
        Comp.save()
        messages.info(request,'Complaint Register Successfully')
        return redirect('/Complain/')
    else:
        return render(request, 'Complaints.html', {})



def ComplaintStatus(request):
    if request.method == 'POST':
        pass
    else:
        uid = request.session['User_id'] 
        MissingComplaint = Missing_Complaint.objects.all().filter(Uid=uid) 
        Complaint = Complaints.objects.all().filter(Userid=uid) 
        return render(request, 'ComplaintStatus.html', {'MissingComplaint':MissingComplaint,'Complaint':Complaint})



def MissingPersons(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        contact = request.POST['contact']
        emailid = request.POST['emailid']
        doorno = request.POST['doorno']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        Country = request.POST['country']
        Pincode = request.POST['Pincode']
        Image1 = request.FILES['Image_upload1']
        Complaint = request.POST['Complaint']
        uid = request.session['User_id']
        CurrDate = datetime.now().date()
        

        MissingComp = Missing_Complaint(FullName=Name,Contact=contact,Uid=uid,Email=emailid,Address=doorno+address,City=city,State=state,Country=Country,Pincode=Pincode,MissingDetails=Complaint,Photo=Image1,Status='Raised',DateofComplaint=CurrDate)
        MissingComp.save()
        messages.info(request,'Missing Complaint Register Successfully')
        return redirect('/MissingPersons/')
    else:
        return render(request, 'MissingPersons.html', {})



def ViewComplaints(request):
    if request.method == 'POST':
        pass
    else:
        MissingComplaint = Missing_Complaint.objects.all() 
        Complaint = Complaints.objects.all() 
        return render(request, 'ViewComplaints.html', {'MissingComplaint':MissingComplaint,'Complaint':Complaint})



def CheckReport(request):
    if request.method == 'POST':
        pass
    else:

        TotalCount = Complaints.objects.all().count()
        TheftCount = Complaints.objects.all().filter(ComplaintType= 'Theft').count()
        ForgeryCount = Complaints.objects.all().filter(ComplaintType= 'Forgery').count()
        MurderCount = Complaints.objects.all().filter(ComplaintType= 'Murder').count()
        CyberCrimeCount = Complaints.objects.all().filter(ComplaintType= 'Cyber Crime').count()

        Headline = Missing_Complaint.objects.all().order_by('-DateofComplaint')[:4]
        return render(request, 'CheckReport.html', {'TotalCount':TotalCount,'TheftCount':TheftCount,'ForgeryCount':ForgeryCount,'MurderCount':MurderCount,'CyberCrimeCount':CyberCrimeCount,'Headline':Headline})



def UpdateComplaint(request):
    if request.method == 'POST':
        Cid = request.POST['UpdateCid']
        ComplainStatus = request.POST['UpdateComplainStatus']

        Complaints.objects.filter(id=Cid).update(Status=ComplainStatus)
        messages.info(request,'Complaint Status Updated Successfully')
        return redirect('/ViewComplaints/')
    else:
        return redirect('/ViewComplaints/')


def UpdateMissingComplaint(request):
    if request.method == 'POST':
        Mid = request.POST['UpdateMid']
        ComplainStatus = request.POST['UpdateMissingComplainStatus']

        Missing_Complaint.objects.filter(id=Mid).update(Status=ComplainStatus)
        messages.info(request,'Missing Complaint Status Updated Successfully')
        return redirect('/ViewComplaints/')
    else:
        return redirect('/ViewComplaints/')

