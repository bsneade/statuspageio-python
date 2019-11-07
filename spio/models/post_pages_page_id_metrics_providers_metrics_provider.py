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


class PostPagesPageIdMetricsProvidersMetricsProvider(object):
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
        'email': 'str',
        'password': 'str',
        'api_key': 'str',
        'api_token': 'str',
        'application_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'email': 'email',
        'password': 'password',
        'api_key': 'api_key',
        'api_token': 'api_token',
        'application_key': 'application_key',
        'type': 'type'
    }

    def __init__(self, email=None, password=None, api_key=None, api_token=None, application_key=None, type=None, local_vars_configuration=None):  # noqa: E501
        """PostPagesPageIdMetricsProvidersMetricsProvider - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._password = None
        self._api_key = None
        self._api_token = None
        self._application_key = None
        self._type = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if api_key is not None:
            self.api_key = api_key
        if api_token is not None:
            self.api_token = api_token
        if application_key is not None:
            self.application_key = application_key
        if type is not None:
            self.type = type

    @property
    def email(self):
        """Gets the email of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501

        Required by the Librato and Pingdom type metrics providers.  # noqa: E501

        :return: The email of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostPagesPageIdMetricsProvidersMetricsProvider.

        Required by the Librato and Pingdom type metrics providers.  # noqa: E501

        :param email: The email of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501

        Required by the Pingdom-type metrics provider.  # noqa: E501

        :return: The password of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PostPagesPageIdMetricsProvidersMetricsProvider.

        Required by the Pingdom-type metrics provider.  # noqa: E501

        :param password: The password of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def api_key(self):
        """Gets the api_key of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501

        Required by the Datadog and NewRelic type metrics providers.  # noqa: E501

        :return: The api_key of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this PostPagesPageIdMetricsProvidersMetricsProvider.

        Required by the Datadog and NewRelic type metrics providers.  # noqa: E501

        :param api_key: The api_key of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def api_token(self):
        """Gets the api_token of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501

        Required by the Librato and Datadog type metrics providers.  # noqa: E501

        :return: The api_token of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this PostPagesPageIdMetricsProvidersMetricsProvider.

        Required by the Librato and Datadog type metrics providers.  # noqa: E501

        :param api_token: The api_token of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def application_key(self):
        """Gets the application_key of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501

        Required by the Pingdom-type metrics provider.  # noqa: E501

        :return: The application_key of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :rtype: str
        """
        return self._application_key

    @application_key.setter
    def application_key(self, application_key):
        """Sets the application_key of this PostPagesPageIdMetricsProvidersMetricsProvider.

        Required by the Pingdom-type metrics provider.  # noqa: E501

        :param application_key: The application_key of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :type: str
        """

        self._application_key = application_key

    @property
    def type(self):
        """Gets the type of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501

        One of \"Pingdom\", \"NewRelic\", \"Librato\", \"Datadog\", or \"Self\"  # noqa: E501

        :return: The type of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostPagesPageIdMetricsProvidersMetricsProvider.

        One of \"Pingdom\", \"NewRelic\", \"Librato\", \"Datadog\", or \"Self\"  # noqa: E501

        :param type: The type of this PostPagesPageIdMetricsProvidersMetricsProvider.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, PostPagesPageIdMetricsProvidersMetricsProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostPagesPageIdMetricsProvidersMetricsProvider):
            return True

        return self.to_dict() != other.to_dict()