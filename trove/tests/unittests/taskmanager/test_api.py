# Copyright 2014 eBay Software Foundation
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

from mock import Mock
from mock import patch

from trove.common.strategies.cluster.experimental.mongodb.taskmanager import (
    MongoDbTaskManagerAPI)
from trove.taskmanager import api as task_api
from trove.tests.unittests import trove_testtools


class TestAPI(trove_testtools.TestCase):

    @patch.object(task_api.API, 'get_client')
    def test_load_api(self, get_client_mock):
        context = Mock()
        manager = 'mongodb'

        self.assertTrue(isinstance(task_api.load(context), task_api.API))
        self.assertTrue(isinstance(task_api.load(context, manager),
                                   MongoDbTaskManagerAPI))
