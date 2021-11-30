#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_netsuite_openair import SourceNetsuiteOpenair

if __name__ == "__main__":
    source = SourceNetsuiteOpenair()
    launch(source, sys.argv[1:])
