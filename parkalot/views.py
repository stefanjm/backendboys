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
    return render(request, 'parkalot/manage.html')

# /parkalot/customer view, if POST then start parking
# also wont redirect to another page. Will just show start a timer on the same page
# Context is used to push variables to template
def customer(request, customer_id):
    # Get the customer parkings
    customer_parkings = Parking.objects.filter(customer__id=customer_id)
    # variables to send to template
    context = {}
    if request.method == "POST":
        form = startParkForm(request.POST)
        # check if form is valid
        if form.is_valid():
            #TODO add customer and it's coordinates to DB, then ask for address from google maps API
            # Check if customer  is stopping or starting parking
            any_ongoing_parkings = customer_parkings.exclude(endDate__isnull=False)
            if(any_ongoing_parkings):
                # Found row with endDate not specified, means customer is already parking
                # so we stop parking
                ongoing_parking = any_ongoing_parkings
                ongoing_parking.endDate = datetime.now()
                ongoing_parking.save()
            # If no parkings without endDate specified are found, means customer wants to start parking, so we do that
            else:
                # startDate automatically uses datetime.now() so we don't need to specify it 
                newParking = Parking(customer = Customer.objects.get(pk=customer_id))
                newParking.save()
    # if not post
    else: 
        # Check for ongoing customer parking
        if(customer_parkings.filter(endDate__isnull=True)):
            context.update({"already_parking": customer_parkings.filter(endDate__isnull=True).first().startDate})
        form = startParkForm()
    context.update({"form": form})
    context.update({"customer_id": customer_id})
    return render(request, "parkalot/customer.html", context)

# /parkalot/parked view, to show when customer started parking
def parked(request):
    return render(request, "parkalot/parked.html")


# /parkalot/manager manager view
# Display all ongoing and finished parkings
def manager(request):
    try:
        # the intellisense version for python is messing up here.....
        # Get ongoing parkings
        ongoing_parkings = Parking.objects.filter(endDate__isnull=True)

        # Get finished parkings
        finished_parkings = Parking.objects.filter(endDate__isnull=False)
        context = {
            "ongoing_parkings": ongoing_parkings,
            "finished_parkings": finished_parkings,
        }
    except Exception as e:
        raise Http404("Summin went wong: " + e)
    return render(request, "parkalot/manager.html", context)