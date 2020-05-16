# coding: utf-8

"""
    RAWG Video Games Database API

     The largest open video games database.  ### Why build on RAWG - More than 350,000 games for 50 platforms including mobiles. - Rich metadata: tags, genres, developers, publishers, individual creators, official websites, release dates, Metacritic ratings. - Where to buy: links to digital distribution services - Similar games based on visual similarity. - Player activity data: Steam average playtime and RAWG player counts and ratings. - Actively developing and constantly getting better by user contribution and our algorithms.  ### Terms of Use - Free for personal use as long as you attribute RAWG as the source of the data and/or images and add an active hyperlink from every page where the data of RAWG is used. - Free for commercial use for startups and hobby projects with not more than 100,000 monthly active users or 500,000 page views per month. If your project is larger than that, email us at [api@rawg.io](mailto:api@rawg.io) for commercial terms. - No cloning. It would not be cool if you used our API to launch a clone of RAWG. We know it is not always easy to say what is a duplicate and what isn't. Drop us a line at [api@rawg.io](mailto:api@rawg.io) if you are in doubt, and we will talk it through. - Every API request should have a User-Agent header with your app name. If you don’t provide it, we may ban your requests.  __[Read more](https://rawg.io/apidocs)__.   # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from rawg.configuration import Configuration


class Twitch(object):
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
        'id': 'int',
        'external_id': 'int',
        'name': 'str',
        'description': 'str',
        'created': 'datetime',
        'published': 'datetime',
        'thumbnail': 'str',
        'view_count': 'int',
        'language': 'str'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'external_id',
        'name': 'name',
        'description': 'description',
        'created': 'created',
        'published': 'published',
        'thumbnail': 'thumbnail',
        'view_count': 'view_count',
        'language': 'language'
    }

    def __init__(self, id=None, external_id=None, name=None, description=None, created=None, published=None, thumbnail=None, view_count=None, language=None, local_vars_configuration=None):  # noqa: E501
        """Twitch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._external_id = None
        self._name = None
        self._description = None
        self._created = None
        self._published = None
        self._thumbnail = None
        self._view_count = None
        self._language = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created is not None:
            self.created = created
        if published is not None:
            self.published = published
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if view_count is not None:
            self.view_count = view_count
        if language is not None:
            self.language = language

    @property
    def id(self):
        """Gets the id of this Twitch.  # noqa: E501


        :return: The id of this Twitch.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Twitch.


        :param id: The id of this Twitch.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this Twitch.  # noqa: E501


        :return: The external_id of this Twitch.  # noqa: E501
        :rtype: int
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Twitch.


        :param external_id: The external_id of this Twitch.  # noqa: E501
        :type: int
        """

        self._external_id = external_id

    @property
    def name(self):
        """Gets the name of this Twitch.  # noqa: E501


        :return: The name of this Twitch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Twitch.


        :param name: The name of this Twitch.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Twitch.  # noqa: E501


        :return: The description of this Twitch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Twitch.


        :param description: The description of this Twitch.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def created(self):
        """Gets the created of this Twitch.  # noqa: E501


        :return: The created of this Twitch.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Twitch.


        :param created: The created of this Twitch.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def published(self):
        """Gets the published of this Twitch.  # noqa: E501


        :return: The published of this Twitch.  # noqa: E501
        :rtype: datetime
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this Twitch.


        :param published: The published of this Twitch.  # noqa: E501
        :type: datetime
        """

        self._published = published

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Twitch.  # noqa: E501


        :return: The thumbnail of this Twitch.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Twitch.


        :param thumbnail: The thumbnail of this Twitch.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                thumbnail is not None and len(thumbnail) < 1):
            raise ValueError("Invalid value for `thumbnail`, length must be greater than or equal to `1`")  # noqa: E501

        self._thumbnail = thumbnail

    @property
    def view_count(self):
        """Gets the view_count of this Twitch.  # noqa: E501


        :return: The view_count of this Twitch.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this Twitch.


        :param view_count: The view_count of this Twitch.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def language(self):
        """Gets the language of this Twitch.  # noqa: E501


        :return: The language of this Twitch.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Twitch.


        :param language: The language of this Twitch.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) < 1):
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

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
        if not isinstance(other, Twitch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Twitch):
            return True

        return self.to_dict() != other.to_dict()