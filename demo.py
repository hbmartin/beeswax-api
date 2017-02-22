import os, sys
sys.path.append(os.path.join(os.getcwd(), 'src'))
import argparse
import json
import attr

from beeswax_api import __version__
from beeswax_api.SessionFactory import SessionFactory
from beeswax_api.models.SegmentUpload import SegmentUpload
from beeswax_api.models.SegmentUpdate import SegmentUpdate, UserSegment


def get_parser():
    parser = argparse.ArgumentParser('beeswax-api')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser

def main(args=None):

    parser = get_parser()
    args = parser.parse_args(args)

    factory = SessionFactory(url="https://XYZ.api.beeswax.com", email="", password="")
    session = factory.login()
    print(session.segments())
    su = SegmentUpload(segment_file_list=[""])
    print(su)
    # print(session.segment_upload(su))
    
    su2 = SegmentUpdate()
    us = UserSegment(user_id="1", segments=["segment-1"])
    su2.add_user(us)
    print(su2)

if __name__ == '__main__':
    main()