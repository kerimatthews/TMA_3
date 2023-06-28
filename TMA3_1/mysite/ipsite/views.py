from django.shortcuts import render



def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def show_ip_address(request):
    user_ip = get_ip_address(request)

  # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
       'user_ip':user_ip,
       'num_visits': num_visits,
    }
    return render(request, "output.html", context=context )
