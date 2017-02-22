import json
import requests


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

    # TODO: segment_upload call passing file, which automatically finds file_size
    # and then proceeds with upload using response's ID

    def segment_upload(self, su):
        return self.post(self.url('/rest/segment_upload'), data=str(su))

    def segment_upload_file(self, sid, sfile):
        files = {'file': ('segment_file', open(sfile, 'rb'), 'text/plain')}
        return self.post(self.url('/rest/segment_upload/upload/' + sid), files=files)

    def segment_update(self, su):
        return self.post(self.url('/rest/segment_update'), data=str(su))


class LoginException(Exception):
    pass
