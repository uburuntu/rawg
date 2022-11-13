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


class CreatorRolesList200Response(object):
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
        'count': 'int',
        'next': 'str',
        'previous': 'str',
        'results': 'list[Position]'
    }

    attribute_map = {
        'count': 'count',
        'next': 'next',
        'previous': 'previous',
        'results': 'results'
    }

    def __init__(self, count=None, next=None, previous=None, results=None, local_vars_configuration=None):  # noqa: E501
        """CreatorRolesList200Response - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._next = None
        self._previous = None
        self._results = None
        self.discriminator = None

        self.count = count
        self.next = next
        self.previous = previous
        self.results = results

    @property
    def count(self):
        """Gets the count of this CreatorRolesList200Response.  # noqa: E501


        :return: The count of this CreatorRolesList200Response.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreatorRolesList200Response.


        :param count: The count of this CreatorRolesList200Response.  # noqa: E501
        :type count: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def next(self):
        """Gets the next of this CreatorRolesList200Response.  # noqa: E501


        :return: The next of this CreatorRolesList200Response.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this CreatorRolesList200Response.


        :param next: The next of this CreatorRolesList200Response.  # noqa: E501
        :type next: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this CreatorRolesList200Response.  # noqa: E501


        :return: The previous of this CreatorRolesList200Response.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this CreatorRolesList200Response.


        :param previous: The previous of this CreatorRolesList200Response.  # noqa: E501
        :type previous: str
        """

        self._previous = previous

    @property
    def results(self):
        """Gets the results of this CreatorRolesList200Response.  # noqa: E501


        :return: The results of this CreatorRolesList200Response.  # noqa: E501
        :rtype: list[Position]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this CreatorRolesList200Response.


        :param results: The results of this CreatorRolesList200Response.  # noqa: E501
        :type results: list[Position]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, CreatorRolesList200Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatorRolesList200Response):
            return True

        return self.to_dict() != other.to_dict()
