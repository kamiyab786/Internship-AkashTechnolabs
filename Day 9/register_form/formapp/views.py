from django.shortcuts import render

# Create your views here.
def form(request):
    if request.method == 'POST':
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        contact= request.POST.get("contact")
        country = request.POST.get("country")
        address= request.POST.get("address")

        context={
            'fn':fn,
            'ln':ln,
            'email':email,
            'gender':gender,
            'contact':contact,
            'country':country,
            'address' :address,
        }
        return render(request,'data.html',context)
    return render(request, 'form.html')