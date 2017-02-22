import attr
from beeswax_api.models import Session


@attr.s
class SessionFactory(object):
    url = attr.ib()
    email = attr.ib()
    password = attr.ib()

    def login(self):
        _session = Session.Session()
        return _session.login(self.url,
                              auth_data={
                                    'email': self.email,
                                    'password': self.password,
                                    'keep_logged_in': True})
