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


class PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig(object):
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
        'position': 'str',
        'incident_background_color': 'str',
        'incident_text_color': 'str',
        'maintenance_background_color': 'str',
        'maintenance_text_color': 'str'
    }

    attribute_map = {
        'position': 'position',
        'incident_background_color': 'incident_background_color',
        'incident_text_color': 'incident_text_color',
        'maintenance_background_color': 'maintenance_background_color',
        'maintenance_text_color': 'maintenance_text_color'
    }

    def __init__(self, position=None, incident_background_color=None, incident_text_color=None, maintenance_background_color=None, maintenance_text_color=None, local_vars_configuration=None):  # noqa: E501
        """PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._position = None
        self._incident_background_color = None
        self._incident_text_color = None
        self._maintenance_background_color = None
        self._maintenance_text_color = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if incident_background_color is not None:
            self.incident_background_color = incident_background_color
        if incident_text_color is not None:
            self.incident_text_color = incident_text_color
        if maintenance_background_color is not None:
            self.maintenance_background_color = maintenance_background_color
        if maintenance_text_color is not None:
            self.maintenance_text_color = maintenance_text_color

    @property
    def position(self):
        """Gets the position of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501

        Corner where status embed iframe will appear on page  # noqa: E501

        :return: The position of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.

        Corner where status embed iframe will appear on page  # noqa: E501

        :param position: The position of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def incident_background_color(self):
        """Gets the incident_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501

        Color of status embed iframe background when displaying incident  # noqa: E501

        :return: The incident_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :rtype: str
        """
        return self._incident_background_color

    @incident_background_color.setter
    def incident_background_color(self, incident_background_color):
        """Sets the incident_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.

        Color of status embed iframe background when displaying incident  # noqa: E501

        :param incident_background_color: The incident_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :type: str
        """

        self._incident_background_color = incident_background_color

    @property
    def incident_text_color(self):
        """Gets the incident_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501

        Color of status embed iframe text when displaying incident  # noqa: E501

        :return: The incident_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :rtype: str
        """
        return self._incident_text_color

    @incident_text_color.setter
    def incident_text_color(self, incident_text_color):
        """Sets the incident_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.

        Color of status embed iframe text when displaying incident  # noqa: E501

        :param incident_text_color: The incident_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :type: str
        """

        self._incident_text_color = incident_text_color

    @property
    def maintenance_background_color(self):
        """Gets the maintenance_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501

        Color of status embed iframe background when displaying maintenance  # noqa: E501

        :return: The maintenance_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_background_color

    @maintenance_background_color.setter
    def maintenance_background_color(self, maintenance_background_color):
        """Sets the maintenance_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.

        Color of status embed iframe background when displaying maintenance  # noqa: E501

        :param maintenance_background_color: The maintenance_background_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :type: str
        """

        self._maintenance_background_color = maintenance_background_color

    @property
    def maintenance_text_color(self):
        """Gets the maintenance_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501

        Color of status embed iframe text when displaying maintenance  # noqa: E501

        :return: The maintenance_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_text_color

    @maintenance_text_color.setter
    def maintenance_text_color(self, maintenance_text_color):
        """Sets the maintenance_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.

        Color of status embed iframe text when displaying maintenance  # noqa: E501

        :param maintenance_text_color: The maintenance_text_color of this PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig.  # noqa: E501
        :type: str
        """

        self._maintenance_text_color = maintenance_text_color

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
        if not isinstance(other, PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig):
            return True

        return self.to_dict() != other.to_dict()
