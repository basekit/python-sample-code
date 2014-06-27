#/usr/bin/env python

import oauth2
import httplib
import json


class OAuthClient():

    '''
    Very simple oauth client
    '''

    def __init__(self, url):
        self.credentials({
            'consumer_key': '',
            'consumer_secret': '',
            'access_token': '',
            'access_secret': ''
        })

        self.request = oauth2.Request.from_consumer_and_token(
            self.consumer,
            token=self.token,
            http_url=url
        )

        self.request.sign_request(
            oauth2.SignatureMethod_HMAC_SHA1(),
            self.consumer,
            self.token
        )

    def credentials(self, credentials):
        self.token = oauth2.Token(
            key=credentials['access_token'],
            secret=credentials['access_secret']
        )
        self.consumer = oauth2.Consumer(
            key=credentials['consumer_key'],
            secret=credentials['consumer_secret']
        )


class BaseKitApi():

    '''
    Returns a JSON responce to the API called
    '''

    def __init__(self, server='rest.example.com', port=80):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.server = server
        self.port = port

        if self.server[-1] is '/':
            self.server = self.server[:-1]

    def setHeaders(self, headers):
        self.headers = headers

    def call(self, request_url, http_method='GET', parameters=[]):
        if self.server not in request_url:
            if request_url[0] is not '/':
                url = "{0}/{1}".format(self.server, request_url)
            else:
                url = "{0}{1}".format(self.server, request_url)
        else:
            url = request_url

        if self.port == 80:
            url = "http://{0}".format(url)
        else:
            url = "https://{0}".format(url)

        client = OAuthClient(url)

        if http_method.upper() == "POST":
            encoded_post_data = client.request.to_postdata()
        else:
            encoded_post_data = None
            url = client.request.to_url()

        connection = httplib.HTTPConnection(
            "%s:%d" % (self.server, self.port)
        )

        connection.request(
            http_method.upper(),
            url,
            body=encoded_post_data,
            headers=self.headers
        )
        response = connection.getresponse().read()
        if response is None:
            return None
        else:
            return json.loads(response)


http_method = 'GET'
parameters = []

api = BaseKitApi('api.example.com')
brand = api.call('/brands/1', http_method, parameters)
print brand
