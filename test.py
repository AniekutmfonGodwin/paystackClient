import requests
import json
from main.paystack import Paystack


paystack = Paystack("PAYSTACK_SECRET_KEY")

respond = paystack.transactions().verify_transaction("REFRENCE_CODE")







print(respond)