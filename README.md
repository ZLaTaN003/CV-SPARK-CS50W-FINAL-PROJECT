# CS50 WEB PROGRAMMING FINAL PROJECT: CV SPARK


This Learning Journey with CS50W was so great !.As a guy who only knew some python i got to learn many things about Django and Javascript i would first like to Thank Whole CS50W Crew


When it came to my Final Project i was determined to make something that would be useful .. So i came to the idea of a CV generator app

## APP IDEA

My App takes in User Data and converts it into a CV format which Users can download and apply to Jobs 



## Libraries Used


xhtml2pdf i used this python library to convert html template to a pdf format

## Key Features

-Register/Login/Logout 

-Profile Section -I made use of Django Signals in my models.py where  i made a feature that connected to User Model .Whenever a User Creates a Account a Profile is generated  for the user prepopulated with details like username email and others which can be edited.I made use of Javascript to add a User experience by adding Toggling feature where i can toggle between Edit Profile and my Profile Details .

-Create Section  -This is the place where User can enter the details that they need to add in thier CV i made use of Javascript to add a custom client side validation to bootstrap form 

-Cvs Section This is the place where CV in pdf form will be generated  users have the option to view the CV which will show them content of the  details they submited  in a CV Format if they like the format they can Download the CV by clicking Download button.Users can also delete thier CV from the list. I made use of Javascript to add a Upvote system where users can upvote other users CVs similar to like feature.


-Team Section This is section where Users can browse through different fields Where they can join Teams like Web Developer,Cybersecurity etc . On joining Users will be able to see other people and thier CVs who are aleready in the Team helping Users to understand key skills needed in thier respective fields


-Jobs Sections  Here i made use of apis from both server side and from client side i used Adzuna api in my views and i added unsplash photos api to match the image with the job offered in my Javascript Code


## Distinctiveness and Complexity

In terms of Distinctivenes this project is entirely different from other projects i had made. i even tried adding Django Features like Signals making use of api calls  from other websites in both server side and client side. i kept in mind of all things i had learned through the entire course and applied most of the concepts i learned in this project. i also had to do some research on the xhtml2pdf python package 
  
This project contains about 5 models and made use of all 3 relations OnetoOne OnetoMany and ManytoMany  i have made use of relation between the models to acheive various features like for example the upvote system and i also have made use js code  for client side manipulation in most of my template so the project is quite Complex

## Files Content

Views.py

-Modelform for Profile Section

-create view -The view Responsible for adding User details used in Cv

-login,logout,register views
        
-profile view responsible for Profile section 

-jobfromlink view responsible for server side api request to adzuna jobs api where i fetch the latest job openings
        
-cv This is the view where i create a Html template which i will later use in xhtml2pdf

-cvtopdf This view converts the Template to Pdf Format


-list This view is used to show the list of CV submited by various users

-likecv This endpoint allows to implement the like feature  in which users can upvote other users cv (made use of JsonResponse)

-edit This view allows users to delete thier CV after they generated a pdf that they dont like

-sectionlist This is responsible for giving users a wide range of field teams which they can join

-join/leave section These views makes users able to join and leave sections

-sectionusers This section shows the list of users in each section


Models.py

-User Model

-Candidate model this is the model used for storing CV details of users

-Profile Model This model is responsible for Profile details of Users 

-Section Model This model is responsible for creating different Fields or Teams that user can join

-Like Model The model that helps users to like other users CV

-Signals Made Use of Django Signals to connect User and Profile Model

Registered Models with admin


urls.py 
     contains routes for my app

script.js
 -Edit Feature in Profiles is Implemented through  javascript code here where i use dom manipulation for better user experience
-Custom Client Side Validation is made for Create Section


styles.css
 Contain css files for project

profile.css
  Tried to play with some css styles for profile section

Templates

 -createresume -This template renders the form where users can submit thier CV details made use of bootstrap forms

 -cv - This is the template that shows or renders actuall Cv of the user its also passed as template in xhtml2pdf for generating pdf

 -jobsfromlink This is the template where i made use of most of the api stuff from backend i got adzuna job api and in frontend using js i got unspash images api that matched with the job postings (Contain Js code for client side api)

-layout This is my base template i have a navbar of my app overhere

-listing This the template where Users can see thier CV which they have submited they can either view or download thier CV or even others(Contains Js code for implementing upvote system)

-profile This template contains profile page of user where user can edit fields liek bio profilepicture Dob etc (Contains Js code for implementing a edit toggle feature)

-login/register - renders login/register form

-sectionlist This is the template where a list of all awailable sections are shown with users being able to join or leave them

-sectionusers This is the template where users can see the users already present in each section with option to download or see thier CV


Pictures This is the medial root of my project 
   -profile_pics This is place where profilephtot that user uploads in Profile section get displayed


## How to run the application
       Install project dependencies by running pip install -r requirements.txt
       Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
       python manage.py runserver to Run



video link
https://youtu.be/b8Ll5m0Nnao?si=pcCMrHPTklIqPwFL
