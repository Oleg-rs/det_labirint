from django.shortcuts import render
from .models import Setting, Katalog, Poryadok, Banner, Banner_2, PreimVa, Primer

def home(request):
    setting = Setting.objects.all()
    katalog = Katalog.objects.all()
    poradok = Poryadok.objects.all()
    banner = Banner.objects.all()
    banner_2 = Banner_2.objects.all()
    preimva = PreimVa.objects.all()
    primer = Primer.objects.all()
    return render(request, 'setting/home.html', {
        'setting':setting,
        'katalog':katalog,
        'poradok':poradok,
        'banner': banner,
        'banner_2': banner_2,
        'preimva': preimva,
        'primer': primer
    })
