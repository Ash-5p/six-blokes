from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import Booking
from .forms import BookingForm


# Create your views here.
def booking_view(request):
    """
    Renders the booking form and allows authenticated user to
    created a booking
    Display an individual instance of :model:`booking.Booking`.

    **Context**

    ``booking``
        An instance of :model:`booking.Booking`.
    ``booking_form``
        An instance of :form:`booking.BookingForm`.
    **Template:**

    :template:`booking/booking.html`
    """
    booking_form = BookingForm()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking_form.save()
            messages.success(
                request, "Booking Successful! We look forward to seeing you!"
                )
            return redirect(booking_list_view)
        else:
            messages.error(request, "Booking failed, Please try again")

    return render(
        request,
        "booking/booking.html",
        {
            "booking": Booking,
            "booking_form": booking_form
        },
    )


@login_required
def booking_list_view(request):
    """
    Renders all of the authenticated users bookings in a list
    past bookings aren't shown
    Display an individual instance of :model:`booking.Booking`.

    **Context**

    ``user_bookings``
        All furture bookings created by the authenticated user.
    ``booking_form``
        An instance of :form:`booking.BookingForm`.
    **Template:**

    :template:`booking/booking_list.html`
    """
    user_bookings = Booking.objects.filter(
        user=request.user
        ).order_by(
            "date"
            ).filter(
                user=request.user, date__gte=now().date()
                )

    context = {
        'user_bookings': user_bookings,
        'booking_form': BookingForm()
    }

    return render(
        request,
        "booking/booking_list.html",
        context

    )


@login_required
def booking_edit(request, booking_id):
    """
    Edit an individual booking.

    **Context**

    ``booking``
        A single booking.
    """

    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, "Booking successfully updated!")
        else:
            messages.error(request, "Error updating booking!")
        return HttpResponseRedirect(reverse("booking_list"))

    # If GET request, return JSON response with booking data
    # (Suggested by ChatGPT)
    return JsonResponse({
        "date": booking.date.strftime("%Y-%m-%d"),
        "time_slot": booking.time_slot,
        "guests": booking.guests,
        "allergies": list(booking.allergies.values_list("id", flat=True)),
        "booking_notes": booking.booking_notes
    })


@login_required
def booking_delete(request, booking_id):
    """
    Delete an individual booking.

    **Context**

    ``booking``
        A single booking.
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    booking.delete()
    messages.add_message(request, messages.SUCCESS, 'Booking deleted!')

    return HttpResponseRedirect(reverse('booking_list'))
