python-sample-code
==================

Sample client code for BaseKit's REST API

This example uses the following python module:

python-oauth2

# Installation on GNU/Linux
$ apt-get install python-oauth2

# Installation on OS X
https://github.com/simplegeo/python-oauth2

This code is just an example and it not intended to be used as a robust production solution, but give a good starting point on using the BaseKit API.

# Setting up

You will need a valid set of oauth security credentials, and these *need* to be updated in the OAuthClient.init method:

    self.credentials({
            'consumer_key': '',
            'consumer_secret': '',
            'access_token': '',
            'access_secret': ''
        })

You will also need to set the required api sever name, this can be set in the call to the 'BaseKitApi' constructor, i.e.

    api = BaseKitApi('api.example.com')

# Usage
    http_method = 'GET'
    parameters = []

    api = BaseKitApi('api.example.com')
    brand = api.call('/brands/1', http_method, parameters)
    print brand