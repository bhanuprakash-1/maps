from django.http import HttpResponse
from django.shortcuts import render
from .models import person,areas_affected,address_search

def base(request):
    return render(request,'disater/base.html')

def person_status(request):
    return render(request , 'disater/person_status.html')

def details(request,person_id):
    return HttpResponse("<h1>this has an id " + str(person_id) + "</h1>")

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q= request.GET['q']
        all_persons= person.objects.filter(first_name__icontains=q)
        return render(request,'disater/results.html',{'all_persons':all_persons,'query':q})
    else:
        return HttpResponse('please submit a search term.')

def affected_areas(request):
    return render(request , 'disater/affected_areas.html')

def Search_affected_areas(request):
    if 'q_city' and 'q_street_number' and 'q_pincode'  in request.GET and request.GET['q_city' and 'q_street_number' and 'q_pincode' ]:
        q_city = request.GET['q_city']
        q_street_number = request.GET['q_street_number']
        q_pincode = request.GET['q_pincode']
        q_address = request.GET['q_address']
        q=areas_affected(city=q_city,street_number=q_street_number,pincode=q_pincode)
        all_areas= areas_affected.objects.all()
        a=0
        add=address_search(address=q_address)
        add.save()
        asd=q
        asd.photo=12
        for area in all_areas:
            if (q_city) == (area.city) and int(q_pincode)== int(area.pincode) and int(q_street_number) == int(area.street_number) :
                a=1
                asd=areas_affected(city=q_city,street_number=q_street_number,pincode=q_pincode,photo=area.photo)

        return render(request,'disater/results_area_affected.html',{'a':a,'query':q,'asd':asd})
    else:
        return HttpResponse('please submit a search term.')


def post(request):
    if 'q_fname' and 'q_lname' and 'q_phno' and 'q_profile' in request.GET and request.GET['q_fname' and 'q_lname' and 'q_phno' and 'q_profile']:
        q_fname = request.GET['q_fname']
        q_lname = request.GET['q_lname']
        q_phno = request.GET['q_phno']
        q_profile = request.GET['q_profile']
        q=person(first_name=q_fname,last_name=q_lname,relative_number=q_phno,profile_picture=q_profile)
        all_person=person.objects.all()
        b=len(all_person)
        q.save()
        return render(request,'disater/base.html',{'b':b,'all_person':all_person})
    else:
        return HttpResponse('please submit a search term.')

