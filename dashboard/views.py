from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from . models import CarEvaluation
from . forms import CarEvaluationForm
from django.contrib.auth.models import User
import joblib
import pandas as pd
import os

CURRENT_DIR = os.path.dirname(__file__)
model_file = os.path.join(CURRENT_DIR, 'model/rf_classifier.pkl')
svm = joblib.load(model_file)


# Create your views here.
BUYING = {
    3 : 'v-high',
    2 : 'high',
    1 : 'med',
    0 :'low'
    }

MAINT = {
    3 : 'v-high',
    2 : 'high',
    1 : 'med',
    0 :'low'
}

DOORS = {
    3 :'5-more',
    2 :'4',
    1 : '3',
    0 :'2'
}

PERSON = {
    2 : 'more',
    1 : '4',
    0 : '2'
    }

LUG_BOOT ={
    2 : 'big',
    1 : 'med',
    0 : 'small'
}


SAFETY = {
    2 : 'high',
    1 : 'med',
    0 : 'low'
}


def site(request):
    
    form = CarEvaluationForm()
    if request.method == "POST":
        form = CarEvaluationForm(request.POST)
        if form.is_valid():
       
            buying = int(form.cleaned_data.get('buying'))
            maint = int(form.cleaned_data.get('maint'))
            doors = int(form.cleaned_data.get('doors'))
            persons = int(form.cleaned_data.get('persons'))
            lug_boot = int(form.cleaned_data.get('lug_boot'))
            safety = int(form.cleaned_data.get('safety'))
        
        
            data = pd.DataFrame({
                'buying':[buying],
                "maint":[maint],
                "doors":[doors],
                "persons":[persons],
                "lug_boot":[lug_boot],
                "safety":[safety]
            })

        
            checker = svm.predict(data)[0]
            if (checker == 0):
                checker = 'Unacceptable'
                messages.warning(request, checker)
            elif (checker == 1):
                checker = 'Acceptable'
                messages.success(request, checker)

            elif (checker == 2):
                checker = 'Good'
                messages.warning(request, checker)

            else:
                checker = 'Very Good'
                messages.warning(request, checker)
            # if form.is_valid():
            if not request.user.is_authenticated:
                return redirect('login')
            obj = form.save(commit=False)
            convert_form_values(obj,buying,maint,doors,persons,lug_boot,safety)
            obj.predictions = checker
            obj.save()
    else:
        form = CarEvaluationForm()

    context = {"form":form}

    return render(request, "dashboard/index.html", context)

@login_required
def predictions(request):
    car_info = CarEvaluation.objects.all()
    context = {
        'car_info': car_info
    }
    return render(request, 'dashboard/predictions.html', context)



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'dashboard/register.html', {'form': form})


def convert_form_values(form, buying, maint, doors, person, lug_boot, safety):
    form.buying = BUYING[buying]
    form.maint = MAINT[maint]
    form.doors = DOORS[doors]
    form.persons = PERSON[person]
    form.lug_boot = LUG_BOOT[lug_boot]
    form.safety = SAFETY[safety]
