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
from rawg.models.game import Game  # noqa: E501
from rawg.rest import ApiException

class TestGame(unittest.TestCase):
    """Game unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Game
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rawg.models.game.Game()  # noqa: E501
        if include_optional :
            return Game(
                id = 56, 
                slug = 'z0', 
                name = '0', 
                released = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                tba = True, 
                background_image = '', 
                rating = 1.337, 
                rating_top = 56, 
                ratings = rawg.models.ratings.Ratings(), 
                ratings_count = 56, 
                reviews_text_count = '', 
                added = 56, 
                added_by_status = rawg.models.added_by_status.Added by status(), 
                metacritic = 56, 
                playtime = 56, 
                suggestions_count = 56, 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                esrb_rating = rawg.models.game_esrb_rating.Game_esrb_rating(
                    id = 56, 
                    slug = 'everyone', 
                    name = 'Everyone', ), 
                platforms = [
                    rawg.models.game_platforms_inner.Game_platforms_inner(
                        platform = rawg.models.game_platforms_inner_platform.Game_platforms_inner_platform(
                            id = 56, 
                            slug = '', 
                            name = '', ), 
                        released_at = '', 
                        requirements = rawg.models.game_platforms_inner_requirements.Game_platforms_inner_requirements(
                            minimum = '', 
                            recommended = '', ), )
                    ]
            )
        else :
            return Game(
                rating = 1.337,
        )

    def testGame(self):
        """Test Game"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
