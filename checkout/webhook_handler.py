# some of the code was copied from Boutique Ado project's repository
# and modified according to the project's needs
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import Profile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'confirmation_email/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'confirmation_email/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        final_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            if save_info:
                profile.user_phone_number = shipping_details.phone
                profile.user_country = shipping_details.address.country
                profile.user_postcode = shipping_details.address.postal_code
                profile.user_town_or_city = shipping_details.address.city
                profile.user_address_line1 = shipping_details.address.line1
                profile.user_address_line2 = shipping_details.address.line2
                profile.user_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    final_total=final_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} |\
                          SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, options_in_cart in json.loads(cart).items():
                    for options, quantity in\
                     options_in_cart['items_by_options'].items():
                        options = options.split('-')
                        color = options[1]
                        size = options[2]
                        components = options[3]
                        product = Product.objects.get(id=item_id)
                        quantity = int(quantity)
                        if components == 'alloy':
                            price = int(product.price_alloy)
                        elif components == 'carbon':
                            price = int(product.price_carbon)
                        else:
                            price = int(product.price)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_color=color,
                            product_size=size,
                            product_components=components,
                            price=price,
                        )
                        order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} |\
                     SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
