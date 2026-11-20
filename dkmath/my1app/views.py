from django.shortcuts import render

def churn_rate(request):
    v = float(request.POST.get('initial', '0'))
    s = float(request.POST.get('lost', '0'))

    churn = (s / v) * 100 if request.method == 'POST' and v != 0 else 0

    print("initial customers =", v)
    print("customers lost =", s)
    print("churn rate =", churn)

    return render(request, 'my1app/churn.html', {'v': v, 's': s, 'churn': churn})