import attr
import json
import os


def s3_or_file(instance, attribute, value):
    if instance.segment_file_list is None and instance.file_name is None:
        raise ValueError("Requires either segment_file_list or path_to_file")
    elif instance.segment_file_list is not None and instance.file_name is not None:
        raise ValueError("Cannot specify both segment_file_list and path_to_file")
    elif instance.segment_file_list is not None and not isinstance(instance.segment_file_list, list):
        raise ValueError("segment_file_list must be a list of string paths")


def upload_must_have_size(instance, attribute, value):
    if instance.file_name is not None:
        if instance.size_in_bytes is None:
            raise ValueError("Requires size_in_bytes")
        if not isinstance(instance.size_in_bytes, int) or instance.size_in_bytes is 0:
            raise ValueError("Requires valid size_in_bytes")


@attr.s(frozen=True)
class SegmentUpload(object):
    segment_file_list = attr.ib(default=None, validator=s3_or_file)
    file_name = attr.ib(default=None, validator=s3_or_file)
    size_in_bytes = attr.ib(default=None, validator=upload_must_have_size)
    file_format = attr.ib(default="BEESWAX")
    segment_key_type = attr.ib(default="DEFAULT")
    continent = attr.ib(default="NAM")
    user_id_type = attr.ib(default="OTHER_MOBILE_ID")
    account_id = attr.ib(default=2)

    def __attrs_post_init__(self):
        attr.validate(self)

    def __str__(self):
        return json.dumps(attr.asdict(self, filter=lambda _attr, value: value is not None))

    @staticmethod
    def from_file(sfile):
        file_size = os.stat(sfile).st_size
        su = SegmentUpload(file_name=sfile, size_in_bytes=file_size)
        return su
