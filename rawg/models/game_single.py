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


class GameSingle(object):
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
        'slug': 'str',
        'name': 'str',
        'name_original': 'str',
        'description': 'str',
        'metacritic': 'int',
        'metacritic_platforms': 'list[GamePlatformMetacritic]',
        'released': 'date',
        'tba': 'bool',
        'updated': 'datetime',
        'background_image': 'str',
        'background_image_additional': 'str',
        'website': 'str',
        'rating': 'float',
        'rating_top': 'int',
        'ratings': 'object',
        'reactions': 'object',
        'added': 'int',
        'added_by_status': 'object',
        'playtime': 'int',
        'screenshots_count': 'int',
        'movies_count': 'int',
        'creators_count': 'int',
        'achievements_count': 'int',
        'parent_achievements_count': 'str',
        'reddit_url': 'str',
        'reddit_name': 'str',
        'reddit_description': 'str',
        'reddit_logo': 'str',
        'reddit_count': 'int',
        'twitch_count': 'str',
        'youtube_count': 'str',
        'reviews_text_count': 'str',
        'ratings_count': 'int',
        'suggestions_count': 'int',
        'alternative_names': 'list[str]',
        'metacritic_url': 'str',
        'parents_count': 'int',
        'additions_count': 'int',
        'game_series_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'slug': 'slug',
        'name': 'name',
        'name_original': 'name_original',
        'description': 'description',
        'metacritic': 'metacritic',
        'metacritic_platforms': 'metacritic_platforms',
        'released': 'released',
        'tba': 'tba',
        'updated': 'updated',
        'background_image': 'background_image',
        'background_image_additional': 'background_image_additional',
        'website': 'website',
        'rating': 'rating',
        'rating_top': 'rating_top',
        'ratings': 'ratings',
        'reactions': 'reactions',
        'added': 'added',
        'added_by_status': 'added_by_status',
        'playtime': 'playtime',
        'screenshots_count': 'screenshots_count',
        'movies_count': 'movies_count',
        'creators_count': 'creators_count',
        'achievements_count': 'achievements_count',
        'parent_achievements_count': 'parent_achievements_count',
        'reddit_url': 'reddit_url',
        'reddit_name': 'reddit_name',
        'reddit_description': 'reddit_description',
        'reddit_logo': 'reddit_logo',
        'reddit_count': 'reddit_count',
        'twitch_count': 'twitch_count',
        'youtube_count': 'youtube_count',
        'reviews_text_count': 'reviews_text_count',
        'ratings_count': 'ratings_count',
        'suggestions_count': 'suggestions_count',
        'alternative_names': 'alternative_names',
        'metacritic_url': 'metacritic_url',
        'parents_count': 'parents_count',
        'additions_count': 'additions_count',
        'game_series_count': 'game_series_count'
    }

    def __init__(self, id=None, slug=None, name=None, name_original=None, description=None, metacritic=None, metacritic_platforms=None, released=None, tba=None, updated=None, background_image=None, background_image_additional=None, website=None, rating=None, rating_top=None, ratings=None, reactions=None, added=None, added_by_status=None, playtime=None, screenshots_count=None, movies_count=None, creators_count=None, achievements_count=None, parent_achievements_count=None, reddit_url=None, reddit_name=None, reddit_description=None, reddit_logo=None, reddit_count=None, twitch_count=None, youtube_count=None, reviews_text_count=None, ratings_count=None, suggestions_count=None, alternative_names=None, metacritic_url=None, parents_count=None, additions_count=None, game_series_count=None, local_vars_configuration=None):  # noqa: E501
        """GameSingle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._slug = None
        self._name = None
        self._name_original = None
        self._description = None
        self._metacritic = None
        self._metacritic_platforms = None
        self._released = None
        self._tba = None
        self._updated = None
        self._background_image = None
        self._background_image_additional = None
        self._website = None
        self._rating = None
        self._rating_top = None
        self._ratings = None
        self._reactions = None
        self._added = None
        self._added_by_status = None
        self._playtime = None
        self._screenshots_count = None
        self._movies_count = None
        self._creators_count = None
        self._achievements_count = None
        self._parent_achievements_count = None
        self._reddit_url = None
        self._reddit_name = None
        self._reddit_description = None
        self._reddit_logo = None
        self._reddit_count = None
        self._twitch_count = None
        self._youtube_count = None
        self._reviews_text_count = None
        self._ratings_count = None
        self._suggestions_count = None
        self._alternative_names = None
        self._metacritic_url = None
        self._parents_count = None
        self._additions_count = None
        self._game_series_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        if name is not None:
            self.name = name
        if name_original is not None:
            self.name_original = name_original
        if description is not None:
            self.description = description
        if metacritic is not None:
            self.metacritic = metacritic
        if metacritic_platforms is not None:
            self.metacritic_platforms = metacritic_platforms
        if released is not None:
            self.released = released
        if tba is not None:
            self.tba = tba
        if updated is not None:
            self.updated = updated
        if background_image is not None:
            self.background_image = background_image
        if background_image_additional is not None:
            self.background_image_additional = background_image_additional
        if website is not None:
            self.website = website
        self.rating = rating
        if rating_top is not None:
            self.rating_top = rating_top
        if ratings is not None:
            self.ratings = ratings
        if reactions is not None:
            self.reactions = reactions
        if added is not None:
            self.added = added
        if added_by_status is not None:
            self.added_by_status = added_by_status
        if playtime is not None:
            self.playtime = playtime
        if screenshots_count is not None:
            self.screenshots_count = screenshots_count
        if movies_count is not None:
            self.movies_count = movies_count
        if creators_count is not None:
            self.creators_count = creators_count
        if achievements_count is not None:
            self.achievements_count = achievements_count
        if parent_achievements_count is not None:
            self.parent_achievements_count = parent_achievements_count
        if reddit_url is not None:
            self.reddit_url = reddit_url
        if reddit_name is not None:
            self.reddit_name = reddit_name
        if reddit_description is not None:
            self.reddit_description = reddit_description
        if reddit_logo is not None:
            self.reddit_logo = reddit_logo
        if reddit_count is not None:
            self.reddit_count = reddit_count
        if twitch_count is not None:
            self.twitch_count = twitch_count
        if youtube_count is not None:
            self.youtube_count = youtube_count
        if reviews_text_count is not None:
            self.reviews_text_count = reviews_text_count
        if ratings_count is not None:
            self.ratings_count = ratings_count
        if suggestions_count is not None:
            self.suggestions_count = suggestions_count
        if alternative_names is not None:
            self.alternative_names = alternative_names
        if metacritic_url is not None:
            self.metacritic_url = metacritic_url
        if parents_count is not None:
            self.parents_count = parents_count
        if additions_count is not None:
            self.additions_count = additions_count
        if game_series_count is not None:
            self.game_series_count = game_series_count

    @property
    def id(self):
        """Gets the id of this GameSingle.  # noqa: E501


        :return: The id of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GameSingle.


        :param id: The id of this GameSingle.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this GameSingle.  # noqa: E501


        :return: The slug of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GameSingle.


        :param slug: The slug of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and len(slug) < 1):
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug)):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this GameSingle.  # noqa: E501


        :return: The name of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GameSingle.


        :param name: The name of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def name_original(self):
        """Gets the name_original of this GameSingle.  # noqa: E501


        :return: The name_original of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._name_original

    @name_original.setter
    def name_original(self, name_original):
        """Sets the name_original of this GameSingle.


        :param name_original: The name_original of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name_original is not None and len(name_original) < 1):
            raise ValueError("Invalid value for `name_original`, length must be greater than or equal to `1`")  # noqa: E501

        self._name_original = name_original

    @property
    def description(self):
        """Gets the description of this GameSingle.  # noqa: E501


        :return: The description of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GameSingle.


        :param description: The description of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def metacritic(self):
        """Gets the metacritic of this GameSingle.  # noqa: E501


        :return: The metacritic of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._metacritic

    @metacritic.setter
    def metacritic(self, metacritic):
        """Sets the metacritic of this GameSingle.


        :param metacritic: The metacritic of this GameSingle.  # noqa: E501
        :type: int
        """

        self._metacritic = metacritic

    @property
    def metacritic_platforms(self):
        """Gets the metacritic_platforms of this GameSingle.  # noqa: E501


        :return: The metacritic_platforms of this GameSingle.  # noqa: E501
        :rtype: list[GamePlatformMetacritic]
        """
        return self._metacritic_platforms

    @metacritic_platforms.setter
    def metacritic_platforms(self, metacritic_platforms):
        """Sets the metacritic_platforms of this GameSingle.


        :param metacritic_platforms: The metacritic_platforms of this GameSingle.  # noqa: E501
        :type: list[GamePlatformMetacritic]
        """

        self._metacritic_platforms = metacritic_platforms

    @property
    def released(self):
        """Gets the released of this GameSingle.  # noqa: E501


        :return: The released of this GameSingle.  # noqa: E501
        :rtype: date
        """
        return self._released

    @released.setter
    def released(self, released):
        """Sets the released of this GameSingle.


        :param released: The released of this GameSingle.  # noqa: E501
        :type: date
        """

        self._released = released

    @property
    def tba(self):
        """Gets the tba of this GameSingle.  # noqa: E501


        :return: The tba of this GameSingle.  # noqa: E501
        :rtype: bool
        """
        return self._tba

    @tba.setter
    def tba(self, tba):
        """Sets the tba of this GameSingle.


        :param tba: The tba of this GameSingle.  # noqa: E501
        :type: bool
        """

        self._tba = tba

    @property
    def updated(self):
        """Gets the updated of this GameSingle.  # noqa: E501


        :return: The updated of this GameSingle.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GameSingle.


        :param updated: The updated of this GameSingle.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def background_image(self):
        """Gets the background_image of this GameSingle.  # noqa: E501


        :return: The background_image of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        """Sets the background_image of this GameSingle.


        :param background_image: The background_image of this GameSingle.  # noqa: E501
        :type: str
        """

        self._background_image = background_image

    @property
    def background_image_additional(self):
        """Gets the background_image_additional of this GameSingle.  # noqa: E501


        :return: The background_image_additional of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._background_image_additional

    @background_image_additional.setter
    def background_image_additional(self, background_image_additional):
        """Sets the background_image_additional of this GameSingle.


        :param background_image_additional: The background_image_additional of this GameSingle.  # noqa: E501
        :type: str
        """

        self._background_image_additional = background_image_additional

    @property
    def website(self):
        """Gets the website of this GameSingle.  # noqa: E501


        :return: The website of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this GameSingle.


        :param website: The website of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                website is not None and len(website) < 1):
            raise ValueError("Invalid value for `website`, length must be greater than or equal to `1`")  # noqa: E501

        self._website = website

    @property
    def rating(self):
        """Gets the rating of this GameSingle.  # noqa: E501


        :return: The rating of this GameSingle.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this GameSingle.


        :param rating: The rating of this GameSingle.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and rating is None:  # noqa: E501
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501

        self._rating = rating

    @property
    def rating_top(self):
        """Gets the rating_top of this GameSingle.  # noqa: E501


        :return: The rating_top of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._rating_top

    @rating_top.setter
    def rating_top(self, rating_top):
        """Sets the rating_top of this GameSingle.


        :param rating_top: The rating_top of this GameSingle.  # noqa: E501
        :type: int
        """

        self._rating_top = rating_top

    @property
    def ratings(self):
        """Gets the ratings of this GameSingle.  # noqa: E501


        :return: The ratings of this GameSingle.  # noqa: E501
        :rtype: object
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this GameSingle.


        :param ratings: The ratings of this GameSingle.  # noqa: E501
        :type: object
        """

        self._ratings = ratings

    @property
    def reactions(self):
        """Gets the reactions of this GameSingle.  # noqa: E501


        :return: The reactions of this GameSingle.  # noqa: E501
        :rtype: object
        """
        return self._reactions

    @reactions.setter
    def reactions(self, reactions):
        """Sets the reactions of this GameSingle.


        :param reactions: The reactions of this GameSingle.  # noqa: E501
        :type: object
        """

        self._reactions = reactions

    @property
    def added(self):
        """Gets the added of this GameSingle.  # noqa: E501


        :return: The added of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this GameSingle.


        :param added: The added of this GameSingle.  # noqa: E501
        :type: int
        """

        self._added = added

    @property
    def added_by_status(self):
        """Gets the added_by_status of this GameSingle.  # noqa: E501


        :return: The added_by_status of this GameSingle.  # noqa: E501
        :rtype: object
        """
        return self._added_by_status

    @added_by_status.setter
    def added_by_status(self, added_by_status):
        """Sets the added_by_status of this GameSingle.


        :param added_by_status: The added_by_status of this GameSingle.  # noqa: E501
        :type: object
        """

        self._added_by_status = added_by_status

    @property
    def playtime(self):
        """Gets the playtime of this GameSingle.  # noqa: E501

        in hours  # noqa: E501

        :return: The playtime of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._playtime

    @playtime.setter
    def playtime(self, playtime):
        """Sets the playtime of this GameSingle.

        in hours  # noqa: E501

        :param playtime: The playtime of this GameSingle.  # noqa: E501
        :type: int
        """

        self._playtime = playtime

    @property
    def screenshots_count(self):
        """Gets the screenshots_count of this GameSingle.  # noqa: E501


        :return: The screenshots_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._screenshots_count

    @screenshots_count.setter
    def screenshots_count(self, screenshots_count):
        """Sets the screenshots_count of this GameSingle.


        :param screenshots_count: The screenshots_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._screenshots_count = screenshots_count

    @property
    def movies_count(self):
        """Gets the movies_count of this GameSingle.  # noqa: E501


        :return: The movies_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._movies_count

    @movies_count.setter
    def movies_count(self, movies_count):
        """Sets the movies_count of this GameSingle.


        :param movies_count: The movies_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._movies_count = movies_count

    @property
    def creators_count(self):
        """Gets the creators_count of this GameSingle.  # noqa: E501


        :return: The creators_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._creators_count

    @creators_count.setter
    def creators_count(self, creators_count):
        """Sets the creators_count of this GameSingle.


        :param creators_count: The creators_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._creators_count = creators_count

    @property
    def achievements_count(self):
        """Gets the achievements_count of this GameSingle.  # noqa: E501


        :return: The achievements_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._achievements_count

    @achievements_count.setter
    def achievements_count(self, achievements_count):
        """Sets the achievements_count of this GameSingle.


        :param achievements_count: The achievements_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._achievements_count = achievements_count

    @property
    def parent_achievements_count(self):
        """Gets the parent_achievements_count of this GameSingle.  # noqa: E501


        :return: The parent_achievements_count of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._parent_achievements_count

    @parent_achievements_count.setter
    def parent_achievements_count(self, parent_achievements_count):
        """Sets the parent_achievements_count of this GameSingle.


        :param parent_achievements_count: The parent_achievements_count of this GameSingle.  # noqa: E501
        :type: str
        """

        self._parent_achievements_count = parent_achievements_count

    @property
    def reddit_url(self):
        """Gets the reddit_url of this GameSingle.  # noqa: E501

        For example \"https://www.reddit.com/r/uncharted/\" or \"uncharted\"  # noqa: E501

        :return: The reddit_url of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._reddit_url

    @reddit_url.setter
    def reddit_url(self, reddit_url):
        """Sets the reddit_url of this GameSingle.

        For example \"https://www.reddit.com/r/uncharted/\" or \"uncharted\"  # noqa: E501

        :param reddit_url: The reddit_url of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reddit_url is not None and len(reddit_url) < 1):
            raise ValueError("Invalid value for `reddit_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._reddit_url = reddit_url

    @property
    def reddit_name(self):
        """Gets the reddit_name of this GameSingle.  # noqa: E501


        :return: The reddit_name of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._reddit_name

    @reddit_name.setter
    def reddit_name(self, reddit_name):
        """Sets the reddit_name of this GameSingle.


        :param reddit_name: The reddit_name of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reddit_name is not None and len(reddit_name) < 1):
            raise ValueError("Invalid value for `reddit_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._reddit_name = reddit_name

    @property
    def reddit_description(self):
        """Gets the reddit_description of this GameSingle.  # noqa: E501


        :return: The reddit_description of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._reddit_description

    @reddit_description.setter
    def reddit_description(self, reddit_description):
        """Sets the reddit_description of this GameSingle.


        :param reddit_description: The reddit_description of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reddit_description is not None and len(reddit_description) < 1):
            raise ValueError("Invalid value for `reddit_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._reddit_description = reddit_description

    @property
    def reddit_logo(self):
        """Gets the reddit_logo of this GameSingle.  # noqa: E501


        :return: The reddit_logo of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._reddit_logo

    @reddit_logo.setter
    def reddit_logo(self, reddit_logo):
        """Sets the reddit_logo of this GameSingle.


        :param reddit_logo: The reddit_logo of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reddit_logo is not None and len(reddit_logo) < 1):
            raise ValueError("Invalid value for `reddit_logo`, length must be greater than or equal to `1`")  # noqa: E501

        self._reddit_logo = reddit_logo

    @property
    def reddit_count(self):
        """Gets the reddit_count of this GameSingle.  # noqa: E501


        :return: The reddit_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._reddit_count

    @reddit_count.setter
    def reddit_count(self, reddit_count):
        """Sets the reddit_count of this GameSingle.


        :param reddit_count: The reddit_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._reddit_count = reddit_count

    @property
    def twitch_count(self):
        """Gets the twitch_count of this GameSingle.  # noqa: E501


        :return: The twitch_count of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._twitch_count

    @twitch_count.setter
    def twitch_count(self, twitch_count):
        """Sets the twitch_count of this GameSingle.


        :param twitch_count: The twitch_count of this GameSingle.  # noqa: E501
        :type: str
        """

        self._twitch_count = twitch_count

    @property
    def youtube_count(self):
        """Gets the youtube_count of this GameSingle.  # noqa: E501


        :return: The youtube_count of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._youtube_count

    @youtube_count.setter
    def youtube_count(self, youtube_count):
        """Sets the youtube_count of this GameSingle.


        :param youtube_count: The youtube_count of this GameSingle.  # noqa: E501
        :type: str
        """

        self._youtube_count = youtube_count

    @property
    def reviews_text_count(self):
        """Gets the reviews_text_count of this GameSingle.  # noqa: E501


        :return: The reviews_text_count of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._reviews_text_count

    @reviews_text_count.setter
    def reviews_text_count(self, reviews_text_count):
        """Sets the reviews_text_count of this GameSingle.


        :param reviews_text_count: The reviews_text_count of this GameSingle.  # noqa: E501
        :type: str
        """

        self._reviews_text_count = reviews_text_count

    @property
    def ratings_count(self):
        """Gets the ratings_count of this GameSingle.  # noqa: E501


        :return: The ratings_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._ratings_count

    @ratings_count.setter
    def ratings_count(self, ratings_count):
        """Sets the ratings_count of this GameSingle.


        :param ratings_count: The ratings_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._ratings_count = ratings_count

    @property
    def suggestions_count(self):
        """Gets the suggestions_count of this GameSingle.  # noqa: E501


        :return: The suggestions_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._suggestions_count

    @suggestions_count.setter
    def suggestions_count(self, suggestions_count):
        """Sets the suggestions_count of this GameSingle.


        :param suggestions_count: The suggestions_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._suggestions_count = suggestions_count

    @property
    def alternative_names(self):
        """Gets the alternative_names of this GameSingle.  # noqa: E501


        :return: The alternative_names of this GameSingle.  # noqa: E501
        :rtype: list[str]
        """
        return self._alternative_names

    @alternative_names.setter
    def alternative_names(self, alternative_names):
        """Sets the alternative_names of this GameSingle.


        :param alternative_names: The alternative_names of this GameSingle.  # noqa: E501
        :type: list[str]
        """

        self._alternative_names = alternative_names

    @property
    def metacritic_url(self):
        """Gets the metacritic_url of this GameSingle.  # noqa: E501

        For example \"http://www.metacritic.com/game/playstation-4/the-witcher-3-wild-hunt\"  # noqa: E501

        :return: The metacritic_url of this GameSingle.  # noqa: E501
        :rtype: str
        """
        return self._metacritic_url

    @metacritic_url.setter
    def metacritic_url(self, metacritic_url):
        """Sets the metacritic_url of this GameSingle.

        For example \"http://www.metacritic.com/game/playstation-4/the-witcher-3-wild-hunt\"  # noqa: E501

        :param metacritic_url: The metacritic_url of this GameSingle.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                metacritic_url is not None and len(metacritic_url) < 1):
            raise ValueError("Invalid value for `metacritic_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._metacritic_url = metacritic_url

    @property
    def parents_count(self):
        """Gets the parents_count of this GameSingle.  # noqa: E501


        :return: The parents_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._parents_count

    @parents_count.setter
    def parents_count(self, parents_count):
        """Sets the parents_count of this GameSingle.


        :param parents_count: The parents_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._parents_count = parents_count

    @property
    def additions_count(self):
        """Gets the additions_count of this GameSingle.  # noqa: E501


        :return: The additions_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._additions_count

    @additions_count.setter
    def additions_count(self, additions_count):
        """Sets the additions_count of this GameSingle.


        :param additions_count: The additions_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._additions_count = additions_count

    @property
    def game_series_count(self):
        """Gets the game_series_count of this GameSingle.  # noqa: E501


        :return: The game_series_count of this GameSingle.  # noqa: E501
        :rtype: int
        """
        return self._game_series_count

    @game_series_count.setter
    def game_series_count(self, game_series_count):
        """Sets the game_series_count of this GameSingle.


        :param game_series_count: The game_series_count of this GameSingle.  # noqa: E501
        :type: int
        """

        self._game_series_count = game_series_count

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
        if not isinstance(other, GameSingle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GameSingle):
            return True

        return self.to_dict() != other.to_dict()