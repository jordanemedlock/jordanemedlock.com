# -*- coding: utf-8 -*-

###############################################################################
#
# ListOrganizationsByUser
# Lists all organizations by user.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListOrganizationsByUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListOrganizationsByUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListOrganizationsByUser, self).__init__(temboo_session, '/Library/Zendesk/Organizations/ListOrganizationsByUser')


    def new_input_set(self):
        return ListOrganizationsByUserInputSet()

    def _make_result_set(self, result, path):
        return ListOrganizationsByUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrganizationsByUserChoreographyExecution(session, exec_id, path)

class ListOrganizationsByUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListOrganizationsByUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(ListOrganizationsByUserInputSet, self)._set_input('Email', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) ID of the user.)
        """
        super(ListOrganizationsByUserInputSet, self)._set_input('ID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number of the results to be returned. Used together with the Number parameter to paginate a large set of results.)
        """
        super(ListOrganizationsByUserInputSet, self)._set_input('Page', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(ListOrganizationsByUserInputSet, self)._set_input('Password', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page. Maximum is 100 and default is 100.)
        """
        super(ListOrganizationsByUserInputSet, self)._set_input('PerPage', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(ListOrganizationsByUserInputSet, self)._set_input('Server', value)

class ListOrganizationsByUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListOrganizationsByUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) The index for the next page of results.)
        """
        return self._output.get('NextPage', None)
    def get_PreviousPage(self):
        """
        Retrieve the value for the "PreviousPage" output from this Choreo execution. ((integer) The index for the previous page of results.)
        """
        return self._output.get('PreviousPage', None)

class ListOrganizationsByUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListOrganizationsByUserResultSet(response, path)
