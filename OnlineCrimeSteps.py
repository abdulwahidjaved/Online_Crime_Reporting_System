#steps 

#Command to create virtual Env:
python -m venv env

#Command to activate virtual env
env\Scripts\activate

#till here we have completed. ----->







#you can find setting.py file inside OnlineCrimeReportingSystem/OnlineCrimeReportingSystem.
#===================================
#you have to comment this code (you can just add # in the starting line as i have added)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'CrimeReport_db',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
#===================================

#===================================

#and add this code 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,"db.sqlite3"),
    }
}
#===================================

#Once the virtual environment is activated 
#it will show (env) in start of the command line

#cd to OnlineCrimeReportingSystem folder there would be manage.py file.
#create a file requirements.txt and add these down line

asgiref==3.8.1
build==1.2.2.post1
colorama==0.4.6
Django==5.1.2
numpy==2.1.2
packaging==24.1
pandas==2.2.3
pillow==10.4.0
pyproject_hooks==1.2.0
python-dateutil==2.9.0.post0
pytz==2024.2
six==1.16.0
sqlparse==0.5.1
tomli==2.0.2
typing_extensions==4.12.2
tzdata==2024.2



#there you can run the command 
pip install -r requirements.txt



#once all the required libraries are installed you can run command python manage.py check

# it will show you 4 warning you can ignore that as it wont make any issue,after this run
python manage.py makemigrations
#after this 
python manage.py migrate
#this will reflect all the db level changes after this run the following command one by one

python manage.py shell

from AppCrime.models import *
 Admin_Details.objects.create(Username='Admin',Password='Success@123')
 #if you get response like this -> <Admin_Details: Admin_Details object (1)> you can exit the shell using command exit()

#then you can run 
python manage.py runserver
#this command will run the server

#you can copy this url to browser and its working:-   http://127.0.0.1:8000/