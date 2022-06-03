import requests


class NGPMClient(object):
    def __init__(self, host, port, identity, secret, backend='https'):
        self.host = host
        self.port = int(port)
        self.identity = identity
        self.secret = secret
        self.backend = backend
        self.token = None

    def get_token(self):
        payload = {
            'identity': self.identity,
            'secret': self.secret
        }
        response = requests.post('tokens', payload)
        self.token = response.json()['token']