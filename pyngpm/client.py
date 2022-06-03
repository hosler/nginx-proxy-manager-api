import requests


class NGPMClient(object):
    def __init__(self, host, port, identity, secret, backend='https'):
        self.host = host
        self.port = int(port)
        self.identity = identity
        self.secret = secret
        self.backend = backend
        self.token = None
        self.url = f'{self.backend}://{self.host}:{self.port}/api'

    def get_token(self):
        payload = {
            'identity': self.identity,
            'secret': self.secret
        }
        response = requests.post(f'{self.url}/tokens', data=payload)
        self.token = response.json()['token']

    def create_vhost(self, domains, scheme, host, port):
        payload = {
            'domain_names': domains,
            'forward_scheme': scheme,
            'forward_host': host,
            'forward_port': port,
        }
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(f'{self.url}/nginx/proxy-hosts', json=payload, headers=headers)
        return response.json()

    def delete_vhost(self, vid):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.delete(f'{self.url}/nginx/proxy-hosts/{vid}', headers=headers)
        return response.json()


