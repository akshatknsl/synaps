#!/usr/bin/env python -u
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2012 Samsung SDS Co., LTD
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from datetime import datetime
import os
import sys
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                                os.pardir, os.pardir))
if os.path.exists(os.path.join(possible_topdir, "synaps", "__init__.py")):
    sys.path.insert(0, possible_topdir)

from synaps.cep.check_spout import CheckSpout 
from synaps import flags
from synaps import log as logging
from synaps import utils


if __name__ == "__main__":
    flags.FLAGS(sys.argv)
    utils.default_flagfile()
    FLAGS = flags.FLAGS
    logging.setup_storm()
    CheckSpout().run()
