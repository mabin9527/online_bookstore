from django.http import HttpResponse


# From walkthrough project webhook handler
class StripeWH_Handler:
    """
    Handle webhook for Stripe
    """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
    """
    Handle webhook event of generic, unknown, unexpected
    """
    return HttpResponse(
        content=f'Unhandled webhook received: {event["type"]}',
        status=200)