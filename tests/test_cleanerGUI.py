from genedb import cleanerfunc

import pytest


def test_removespecchar():
    string = cleanerfunc.removespecchar("The big \"bad\" bear ran          across the lake")
    assert string == "The big bad bear ran across the lake"
