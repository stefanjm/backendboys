from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404

# our specific stuff
from .models import Parking, Customer
from .forms import startParkForm

# Import Datetime
from datetime import datetime

# Create your views here.

# /parkalot landing page
def index(request):
    # Render the template
    return render(request, 'parkalot/index.html')

# /parkalot/customer view, if POST then start parking
def customer(request, customer_id):
    if request.method == "POST":
        form = startParkForm(request.POST)
        # check if form is valid
        if form.is_valid():
            # add customer and it's coordinates to DB, then ask for address from google maps API
            #TODO
            # when done, redirect
            return HttpResponseRedirect("/parkalot/parked")
        else:
            error_message = "faileeeed model validation: " + str(customer_id)
    # if not post
    else:
        error_message = "not POST"
        form = startParkForm()

    return render(request, "parkalot/customer.html", {"form": form, "customer_id": customer_id, "error_message": error_message})

# /parkalot/parked view, to show when customer started parking
def parked(request):
    return render(request, "parkalot/parked.html")


# /parkalot/manager manager view
# Display all ongoing parkings
def manager(request):
    try:
        # the intellisense version for python is messing up here.....
        ongoing_parkings = Parking.objects.filter(endDate__isnull=True)
        context = {
            "ongoing_parkings": ongoing_parkings,
        }
    except Exception as e:
        raise Http404("Summin went wong: " + e)
    return render(request, "parkalot/manager.html", context)