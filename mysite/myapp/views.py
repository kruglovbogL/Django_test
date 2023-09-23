from django.http import HttpResponse
from .models import Product

def index(request):
    latest_question_list = Product.name.order_by()[:5]
    Output = ", ".join([q.Product_text for q in latest_Product_list])
    return HttpResponse(Output)