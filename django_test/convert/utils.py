import requests
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

def get_conversion_from_api(to_currency="EUR", from_currency="USD", amount=1):
    """
    Return currency conversion
    """
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {"apikey": settings.API_KEY}
    print(from_currency,to_currency)
    
    if to_currency == from_currency:
        return Response(
            {"success": False, "error": "Please provide different currency"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        response = requests.request("GET", url, headers=headers)
        if ( response.status_code == 200 and int(response.headers["X-RateLimit-Remaining-Day"]) > 1):        
            return response
        else:
            return {"success": False,"status_code":417}
    except:
        return Response(
            {"success": False, "error": "Something went wrong"},
            status=status.HTTP_417_EXPECTATION_FAILED,
        )
