from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle unexpected/unknown event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle Stripe payment_intent_succeeded webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle Stripe payment_intent_payment_failed webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)