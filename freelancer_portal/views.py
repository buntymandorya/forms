from django.shortcuts import render
# from registration.models import demo,Enquiry
# from .form import ContactForm
from registration.models import demo,COUNTRY_CHOICES,LANGUAGE_CHOICES,EXPERTISE_CHOICES
def index(request):
    context = {
                'country_choices': COUNTRY_CHOICES,
                'language_choices': LANGUAGE_CHOICES,
                'expertise_choices': EXPERTISE_CHOICES,
                'success': False

            }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        states = request.POST['states']
        date = request.POST['dob']
        # state=request.POST['state']
        country = request.POST["country"] 
        city=request.POST["city"]
        educational=request.POST["educational"]
        otherLanguage=request.POST["otherLanguage"]
        mobile=request.POST["mobile"]
        hours=request.POST["hours"]
        tools=request.POST["tools"]
        project=request.POST["project"]
        equipment=request.POST["equipment"]
        skills=request.POST["skills"]
        link=request.POST["link"]
        referred=request.POST["referred"]
        gender = request.POST['gender']
        languages_list = request.POST.getlist('languages')
        languages_str = ','.join(languages_list)
        expertise_list = request.POST.getlist('expertise')
        expertise_str = ','.join(expertise_list)
        
        # country=request.POST["country"]

        demo(name=name,email=email,states=states,city=city,educational=educational,otherLanguage=otherLanguage,mobile=mobile,hours=hours,tools=tools,project=project,equipment=equipment,skills=skills,link=link,referred=referred,country=country,date=date, gender=gender,languages=languages_str,expertise=expertise_str,).save()
        context['success'] = True  # Set success flag


        
    return render (request,'index.html',context)

