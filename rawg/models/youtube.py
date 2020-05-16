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


class Youtube(object):
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
        'external_id': 'str',
        'channel_id': 'str',
        'channel_title': 'str',
        'name': 'str',
        'description': 'str',
        'created': 'datetime',
        'view_count': 'int',
        'comments_count': 'int',
        'like_count': 'int',
        'dislike_count': 'int',
        'favorite_count': 'int',
        'thumbnails': 'object'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'external_id',
        'channel_id': 'channel_id',
        'channel_title': 'channel_title',
        'name': 'name',
        'description': 'description',
        'created': 'created',
        'view_count': 'view_count',
        'comments_count': 'comments_count',
        'like_count': 'like_count',
        'dislike_count': 'dislike_count',
        'favorite_count': 'favorite_count',
        'thumbnails': 'thumbnails'
    }

    def __init__(self, id=None, external_id=None, channel_id=None, channel_title=None, name=None, description=None, created=None, view_count=None, comments_count=None, like_count=None, dislike_count=None, favorite_count=None, thumbnails=None, local_vars_configuration=None):  # noqa: E501
        """Youtube - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._external_id = None
        self._channel_id = None
        self._channel_title = None
        self._name = None
        self._description = None
        self._created = None
        self._view_count = None
        self._comments_count = None
        self._like_count = None
        self._dislike_count = None
        self._favorite_count = None
        self._thumbnails = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_title is not None:
            self.channel_title = channel_title
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created is not None:
            self.created = created
        if view_count is not None:
            self.view_count = view_count
        if comments_count is not None:
            self.comments_count = comments_count
        if like_count is not None:
            self.like_count = like_count
        if dislike_count is not None:
            self.dislike_count = dislike_count
        if favorite_count is not None:
            self.favorite_count = favorite_count
        if thumbnails is not None:
            self.thumbnails = thumbnails

    @property
    def id(self):
        """Gets the id of this Youtube.  # noqa: E501


        :return: The id of this Youtube.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Youtube.


        :param id: The id of this Youtube.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this Youtube.  # noqa: E501


        :return: The external_id of this Youtube.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Youtube.


        :param external_id: The external_id of this Youtube.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) < 1):
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_id = external_id

    @property
    def channel_id(self):
        """Gets the channel_id of this Youtube.  # noqa: E501


        :return: The channel_id of this Youtube.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this Youtube.


        :param channel_id: The channel_id of this Youtube.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                channel_id is not None and len(channel_id) < 1):
            raise ValueError("Invalid value for `channel_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._channel_id = channel_id

    @property
    def channel_title(self):
        """Gets the channel_title of this Youtube.  # noqa: E501


        :return: The channel_title of this Youtube.  # noqa: E501
        :rtype: str
        """
        return self._channel_title

    @channel_title.setter
    def channel_title(self, channel_title):
        """Sets the channel_title of this Youtube.


        :param channel_title: The channel_title of this Youtube.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                channel_title is not None and len(channel_title) < 1):
            raise ValueError("Invalid value for `channel_title`, length must be greater than or equal to `1`")  # noqa: E501

        self._channel_title = channel_title

    @property
    def name(self):
        """Gets the name of this Youtube.  # noqa: E501


        :return: The name of this Youtube.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Youtube.


        :param name: The name of this Youtube.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Youtube.  # noqa: E501


        :return: The description of this Youtube.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Youtube.


        :param description: The description of this Youtube.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def created(self):
        """Gets the created of this Youtube.  # noqa: E501


        :return: The created of this Youtube.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Youtube.


        :param created: The created of this Youtube.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def view_count(self):
        """Gets the view_count of this Youtube.  # noqa: E501


        :return: The view_count of this Youtube.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this Youtube.


        :param view_count: The view_count of this Youtube.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def comments_count(self):
        """Gets the comments_count of this Youtube.  # noqa: E501


        :return: The comments_count of this Youtube.  # noqa: E501
        :rtype: int
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this Youtube.


        :param comments_count: The comments_count of this Youtube.  # noqa: E501
        :type: int
        """

        self._comments_count = comments_count

    @property
    def like_count(self):
        """Gets the like_count of this Youtube.  # noqa: E501


        :return: The like_count of this Youtube.  # noqa: E501
        :rtype: int
        """
        return self._like_count

    @like_count.setter
    def like_count(self, like_count):
        """Sets the like_count of this Youtube.


        :param like_count: The like_count of this Youtube.  # noqa: E501
        :type: int
        """

        self._like_count = like_count

    @property
    def dislike_count(self):
        """Gets the dislike_count of this Youtube.  # noqa: E501


        :return: The dislike_count of this Youtube.  # noqa: E501
        :rtype: int
        """
        return self._dislike_count

    @dislike_count.setter
    def dislike_count(self, dislike_count):
        """Sets the dislike_count of this Youtube.


        :param dislike_count: The dislike_count of this Youtube.  # noqa: E501
        :type: int
        """

        self._dislike_count = dislike_count

    @property
    def favorite_count(self):
        """Gets the favorite_count of this Youtube.  # noqa: E501


        :return: The favorite_count of this Youtube.  # noqa: E501
        :rtype: int
        """
        return self._favorite_count

    @favorite_count.setter
    def favorite_count(self, favorite_count):
        """Sets the favorite_count of this Youtube.


        :param favorite_count: The favorite_count of this Youtube.  # noqa: E501
        :type: int
        """

        self._favorite_count = favorite_count

    @property
    def thumbnails(self):
        """Gets the thumbnails of this Youtube.  # noqa: E501


        :return: The thumbnails of this Youtube.  # noqa: E501
        :rtype: object
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this Youtube.


        :param thumbnails: The thumbnails of this Youtube.  # noqa: E501
        :type: object
        """

        self._thumbnails = thumbnails

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
        if not isinstance(other, Youtube):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Youtube):
            return True

        return self.to_dict() != other.to_dict()