import pytest
import beeswax_api


def test_project_defines_author_and_version():
    assert hasattr(beeswax_api, '__author__')
    assert hasattr(beeswax_api, '__version__')
