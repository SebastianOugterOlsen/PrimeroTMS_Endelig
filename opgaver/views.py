from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Opgaver, Kunder
from .forms import OpgaverForm, KunderForm


def home_view(request, *args, **kwargs):
    return render(request, "home.html")



def opgaver_detail_view(request):
    queryset = Opgaver.objects.exclude(status='5')  # Liste med alle opgave objecter der er aktive
    context = {"object_list": queryset}
    return render(request, "opgaver/opgaver_detail.html", context)

def opgaver_opret_view(request):
    obj = Opgaver.objects.get(id=1)
    form = OpgaverForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OpgaverForm()
        return redirect('/opgaver')

    context = {'form': form}
    return render(request, "opgaver/opgaver_opret.html", context)


def opgaver_slet_view(request, id):
    obj = get_object_or_404(Opgaver, id=1)
    # POST request
    if request.method == "POST":
        # Godkend sletning
        obj.delete()
        return redirect('/opgaver')
    context = {"object": obj}

    return render(request, "opgaver/opgaver_slet.html", context)


def opgaver_rediger_view(request, pk):
    obj = get_object_or_404(Opgaver, id=pk)

    form = OpgaverForm(instance=obj)

    if request.method == 'POST':
        form = OpgaverForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/opgaver')

    context = {'form': form}

    return render(request,'opgaver/opgaver_rediger.html', context)



def kunder_opret_view(request):
    obj = Kunder.objects.get(id=1)
    form = KunderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = KunderForm()
        return redirect('/kunder')

    context = {'form': form}
    return render(request, "kunder/kunder_opret.html", context)


def kunder_detail_view(request):
    queryset = Kunder.objects.all()  # Liste med alle opgave objecter
    context = {"object_list": queryset}
    return render(request, "kunder/kunder_detail.html", context)


def kunder_slet_view(request, pk):
    item = get_object_or_404(Opgaver, id=pk)
    # POST request
    if request.method == "POST":
        # Godkend sletning
        item.delete()
        return redirect('/kunder')
    context = {"item": item}

    return render(request, "kunder/kunder_slet.html", context)


def kunder_rediger_view(request, pk):
    obj = get_object_or_404(Opgaver, id=pk)

    form = KunderForm(instance=obj)

    if request.method == 'POST':
        form = KunderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/kunder')

    context = {'form': form}

    return render(request,'kunder/kunder_rediger.html', context)

def opgaver_inaktive_view(request):
    queryset = Opgaver.objects.filter(status='5')  # Liste med alle opgave objecter der er inaktive
    context = {"object_list": queryset}
    return render(request, "opgaver/opgaver_inaktive.html", context)


#def opgaver_inaktive_view(request, ansvarlig):
 #   obj = get_object_or_404(Opgaver, id=ansvarlig)
  #  queryset = Opgaver.objects.filter(kunde_navn='id')  # Liste med alle opgave objecter der er inaktive
   # context = {"object_list": queryset}
    #return render(request, "opgaver/opgaver_inaktive.html", context)

