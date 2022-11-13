# coding: utf-8

"""
    RAWG Video Games Database API

     The largest open video games database.  ### Why build on RAWG - More than 350,000 games for 50 platforms including mobiles. - Rich metadata: tags, genres, developers, publishers, individual creators, official websites, release dates, Metacritic ratings. - Where to buy: links to digital distribution services - Similar games based on visual similarity. - Player activity data: Steam average playtime and RAWG player counts and ratings. - Actively developing and constantly getting better by user contribution and our algorithms.  ### Terms of Use - Free for personal use as long as you attribute RAWG as the source of the data and/or images and add an active hyperlink from every page where the data of RAWG is used. - Free for commercial use for startups and hobby projects with not more than 100,000 monthly active users or 500,000 page views per month. If your project is larger than that, email us at [api@rawg.io](mailto:api@rawg.io) for commercial terms. - No cloning. It would not be cool if you used our API to launch a clone of RAWG. We know it is not always easy to say what is a duplicate and what isn't. Drop us a line at [api@rawg.io](mailto:api@rawg.io) if you are in doubt, and we will talk it through. - You must include an API key with every request. The key can be obtained at https://rawg.io/apidocs. If you don’t provide it, we may ban your requests.  __[Read more](https://rawg.io/apidocs)__.   # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rawg
from rawg.api.publishers_api import PublishersApi  # noqa: E501
from rawg.rest import ApiException


class TestPublishersApi(unittest.TestCase):
    """PublishersApi unit test stubs"""

    def setUp(self):
        self.api = rawg.api.publishers_api.PublishersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_publishers_list(self):
        """Test case for publishers_list

        Get a list of video game publishers.  # noqa: E501
        """
        pass

    def test_publishers_read(self):
        """Test case for publishers_read

        Get details of the publisher.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
