from datetime import date
from typing import Any, List, Optional

from pydantic import BaseModel
from pydantic.color import Color

__all__ = (
    'RawgPlatformData',
    'RawgPlatform',
    'RawgStoreData',
    'RawgStore',
    'RawgRating',
    'RawgAddedByStatus',
    'RawgChartYear',
    'RawgCharts',
    'RawgClips',
    'RawgClip',
    'RawgScreenshot',
    'RawgGenre',
    'RawgGame',
    'RawgSearch',
)


class RawgBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True
        use_enum_values = True


class RawgPlatformData(RawgBase):
    id: int
    name: str
    slug: str


class RawgPlatform(RawgBase):
    platform: RawgPlatformData


class RawgStoreData(RawgBase):
    id: int
    name: str
    slug: str


class RawgStore(RawgBase):
    store: RawgStoreData


class RawgRating(RawgBase):
    id: int
    title: str
    count: int
    percent: float


class RawgAddedByStatus(RawgBase):
    yet: int = 0
    owned: int = 0
    beaten: int = 0
    toplay: int = 0
    dropped: int = 0
    playing: int = 0


class RawgChartYear(RawgBase):
    year: int
    change: str
    position: int


class RawgCharts(RawgBase):
    year: Optional[RawgChartYear]


class RawgClips(RawgBase):
    p320: str
    p640: str
    full: str

    class Config:
        fields = {
            'p320': {'alias': '320'},
            'p640': {'alias': '640'},
        }


class RawgClip(RawgBase):
    clip: str
    clips: RawgClips
    preview: str


class RawgScreenshot(RawgBase):
    id: int
    image: str


class RawgGenre(RawgBase):
    id: int
    name: str
    slug: str


class RawgGameBase(RawgBase):
    slug: str
    name: str
    promo: str
    playtime: int
    platforms: Optional[List[RawgPlatform]]
    stores: Optional[List[RawgStore]]
    released: Optional[date]
    tba: bool
    background_image: Optional[str]
    rating: float
    rating_top: int
    ratings: List[RawgRating]
    ratings_count: int
    reviews_text_count: int
    added: int
    added_by_status: Optional[RawgAddedByStatus]
    metacritic: Optional[int]
    charts: RawgCharts
    comments_count: int
    comments_parent_count: int
    suggestions_count: int
    id: int
    user_game: Any  # Unused
    reviews_count: int
    saturated_color: Color
    dominant_color: Color
    parent_platforms: Optional[List[RawgPlatform]]
    genres: List[RawgGenre]


class RawgGameSearch(RawgGameBase):
    clip: Optional[RawgClip]
    score: str
    short_screenshots: List[RawgScreenshot]


class RawgGame(RawgGameBase):
    background_image_additional: str
    description_raw: str
    description_is_protected: bool
    events_count: int
    collections_count: int
    movies_count: int
    developers: list
    reddit_name: str
    esrb_rating: dict
    seo_title: str
    reddit_count: int
    tags: list
    reddit_description: str
    persons_count: int
    seo_h1: str
    imgur_count: int
    seo_description: str
    reddit_url: str
    youtube_count: int
    updated: str
    publishers: list
    achievements_count: int
    metacritic_url: str
    seo_descriptions: dict
    website: str
    parent_achievements_count: int
    twitch_count: int
    description: str
    reddit_logo: str
    alternative_names: list
    screenshots_count: int
    reactions: dict
    discussions_count: int


class RawgSearch(RawgBase):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[RawgGameSearch]
