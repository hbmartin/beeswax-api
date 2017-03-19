import json
import os
import requests

from beeswax_api.models.SegmentUpload import SegmentUpload
from beeswax_api.Exceptions import LoginException, SegmentUploadException


class Session(requests.Session):
    _url_ = ""

    def url(self, path):
        return self._url_ + path

    def login(self, _url, auth_data):
        self._url_ = _url
        r = self.post(self.url('/rest/authenticate'), data=json.dumps(auth_data))
        if not r.ok:
            raise LoginException(r)
        return self

    def segments(self):
        return self.get(self.url('/rest/segment'))

    def segment_upload_local_file(self, sfile):
        su = SegmentUpload.from_file(sfile)
        r = self.segment_upload(su)
        if not r.ok:
            raise SegmentUploadException(r)
        rj = r.json()
        sid = rj['payload']['id']
        return self.segment_upload_file_id(sfile, sid)

    def segment_upload(self, su):
        return self.post(self.url('/rest/segment_upload'), data=str(su))

    def segment_upload_file_id(self, sfile, sid):
        file_name = os.path.basename(sfile)
        files = {'segment_file': (file_name, open(sfile, 'rb'), 'text/plain')}
        return self.post(self.url('/rest/segment_upload/upload/' + str(sid)), files=files)

    def segment_update(self, su):
        return self.post(self.url('/rest/segment_update'), data=str(su))
