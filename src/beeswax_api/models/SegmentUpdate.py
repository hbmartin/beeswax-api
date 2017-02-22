import attr, json

@attr.s
class SegmentUpdate(object):
    user_data = attr.ib(default=[])
    segment_key_type = attr.ib(default="DEFAULT")
    user_id_type = attr.ib(default="BEESWAX")
    
    def __attrs_post_init__(self):
        attr.validate(self)
    
    def __str__(self):
        return json.dumps(attr.asdict(self, filter = lambda _attr, value: value != None))
    
    def add_user(self, us):
        if not isinstance(us, UserSegment):
            raise ValueError("Can only add UserSegment")
        self.user_data.append(us)

@attr.s
class UserSegment(object):
    user_id = attr.ib()
    segments = attr.ib(default=[])
    
    def __str__(self):
        return json.dumps(attr.asdict(self, filter = lambda _attr, value: value != None))