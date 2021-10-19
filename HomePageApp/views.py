from django.shortcuts import render
import logging,time


logging.basicConfig(level=logging.INFO,filename='execution_logs.logs',)

# Create your views here.
def show_homepage(request):
    v_greet_message=None
    v_userName='Yash'
    currentHour=int(time.strftime('%H'))
    if currentHour<12:
        v_greet_message= 'Good Morning'
    elif currentHour>12:
        v_greet_message= 'Good Afternoon'
    elif currentHour >16:
        v_greet_message= 'Good Evening'


    homepageData={'t_userName' :v_userName,'t_greetMessage':v_greet_message}
    logging.debug('Inside Homepage')
    return render(request, 'HomePageApp/index.html',context=homepageData)