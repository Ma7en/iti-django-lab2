from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def account_list(request):
    context = {}
    accounts = Account.objects.all()  # Fetch all records from the database
    context["accounts"] = accounts
    return render(request, "account/list.html", context)


def account_create(request):
    context = {}
    if request.method == "POST":
        # validation on the server side
        if (
            len(request.POST["username"]) > 0
            and len(request.POST["username"]) <= 100
            and len(request.POST["password"]) <= 200
            and request.POST["email"]
        ):
            accountobj = Account()
            accountobj.username = request.POST["username"]
            accountobj.email = request.POST["email"]
            accountobj.password = request.POST["password"]
            accountobj.save()
            return redirect("account_list")
        else:
            context["error"] = "Invalid data"

    return render(request, "account/create.html", context)


def account_update(request, id):
    context = {}
    try:
        account = Account.objects.get(id=id)  # Fetch the account to be updated
        if request.method == "POST":
            if (
                len(request.POST["username"]) > 0
                and len(request.POST["username"]) <= 100
                and len(request.POST["password"]) <= 200
                and request.POST["email"]
            ):
                account.username = request.POST["username"]
                account.email = request.POST["email"]
                account.password = request.POST["password"]
                account.save()
                return redirect("account_list")
            else:
                context["error"] = "Invalid data"
        context["account"] = account
    except Account.DoesNotExist:
        return HttpResponse("Account not found", status=404)
    return render(request, "account/update.html", context)


def account_delete(request, id):
    context = {}
    try:
        account = Account.objects.get(id=id)  # Fetch the account to be deleted
        if request.method == "POST":
            account.delete()
            return redirect("account_list")
        context["account"] = account
    except Account.DoesNotExist:
        return HttpResponse("Account not found", status=404)
    return render(request, "account/delete.html", context)


def account_details(request, id):
    context = {}
    account = Account.objects.get(id=id)  # Fetch record from the database
    context["account"] = account
    return render(request, "account/details.html", context)
