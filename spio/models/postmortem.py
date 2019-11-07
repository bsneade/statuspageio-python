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


class Postmortem(object):
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
        'preview_key': 'str',
        'body': 'str',
        'body_updated_at': 'datetime',
        'body_draft': 'str',
        'body_draft_updated_at': 'datetime',
        'published_at': 'datetime',
        'notify_subscribers': 'bool',
        'notify_twitter': 'bool',
        'custom_tweet': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'preview_key': 'preview_key',
        'body': 'body',
        'body_updated_at': 'body_updated_at',
        'body_draft': 'body_draft',
        'body_draft_updated_at': 'body_draft_updated_at',
        'published_at': 'published_at',
        'notify_subscribers': 'notify_subscribers',
        'notify_twitter': 'notify_twitter',
        'custom_tweet': 'custom_tweet',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, preview_key=None, body=None, body_updated_at=None, body_draft=None, body_draft_updated_at=None, published_at=None, notify_subscribers=None, notify_twitter=None, custom_tweet=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Postmortem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._preview_key = None
        self._body = None
        self._body_updated_at = None
        self._body_draft = None
        self._body_draft_updated_at = None
        self._published_at = None
        self._notify_subscribers = None
        self._notify_twitter = None
        self._custom_tweet = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if preview_key is not None:
            self.preview_key = preview_key
        if body is not None:
            self.body = body
        if body_updated_at is not None:
            self.body_updated_at = body_updated_at
        if body_draft is not None:
            self.body_draft = body_draft
        if body_draft_updated_at is not None:
            self.body_draft_updated_at = body_draft_updated_at
        if published_at is not None:
            self.published_at = published_at
        if notify_subscribers is not None:
            self.notify_subscribers = notify_subscribers
        if notify_twitter is not None:
            self.notify_twitter = notify_twitter
        if custom_tweet is not None:
            self.custom_tweet = custom_tweet
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def preview_key(self):
        """Gets the preview_key of this Postmortem.  # noqa: E501

        Preview Key  # noqa: E501

        :return: The preview_key of this Postmortem.  # noqa: E501
        :rtype: str
        """
        return self._preview_key

    @preview_key.setter
    def preview_key(self, preview_key):
        """Sets the preview_key of this Postmortem.

        Preview Key  # noqa: E501

        :param preview_key: The preview_key of this Postmortem.  # noqa: E501
        :type: str
        """

        self._preview_key = preview_key

    @property
    def body(self):
        """Gets the body of this Postmortem.  # noqa: E501

        Postmortem body  # noqa: E501

        :return: The body of this Postmortem.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Postmortem.

        Postmortem body  # noqa: E501

        :param body: The body of this Postmortem.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def body_updated_at(self):
        """Gets the body_updated_at of this Postmortem.  # noqa: E501


        :return: The body_updated_at of this Postmortem.  # noqa: E501
        :rtype: datetime
        """
        return self._body_updated_at

    @body_updated_at.setter
    def body_updated_at(self, body_updated_at):
        """Sets the body_updated_at of this Postmortem.


        :param body_updated_at: The body_updated_at of this Postmortem.  # noqa: E501
        :type: datetime
        """

        self._body_updated_at = body_updated_at

    @property
    def body_draft(self):
        """Gets the body_draft of this Postmortem.  # noqa: E501

        Body draft  # noqa: E501

        :return: The body_draft of this Postmortem.  # noqa: E501
        :rtype: str
        """
        return self._body_draft

    @body_draft.setter
    def body_draft(self, body_draft):
        """Sets the body_draft of this Postmortem.

        Body draft  # noqa: E501

        :param body_draft: The body_draft of this Postmortem.  # noqa: E501
        :type: str
        """

        self._body_draft = body_draft

    @property
    def body_draft_updated_at(self):
        """Gets the body_draft_updated_at of this Postmortem.  # noqa: E501


        :return: The body_draft_updated_at of this Postmortem.  # noqa: E501
        :rtype: datetime
        """
        return self._body_draft_updated_at

    @body_draft_updated_at.setter
    def body_draft_updated_at(self, body_draft_updated_at):
        """Sets the body_draft_updated_at of this Postmortem.


        :param body_draft_updated_at: The body_draft_updated_at of this Postmortem.  # noqa: E501
        :type: datetime
        """

        self._body_draft_updated_at = body_draft_updated_at

    @property
    def published_at(self):
        """Gets the published_at of this Postmortem.  # noqa: E501


        :return: The published_at of this Postmortem.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this Postmortem.


        :param published_at: The published_at of this Postmortem.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

    @property
    def notify_subscribers(self):
        """Gets the notify_subscribers of this Postmortem.  # noqa: E501

        Should email subscribers be notified.  # noqa: E501

        :return: The notify_subscribers of this Postmortem.  # noqa: E501
        :rtype: bool
        """
        return self._notify_subscribers

    @notify_subscribers.setter
    def notify_subscribers(self, notify_subscribers):
        """Sets the notify_subscribers of this Postmortem.

        Should email subscribers be notified.  # noqa: E501

        :param notify_subscribers: The notify_subscribers of this Postmortem.  # noqa: E501
        :type: bool
        """

        self._notify_subscribers = notify_subscribers

    @property
    def notify_twitter(self):
        """Gets the notify_twitter of this Postmortem.  # noqa: E501

        Should Twitter followers be notified.  # noqa: E501

        :return: The notify_twitter of this Postmortem.  # noqa: E501
        :rtype: bool
        """
        return self._notify_twitter

    @notify_twitter.setter
    def notify_twitter(self, notify_twitter):
        """Sets the notify_twitter of this Postmortem.

        Should Twitter followers be notified.  # noqa: E501

        :param notify_twitter: The notify_twitter of this Postmortem.  # noqa: E501
        :type: bool
        """

        self._notify_twitter = notify_twitter

    @property
    def custom_tweet(self):
        """Gets the custom_tweet of this Postmortem.  # noqa: E501

        Custom tweet for Incident Postmortem  # noqa: E501

        :return: The custom_tweet of this Postmortem.  # noqa: E501
        :rtype: str
        """
        return self._custom_tweet

    @custom_tweet.setter
    def custom_tweet(self, custom_tweet):
        """Sets the custom_tweet of this Postmortem.

        Custom tweet for Incident Postmortem  # noqa: E501

        :param custom_tweet: The custom_tweet of this Postmortem.  # noqa: E501
        :type: str
        """

        self._custom_tweet = custom_tweet

    @property
    def created_at(self):
        """Gets the created_at of this Postmortem.  # noqa: E501


        :return: The created_at of this Postmortem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Postmortem.


        :param created_at: The created_at of this Postmortem.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Postmortem.  # noqa: E501


        :return: The updated_at of this Postmortem.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Postmortem.


        :param updated_at: The updated_at of this Postmortem.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Postmortem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Postmortem):
            return True

        return self.to_dict() != other.to_dict()