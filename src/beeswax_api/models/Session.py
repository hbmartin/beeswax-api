import requests, json

class Session(requests.Session):
    _url_ = ""
    
    def url(self, path):
        return self._url_ + path

    def login(self, _url, auth_data):
        self._url_ = _url
        resp = self.post(self.url('/rest/authenticate'), data=json.dumps(auth_data))
        if not resp.ok:
            raise LoginException()
        return self
    
    def segments(self):
        return self.get(self.url('/rest/segment')).json()

class LoginException(Exception):
    pass