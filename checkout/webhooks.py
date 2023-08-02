from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe

from checkout.webhook_handler import StripeWH_Handler



# From walkthrough project webhooks.py
@require_POST
@csrf_exempt
def webhook(request):
    """
    Stripe webhook listener
    """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Receive webhook and verify sig
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid sig
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': (
            handler.handle_payment_intent_payment_failed
            ),
    }

    # Receive webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response