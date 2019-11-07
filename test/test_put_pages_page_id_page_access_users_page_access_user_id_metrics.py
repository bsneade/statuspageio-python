# coding: utf-8

"""
    Statuspage API

    # Code of Conduct Please don't abuse the API, and please report all feature requests and issues to https://help.statuspage.io/help/contact-us-30  # Rate Limiting Each API token is limited to 1 request / second as measured on a 60 second rolling window. To get this limit increased or lifted, please contact us at https://help.statuspage.io/help/contact-us-30  # Basics  ## HTTPS It's required  ## URL Prefix In order to maintain version integrity into the future, the API is versioned. All calls currently begin with the following prefix:    https://api.statuspage.io/v1/  ## RESTful Interface Wherever possible, the API seeks to implement repeatable patterns with logical, representative URLs and descriptive HTTP verbs. Below are some examples and conventions you will see throughout the documentation.  * Collections are buckets: https://api.statuspage.io/v1/pages/asdf123/incidents.json * Elements have unique IDs: https://api.statuspage.io/v1/pages/asdf123/incidents/jklm456.json * GET will retrieve information about a collection/element * POST will create an element in a collection * PATCH will update a single element * PUT will replace a single element in a collection (rarely used) * DELETE will destroy a single element  ## Sending Data Information can be sent in the body as form urlencoded or JSON, but make sure the Content-Type header matches the body structure or the server gremlins will be angry.  All examples are provided in JSON format, however they can easily be converted to form encoding if required.  Some examples of how to convert things are below:      // JSON     {       \"incident\": {         \"name\": \"test incident\",         \"components\": [\"8kbf7d35c070\", \"vtnh60py4yd7\"]       }     }      // Form Encoded (using curl as an example):     curl -X POST https://api.statuspage.io/v1/example \\       -d \"incident[name]=test incident\" \\       -d \"incident[components][]=8kbf7d35c070\" \\       -d \"incident[components][]=vtnh60py4yd7\"  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import spio
from spio.models.put_pages_page_id_page_access_users_page_access_user_id_metrics import PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics  # noqa: E501
from spio.rest import ApiException


class TestPutPagesPageIdPageAccessUsersPageAccessUserIdMetrics(unittest.TestCase):
    """PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPutPagesPageIdPageAccessUsersPageAccessUserIdMetrics(self):
        """Test PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics"""
        # FIXME: construct object with mandatory attributes with example values
        # model = spio.models.put_pages_page_id_page_access_users_page_access_user_id_metrics.PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
