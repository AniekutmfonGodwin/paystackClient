import requests
import json

class Product:
    def __init__(self,headers):
        self.headers = headers
        


    def create_product(self,name,description,price,currency,**kwargs):
        """
            name:(String)	Name of product
            description:(String)	A description for this product
            Integer:(Price) should be in kobo if currency is NGN and pesewas for GHS
            currency	String	Currency in which price is set

            optional:
            limited (Boolean) Set to true if the product has limited stock. Leave as false if the product has unlimited stock
            quantity (Integer) Number of products in stock. Use if limited is true
        """
        kwargs['name'] = name
        kwargs['description'] = description
        kwargs['price'] = price
        kwargs['currency'] = currency
        payload = json.dumps(kwargs)
        url = "https://api.paystack.co/product"
        print("loading...")
        # r =requests.request("POST", url, headers=self.headers, data = payload)
        # result = json.loads(r.text)
        try:
            r =requests.request("POST", url, headers=self.headers, data = payload)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}

        print("DONE","status",result["status"])
        print("message",result["message"])
        return result

    def list_products(self,perPage,page,**kwargs):
        """
           Query Param
            perPage	Integer	Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
            page	Integer	Specify exactly what page you want to retrieve. If not specify we use a default value of 1.

            optional:
            from
            (Datetime)
            A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            to
            (Datetime)
            A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        """
        kwargs['perPage'] = perPage
        kwargs['page'] = page
        if kwargs.get("_from"):
            kwargs['from'] = kwargs.get("_from")
        # del kwargs['_from'] 
        params = kwargs
        url = "https://api.paystack.co/product"
        print("loading...")
        try:
            r =requests.request("GET", url, headers=self.headers, params = params)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])
        return result



    def fetch_product(self,id):
        """
           Path Param
            id	String	product id you want to fetch

        """
        
        url = f"https://api.paystack.co/product/{id}"
        print("loading...")
        try:
            r =requests.request("GET", url, headers=self.headers)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])
        return result


    def update_product(self,id,name,description,price,currency,**kwargs):
        """
           Query Param
            id	String	Product ID

            Body Param
            name	String	Name of product
            description	String	A description for this product
            price	Integer	Price should be in kobo if currency is NGN and pesewas for GHS
            currency	String	Currency in which price is set

            optional:
            limited
            (Boolean)
            Set to true if the product has limited stock. Leave as false if the product has unlimited stock
            quantity
            (Integer)
            Number of products in stock. Use if limited is true
        """
        kwargs['name'] = name
        kwargs['description'] = description
        kwargs['price'] = price
        kwargs['currency'] = currency
        payload = json.dumps(kwargs)
        url = f"https://api.paystack.co/product/{id}"
        print("loading...")

        try:
            r =requests.request("PUT", url, headers=self.headers,data=payload)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])
        return result



class Transactions:
    def __init__(self,headers):
        self.headers = headers

    # def initialize_transaction(self):
    #     pass

    def verify_transaction(self,reference):
        """
           Path Param
            reference	String	The transaction reference used to intiate the transaction
        """
        
        url = f"https://api.paystack.co/transaction/verify/{reference}"
        print("loading...")

        try:
            r =requests.request("GET", url, headers=self.headers)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])
        return result


    def list_transactions(self,perPage,page,**kwargs):
        """
           Query Param
            perPage	Integer	Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
            page	Integer	Specify exactly what page you want to retrieve. If not specify we use a default value of 1.

            Optional
            customer
            (Integer)
            Specify an ID for the customer whose transactions you want to retrieve
            status
            (String)
            Filter transactions by status ('failed', 'success', 'abandoned')
            from
            (Datetime)
            A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            to
            (Datetime)
            A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            amount
            (Integer)
            Filter transactions by amount. Specify the amount, in kobo if currency is NGN and pesewas if currency is GHS.
        """
        
        url = " https://api.paystack.co/transaction"
        print("loading...")
        kwargs['perPage'] = perPage
        kwargs['page'] = page
        

        try:
            r =requests.request("GET", url, headers=self.headers,params=kwargs)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}

        print("DONE","status",result["status"])
        print("message",result["message"])
        return result



    def fetch_transaction(self,id):
        """
           Path Param
            id	Integer	An ID for the transaction to fetch
        """
        
        url = f"https://api.paystack.co/transaction/{id}"
        print("loading...")
        
        try:
            r =requests.request("GET", url, headers=self.headers)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}

        print("DONE","status",result["status"])
        print("message",result["message"])
        return result

    # def charge_authorization(self):
    #     pass

    # def check_authorization(self):
    #     pass

    # def view_transaction_timeline(self):
    #     pass

    # def transaction_totals(self):
    #     pass

    def export_transactions(self):
        pass

    def partial_debit(self):
        pass







class PaymentPage:
    def __init__(self,headers):
        self.headers = headers


    def create_page(self,name,**kwargs):
        """
           

            Body Param
            name	String	Name of page

            optional:
            description
            (String)
            A description for this page
            amount
            (Integer)
            Amount should be in kobo if currency is NGN and pesewas for GHS
            slug
            (String)
            URL slug you would like to be associated with this page. Page will be accessible at https://paystack.com/pay/[slug]
            metadata
            (Object)
            Extra data to configure the payment page including subaccount, logo image, transaction charge
            redirect_url
            (String)
            If you would like Paystack to redirect someplace upon successful payment, specify the URL here.
            custom_fields
            (Array of Objects)
            If you would like to accept custom fields, specify them here. See sample code for details.
        """
        kwargs['name'] = name
        
        payload = json.dumps(kwargs)
        url = "https://api.paystack.co/page"
        print("loading...")
        try:
            r =requests.request("POST", url, headers=self.headers,data=payload)
            result = json.loads(r.text)
        except:
            result = {'status':False,'message':'no internet conection'}

        print("DONE","status",result["status"])
        print("message",result["message"])
        return result


    def list_pages(self,perPage,page,**kwargs):
        """
           Query Param
            perPage	Integer	Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
            page	Integer	Specify exactly what page you want to retrieve. If not specify we use a default value of 1.

            Optional param
            from
            (Datetime)
            A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            to
            (Datetime)
            A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        """
        kwargs['perPage'] = perPage
        kwargs['page'] = page
        
        # payload = json.dumps(kwargs)
        url = "https://api.paystack.co/page"
        print("loading...")

        try:
            r =requests.request("GET", url, headers=self.headers,params=kwargs)
            result = json.loads(r.text)
            
        except:
            result = {'status':False,'message':'no internet conection'}

        print("DONE","status",result["status"])
        print("message",result["message"])
        return json.loads(r.text)

    def fetch_page(self,id_or_slug):
        """
          Path Param
            id_or_slug	String	The page ID or slug you want to fetch
        """
        
        url = f"https://api.paystack.co/page{id_orslug}"
        print("loading...")

        try:
            r =requests.request("GET", url, headers=self.headers)
            result = json.loads(r.text)
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])
        return result


    def update_page(self,id_or_slug,name,description,**kwargs):
        """
          Headers
            id_or_slug	String	Page ID or slug

            Body Param
            name	String	Name of page
            description	String	A description for this page

            optional
            amount
            (Integer)
            Default amount you want to accept using this page. If none is set, customer is free to provide any amount of their choice. The latter scenario is useful for accepting donations
            active
            (Boolean)
            Set to false to deactivate page url
        """
        kwargs['name'] = name
        kwargs['description'] = description
        
        payload = json.dumps(kwargs)
        print("loading...")
        url = f"https://api.paystack.co/page{id_orslug}"

        try:
            r = requests.request("PUT", url, headers=self.headers,data=payload)
            result = json.loads(r.text)
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])

        return result


    def check_slug_availability(self,slug):
        """
          Path Param
            slug	String	URL slug to be confirmed
        """
        
        print("loading...")
        url = f"https://api.paystack.co/page/check_slug_availability/{slug}"

        try:
            r = requests.request("GET", url, headers=self.headers)
            result = json.loads(r.text)
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])
        return result


    def add_products(self,id,*args):
        """
          Headers
            id	Integer	Id of the payment page
            Body Param
            product	Array of Integer	Ids of all the products
        """
        payload = json.dumps(list(args))
        print("LOADING...")
        url = f"https://api.paystack.co/page/{id}/product"
        try:
            r = requests.request("POST", url, headers=self.headers,data=payload)
            result = json.loads(r.text)
        except:
            result = {'status':False,'message':'no internet conection'}
        print("DONE","status",result["status"])
        print("message",result["message"])

        return result
        



class Paystack:
    def __init__(self,secret_key):
        self.headers = {
            'Authorization': f'Bearer {secret_key}',
            'Content-Type': 'application/json',
            'Cookie': '__cfduid=d79e952cae386250527a228e45bcd86621599378182; sails.sid=s%3AAgHxS-pawZ9CRRe179v00Zx39FWNkqez.Y22k%2BmcElxoVBg9a8u17XrzclBVvhkmexITI944tQrk'
            }


    def paymentpage(self):
        return PaymentPage(self.headers)



    def product(self):
        return Product(self.headers)


    def transactions(self):
        return Transactions(self.headers)



