from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_conversion_from_api

response = get_conversion_from_api()

status_code = response.status_code
result = response.text


class CurrencyConvertor(APIView):
    """
        Get Pair curency Conversion from api

        * Params: to_currency, from_currency, amount
        * Response json with success, error, result
        * Example: api/v1/convert/?to_currency=EUR&from_currency=USD&amount=100
        {
        "success": true,
        "query": {
            "from": "USD",
            "to": "EUR",
            "amount": 100
        },
        "info": {
            "timestamp": 1674513903,
            "rate": 0.91985
        },
        "date": "2023-01-23",
        "result": 91.985
    }
    """
    def param_validators(self,to_currency,from_currency,amount):
        self.validate_data = {"EUR", "USD", "JPY"}
        if not to_currency or not from_currency or not amount:
            return Response(
                {
                    "success": False,
                    "error": "Please provide Amount, to currency, from currency",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if (
            to_currency not in self.validate_data
            or from_currency not in self.validate_data
        ):
            return Response(
                {
                    "success": False,
                    "error": "Please provide valid currency EUR,USD, JPY",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        

        try:
            if float(amount) < 0:
                return Response(
                    {
                        "success": False,
                        "error": "Please provide Amount greater than 0",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            return Response(
                {"success": False, "error": "Please provide Amount"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    

    def get(self, request, format=None):
        """
        Return currency conversion
        """
        to_currency = request.GET.get("to_currency")
        from_currency = request.GET.get("from_currency")
        amount = request.GET.get("amount")
        self.param_validators(to_currency,from_currency,amount)
        
        
        response = get_conversion_from_api(to_currency, from_currency, amount)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        
        else:
            return Response(
                {"success": False, "error": "Something went wrong with api"},
                status=status.HTTP_417_EXPECTATION_FAILED,
            )
       
       

      
