# coding: utf-8

"""
    Statuspage API

    # Code of Conduct Please don't abuse the API, and please report all feature requests and issues to https://help.statuspage.io/help/contact-us-30  # Rate Limiting Each API token is limited to 1 request / second as measured on a 60 second rolling window. To get this limit increased or lifted, please contact us at https://help.statuspage.io/help/contact-us-30  # Basics  ## HTTPS It's required  ## URL Prefix In order to maintain version integrity into the future, the API is versioned. All calls currently begin with the following prefix:    https://api.statuspage.io/v1/  ## RESTful Interface Wherever possible, the API seeks to implement repeatable patterns with logical, representative URLs and descriptive HTTP verbs. Below are some examples and conventions you will see throughout the documentation.  * Collections are buckets: https://api.statuspage.io/v1/pages/asdf123/incidents.json * Elements have unique IDs: https://api.statuspage.io/v1/pages/asdf123/incidents/jklm456.json * GET will retrieve information about a collection/element * POST will create an element in a collection * PATCH will update a single element * PUT will replace a single element in a collection (rarely used) * DELETE will destroy a single element  ## Sending Data Information can be sent in the body as form urlencoded or JSON, but make sure the Content-Type header matches the body structure or the server gremlins will be angry.  All examples are provided in JSON format, however they can easily be converted to form encoding if required.  Some examples of how to convert things are below:      // JSON     {       \"incident\": {         \"name\": \"test incident\",         \"components\": [\"8kbf7d35c070\", \"vtnh60py4yd7\"]       }     }      // Form Encoded (using curl as an example):     curl -X POST https://api.statuspage.io/v1/example \\       -d \"incident[name]=test incident\" \\       -d \"incident[components][]=8kbf7d35c070\" \\       -d \"incident[components][]=vtnh60py4yd7\"  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from spio.configuration import Configuration


class PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'wants_twitter_update': 'bool',
        'body': 'str',
        'display_at': 'datetime',
        'deliver_notifications': 'bool'
    }

    attribute_map = {
        'wants_twitter_update': 'wants_twitter_update',
        'body': 'body',
        'display_at': 'display_at',
        'deliver_notifications': 'deliver_notifications'
    }

    def __init__(self, wants_twitter_update=None, body=None, display_at=None, deliver_notifications=None, local_vars_configuration=None):  # noqa: E501
        """PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wants_twitter_update = None
        self._body = None
        self._display_at = None
        self._deliver_notifications = None
        self.discriminator = None

        if wants_twitter_update is not None:
            self.wants_twitter_update = wants_twitter_update
        if body is not None:
            self.body = body
        if display_at is not None:
            self.display_at = display_at
        if deliver_notifications is not None:
            self.deliver_notifications = deliver_notifications

    @property
    def wants_twitter_update(self):
        """Gets the wants_twitter_update of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501

        Controls whether to create twitter update.  # noqa: E501

        :return: The wants_twitter_update of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._wants_twitter_update

    @wants_twitter_update.setter
    def wants_twitter_update(self, wants_twitter_update):
        """Sets the wants_twitter_update of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.

        Controls whether to create twitter update.  # noqa: E501

        :param wants_twitter_update: The wants_twitter_update of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :type: bool
        """

        self._wants_twitter_update = wants_twitter_update

    @property
    def body(self):
        """Gets the body of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501

        Incident update body.  # noqa: E501

        :return: The body of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.

        Incident update body.  # noqa: E501

        :param body: The body of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def display_at(self):
        """Gets the display_at of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501

        Timestamp when incident update is happened.  # noqa: E501

        :return: The display_at of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._display_at

    @display_at.setter
    def display_at(self, display_at):
        """Sets the display_at of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.

        Timestamp when incident update is happened.  # noqa: E501

        :param display_at: The display_at of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :type: datetime
        """

        self._display_at = display_at

    @property
    def deliver_notifications(self):
        """Gets the deliver_notifications of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501

        Controls whether to delivery notifications.  # noqa: E501

        :return: The deliver_notifications of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._deliver_notifications

    @deliver_notifications.setter
    def deliver_notifications(self, deliver_notifications):
        """Sets the deliver_notifications of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.

        Controls whether to delivery notifications.  # noqa: E501

        :param deliver_notifications: The deliver_notifications of this PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate.  # noqa: E501
        :type: bool
        """

        self._deliver_notifications = deliver_notifications

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate):
            return True

        return self.to_dict() != other.to_dict()
