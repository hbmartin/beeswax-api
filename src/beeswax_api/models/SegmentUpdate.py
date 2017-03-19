import attr
import json


@attr.s
class SegmentUpdate(object):
    user_data = attr.ib(default=[])
    segment_key_type = attr.ib(default="DEFAULT")
    user_id_type = attr.ib(default="BEESWAX")

    def __attrs_post_init__(self):
        attr.validate(self)

    def __str__(self):
        return json.dumps(attr.asdict(self, filter=lambda _attr, value: value is not None))

    def add_user(self, us):
        if not isinstance(us, UserSegment):
            raise ValueError("Can only add UserSegment")
        self.user_data.append(us)

    def add_user_dict(self, users):
        for key, val in users.items():
            self.add_user(UserSegment(user_id=key, segments=val))


@attr.s
class UserSegment(object):
    user_id = attr.ib()
    segments = attr.ib(default=[])

    def __str__(self):
        return json.dumps(attr.asdict(self, filter=lambda _attr, value: value is not None))
