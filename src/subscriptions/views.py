from django.shortcuts import render, redirect
from subscriptions.models import SubscriptionPrice, UserSubscription
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import helpers.billing
from django.contrib import messages
from subscriptions import utils as subs_utils

# Create your views here.


@login_required
def user_subscription_view(request):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    # sub_data = user_sub_obj.serialize()
    if request.method == "POST":
        print("refresh subscription")
        finished = subs_utils.refresh_active_users_subscriptions(
            user_ids=[request.user.id], active_only=False
        )
        if finished:
            messages.success(request, "Your plan has been refreshed.")
        else:
            messages.error(
                request, "Your plan details have not been refreshed, please try again."
            )
        return redirect(user_sub_obj.get_absolute_url())

    context = {
        "subscription": user_sub_obj,
    }
    return render(request, "subscriptions/user_detail_view.html", context)


@login_required
def user_subscription_cancel_view(request):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    # sub_data = user_sub_obj.serialize()
    if request.method == "POST":
        print("refresh subscription")
        if user_sub_obj.stripe_id and user_sub_obj.is_active_status:
            sub_data = helpers.billing.cancel_subscription(
                user_sub_obj.stripe_id,
                reason="User wanted to end",
                feedback="other",
                cancel_at_period_end=True,
                raw=False,
            )
            for k, v in sub_data.items():
                setattr(user_sub_obj, k, v)
            user_sub_obj.save()
            messages.success(request, "Your plan has been cancelled.")
        return redirect(user_sub_obj.get_absolute_url())

    context = {
        "subscription": user_sub_obj,
    }
    return render(request, "subscriptions/user_cancel_view.html", context)


def subscription_price_view(request, interval="month"):
    qs = SubscriptionPrice.objects.filter(featured=True)
    inv_mo = SubscriptionPrice.IntervalChoices.MONTHLY
    inv_yr = SubscriptionPrice.IntervalChoices.YEARLY
    object_list = qs.filter(interval=inv_mo)
    url_path_name = "pricing_interval"
    mo_url = reverse(url_path_name, kwargs={"interval": inv_mo})
    yr_url = reverse(url_path_name, kwargs={"interval": inv_yr})
    active = inv_mo
    if interval == inv_yr:
        active = inv_yr
        object_list = qs.filter(interval=inv_yr)
    context = {
        "object_list": object_list,
        "mo_url": mo_url,
        "yr_url": yr_url,
        "active": active,
    }
    return render(request, "subscriptions/pricing.html", context)
