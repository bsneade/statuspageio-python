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


class Subscriber(object):
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
        'id': 'str',
        'skip_confirmation_notification': 'bool',
        'mode': 'str',
        'email': 'str',
        'endpoint': 'str',
        'phone_number': 'str',
        'phone_country': 'str',
        'display_phone_number': 'str',
        'quarantined_at': 'datetime',
        'purge_at': 'datetime',
        'components': 'str',
        'page_access_user_id': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'skip_confirmation_notification': 'skip_confirmation_notification',
        'mode': 'mode',
        'email': 'email',
        'endpoint': 'endpoint',
        'phone_number': 'phone_number',
        'phone_country': 'phone_country',
        'display_phone_number': 'display_phone_number',
        'quarantined_at': 'quarantined_at',
        'purge_at': 'purge_at',
        'components': 'components',
        'page_access_user_id': 'page_access_user_id',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, skip_confirmation_notification=None, mode=None, email=None, endpoint=None, phone_number=None, phone_country=None, display_phone_number=None, quarantined_at=None, purge_at=None, components=None, page_access_user_id=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """Subscriber - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._skip_confirmation_notification = None
        self._mode = None
        self._email = None
        self._endpoint = None
        self._phone_number = None
        self._phone_country = None
        self._display_phone_number = None
        self._quarantined_at = None
        self._purge_at = None
        self._components = None
        self._page_access_user_id = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if skip_confirmation_notification is not None:
            self.skip_confirmation_notification = skip_confirmation_notification
        if mode is not None:
            self.mode = mode
        if email is not None:
            self.email = email
        if endpoint is not None:
            self.endpoint = endpoint
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_country is not None:
            self.phone_country = phone_country
        if display_phone_number is not None:
            self.display_phone_number = display_phone_number
        if quarantined_at is not None:
            self.quarantined_at = quarantined_at
        if purge_at is not None:
            self.purge_at = purge_at
        if components is not None:
            self.components = components
        if page_access_user_id is not None:
            self.page_access_user_id = page_access_user_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this Subscriber.  # noqa: E501

        Subscriber Identifier  # noqa: E501

        :return: The id of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscriber.

        Subscriber Identifier  # noqa: E501

        :param id: The id of this Subscriber.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def skip_confirmation_notification(self):
        """Gets the skip_confirmation_notification of this Subscriber.  # noqa: E501

        If this is true, do not notify the user with changes to their subscription.  # noqa: E501

        :return: The skip_confirmation_notification of this Subscriber.  # noqa: E501
        :rtype: bool
        """
        return self._skip_confirmation_notification

    @skip_confirmation_notification.setter
    def skip_confirmation_notification(self, skip_confirmation_notification):
        """Sets the skip_confirmation_notification of this Subscriber.

        If this is true, do not notify the user with changes to their subscription.  # noqa: E501

        :param skip_confirmation_notification: The skip_confirmation_notification of this Subscriber.  # noqa: E501
        :type: bool
        """

        self._skip_confirmation_notification = skip_confirmation_notification

    @property
    def mode(self):
        """Gets the mode of this Subscriber.  # noqa: E501

        The communication mode of the subscriber.  # noqa: E501

        :return: The mode of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Subscriber.

        The communication mode of the subscriber.  # noqa: E501

        :param mode: The mode of this Subscriber.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def email(self):
        """Gets the email of this Subscriber.  # noqa: E501

        The email address to use to contact the subscriber. Used for Email and Webhook subscribers.  # noqa: E501

        :return: The email of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Subscriber.

        The email address to use to contact the subscriber. Used for Email and Webhook subscribers.  # noqa: E501

        :param email: The email of this Subscriber.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def endpoint(self):
        """Gets the endpoint of this Subscriber.  # noqa: E501

        The URL where a webhook subscriber elects to receive updates.  # noqa: E501

        :return: The endpoint of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this Subscriber.

        The URL where a webhook subscriber elects to receive updates.  # noqa: E501

        :param endpoint: The endpoint of this Subscriber.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def phone_number(self):
        """Gets the phone_number of this Subscriber.  # noqa: E501

        The phone number used to contact an SMS subscriber  # noqa: E501

        :return: The phone_number of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Subscriber.

        The phone number used to contact an SMS subscriber  # noqa: E501

        :param phone_number: The phone_number of this Subscriber.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_country(self):
        """Gets the phone_country of this Subscriber.  # noqa: E501

        The two-character country code representing the country of which the phone_number is a part.  # noqa: E501

        :return: The phone_country of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._phone_country

    @phone_country.setter
    def phone_country(self, phone_country):
        """Sets the phone_country of this Subscriber.

        The two-character country code representing the country of which the phone_number is a part.  # noqa: E501

        :param phone_country: The phone_country of this Subscriber.  # noqa: E501
        :type: str
        """

        self._phone_country = phone_country

    @property
    def display_phone_number(self):
        """Gets the display_phone_number of this Subscriber.  # noqa: E501

        A formatted version of the phone_number and phone_country pair, nicely formatted for display.  # noqa: E501

        :return: The display_phone_number of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._display_phone_number

    @display_phone_number.setter
    def display_phone_number(self, display_phone_number):
        """Sets the display_phone_number of this Subscriber.

        A formatted version of the phone_number and phone_country pair, nicely formatted for display.  # noqa: E501

        :param display_phone_number: The display_phone_number of this Subscriber.  # noqa: E501
        :type: str
        """

        self._display_phone_number = display_phone_number

    @property
    def quarantined_at(self):
        """Gets the quarantined_at of this Subscriber.  # noqa: E501

        The timestamp when the subscriber was quarantined due to an issue reaching them.  # noqa: E501

        :return: The quarantined_at of this Subscriber.  # noqa: E501
        :rtype: datetime
        """
        return self._quarantined_at

    @quarantined_at.setter
    def quarantined_at(self, quarantined_at):
        """Sets the quarantined_at of this Subscriber.

        The timestamp when the subscriber was quarantined due to an issue reaching them.  # noqa: E501

        :param quarantined_at: The quarantined_at of this Subscriber.  # noqa: E501
        :type: datetime
        """

        self._quarantined_at = quarantined_at

    @property
    def purge_at(self):
        """Gets the purge_at of this Subscriber.  # noqa: E501

        The timestamp when a quarantined subscriber will be purged (unsubscribed).  # noqa: E501

        :return: The purge_at of this Subscriber.  # noqa: E501
        :rtype: datetime
        """
        return self._purge_at

    @purge_at.setter
    def purge_at(self, purge_at):
        """Sets the purge_at of this Subscriber.

        The timestamp when a quarantined subscriber will be purged (unsubscribed).  # noqa: E501

        :param purge_at: The purge_at of this Subscriber.  # noqa: E501
        :type: datetime
        """

        self._purge_at = purge_at

    @property
    def components(self):
        """Gets the components of this Subscriber.  # noqa: E501

        The components for which the subscriber has elected to receive updates.  # noqa: E501

        :return: The components of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Subscriber.

        The components for which the subscriber has elected to receive updates.  # noqa: E501

        :param components: The components of this Subscriber.  # noqa: E501
        :type: str
        """

        self._components = components

    @property
    def page_access_user_id(self):
        """Gets the page_access_user_id of this Subscriber.  # noqa: E501

        The Page Access user this subscriber belongs to (only for audience-specific pages).  # noqa: E501

        :return: The page_access_user_id of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._page_access_user_id

    @page_access_user_id.setter
    def page_access_user_id(self, page_access_user_id):
        """Sets the page_access_user_id of this Subscriber.

        The Page Access user this subscriber belongs to (only for audience-specific pages).  # noqa: E501

        :param page_access_user_id: The page_access_user_id of this Subscriber.  # noqa: E501
        :type: str
        """

        self._page_access_user_id = page_access_user_id

    @property
    def created_at(self):
        """Gets the created_at of this Subscriber.  # noqa: E501


        :return: The created_at of this Subscriber.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Subscriber.


        :param created_at: The created_at of this Subscriber.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, Subscriber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscriber):
            return True

        return self.to_dict() != other.to_dict()