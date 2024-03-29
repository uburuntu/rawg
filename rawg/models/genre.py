# coding: utf-8

"""
    RAWG Video Games Database API

     The largest open video games database.  ### Why build on RAWG - More than 350,000 games for 50 platforms including mobiles. - Rich metadata: tags, genres, developers, publishers, individual creators, official websites, release dates, Metacritic ratings. - Where to buy: links to digital distribution services - Similar games based on visual similarity. - Player activity data: Steam average playtime and RAWG player counts and ratings. - Actively developing and constantly getting better by user contribution and our algorithms.  ### Terms of Use - Free for personal use as long as you attribute RAWG as the source of the data and/or images and add an active hyperlink from every page where the data of RAWG is used. - Free for commercial use for startups and hobby projects with not more than 100,000 monthly active users or 500,000 page views per month. If your project is larger than that, email us at [api@rawg.io](mailto:api@rawg.io) for commercial terms. - No cloning. It would not be cool if you used our API to launch a clone of RAWG. We know it is not always easy to say what is a duplicate and what isn't. Drop us a line at [api@rawg.io](mailto:api@rawg.io) if you are in doubt, and we will talk it through. - You must include an API key with every request. The key can be obtained at https://rawg.io/apidocs. If you don’t provide it, we may ban your requests.  __[Read more](https://rawg.io/apidocs)__.   # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from rawg.configuration import Configuration


class Genre(object):
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
        'name': 'str',
        'slug': 'str',
        'games_count': 'int',
        'image_background': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'games_count': 'games_count',
        'image_background': 'image_background'
    }

    def __init__(self, id=None, name=None, slug=None, games_count=None, image_background=None, local_vars_configuration=None):  # noqa: E501
        """Genre - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._slug = None
        self._games_count = None
        self._image_background = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if slug is not None:
            self.slug = slug
        if games_count is not None:
            self.games_count = games_count
        if image_background is not None:
            self.image_background = image_background

    @property
    def id(self):
        """Gets the id of this Genre.  # noqa: E501


        :return: The id of this Genre.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Genre.


        :param id: The id of this Genre.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Genre.  # noqa: E501


        :return: The name of this Genre.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Genre.


        :param name: The name of this Genre.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Genre.  # noqa: E501


        :return: The slug of this Genre.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Genre.


        :param slug: The slug of this Genre.  # noqa: E501
        :type slug: str
        """
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and len(slug) < 1):
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug)):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def games_count(self):
        """Gets the games_count of this Genre.  # noqa: E501


        :return: The games_count of this Genre.  # noqa: E501
        :rtype: int
        """
        return self._games_count

    @games_count.setter
    def games_count(self, games_count):
        """Sets the games_count of this Genre.


        :param games_count: The games_count of this Genre.  # noqa: E501
        :type games_count: int
        """

        self._games_count = games_count

    @property
    def image_background(self):
        """Gets the image_background of this Genre.  # noqa: E501


        :return: The image_background of this Genre.  # noqa: E501
        :rtype: str
        """
        return self._image_background

    @image_background.setter
    def image_background(self, image_background):
        """Sets the image_background of this Genre.


        :param image_background: The image_background of this Genre.  # noqa: E501
        :type image_background: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_background is not None and len(image_background) < 1):
            raise ValueError("Invalid value for `image_background`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_background = image_background

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Genre):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Genre):
            return True

        return self.to_dict() != other.to_dict()
