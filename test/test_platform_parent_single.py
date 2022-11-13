# coding: utf-8

"""
    RAWG Video Games Database API

     The largest open video games database.  ### Why build on RAWG - More than 350,000 games for 50 platforms including mobiles. - Rich metadata: tags, genres, developers, publishers, individual creators, official websites, release dates, Metacritic ratings. - Where to buy: links to digital distribution services - Similar games based on visual similarity. - Player activity data: Steam average playtime and RAWG player counts and ratings. - Actively developing and constantly getting better by user contribution and our algorithms.  ### Terms of Use - Free for personal use as long as you attribute RAWG as the source of the data and/or images and add an active hyperlink from every page where the data of RAWG is used. - Free for commercial use for startups and hobby projects with not more than 100,000 monthly active users or 500,000 page views per month. If your project is larger than that, email us at [api@rawg.io](mailto:api@rawg.io) for commercial terms. - No cloning. It would not be cool if you used our API to launch a clone of RAWG. We know it is not always easy to say what is a duplicate and what isn't. Drop us a line at [api@rawg.io](mailto:api@rawg.io) if you are in doubt, and we will talk it through. - You must include an API key with every request. The key can be obtained at https://rawg.io/apidocs. If you don’t provide it, we may ban your requests.  __[Read more](https://rawg.io/apidocs)__.   # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rawg
from rawg.models.platform_parent_single import PlatformParentSingle  # noqa: E501
from rawg.rest import ApiException

class TestPlatformParentSingle(unittest.TestCase):
    """PlatformParentSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlatformParentSingle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rawg.models.platform_parent_single.PlatformParentSingle()  # noqa: E501
        if include_optional :
            return PlatformParentSingle(
                id = 56, 
                name = '0', 
                slug = 'z0', 
                platforms = [
                    rawg.models.platform.Platform(
                        id = 56, 
                        name = '0', 
                        slug = 'z0', 
                        games_count = 56, 
                        image_background = '', 
                        image = '', 
                        year_start = 0, 
                        year_end = 0, )
                    ]
            )
        else :
            return PlatformParentSingle(
                name = '0',
                platforms = [
                    rawg.models.platform.Platform(
                        id = 56, 
                        name = '0', 
                        slug = 'z0', 
                        games_count = 56, 
                        image_background = '', 
                        image = '', 
                        year_start = 0, 
                        year_end = 0, )
                    ],
        )

    def testPlatformParentSingle(self):
        """Test PlatformParentSingle"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
