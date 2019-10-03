from datetime import date
from typing import Any, List, Optional

from pydantic import BaseModel, Extra
from pydantic.color import Color


class RawgBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        extra = Extra.allow
        validate_all = True
        validate_assignment = True
        use_enum_values = True


class RawgPlatformDataBase(RawgBase):
    id: int
    name: str
    slug: str


class RawgPlatformData(RawgPlatformDataBase):
    games_count: int

    # Optional fields
    image: Optional[str]
    image_background: Optional[str]
    year_end: Optional[date]
    year_start: Optional[date]


class RawgPlatformBase(RawgBase):
    platform: RawgPlatformDataBase


class RawgPlatform(RawgPlatformBase):
    platform: RawgPlatformData

    # Optional fields
    requirements: Optional[dict]
    released_at: Optional[date]


class RawgStoreDataBase(RawgBase):
    id: int
    name: str
    slug: str


class RawgStoreData(RawgStoreDataBase):
    domain: str
    games_count: int
    image_background: str


class RawgStoreBase(RawgBase):
    store: RawgStoreDataBase


class RawgStore(RawgStoreBase):
    store: RawgStoreData
    id: int
    url: str


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


class RawgChartGenre(RawgBase):
    name: str
    change: str
    position: int


class RawgCharts(RawgBase):
    full: Optional[int]
    genre: Optional[RawgChartGenre]
    person: Optional[dict]
    released: Optional[RawgChartYear]
    toplay: Optional[int]
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


class RawgGenreBase(RawgBase):
    id: int
    name: str
    slug: str


class RawgGenre(RawgGenreBase):
    games_count: int
    image_background: str


class RawgGameBase(RawgBase):
    added: int
    charts: Optional[RawgCharts]
    comments_count: int
    comments_parent_count: int
    dominant_color: Color
    genres: List[RawgGenreBase]
    id: int
    name: str
    playtime: int
    promo: str
    rating: float
    rating_top: int
    ratings: List[RawgRating]
    ratings_count: int
    reviews_count: int
    reviews_text_count: int
    saturated_color: Color
    slug: str
    suggestions_count: int
    tba: bool

    # Optional fields
    added_by_status: Optional[RawgAddedByStatus]
    background_image: Optional[str]
    community_rating: Optional[int]
    metacritic: Optional[int]
    parent_platforms: Optional[List[RawgPlatformBase]]
    platforms: Optional[List[RawgPlatformBase]]
    released: Optional[date]
    stores: Optional[List[RawgStoreBase]]

    # Unused fields
    user_game: Any


class RawgGameSearch(RawgGameBase):
    score: str
    short_screenshots: List[RawgScreenshot]

    # Optional fields
    clip: Optional[RawgClip]


class RawgGameSuggested(RawgGameBase):
    short_screenshots: List[RawgScreenshot]

    # Optional fields
    clip: Optional[RawgClip]


class RawgGame(RawgGameBase):
    achievements_count: int
    collections_count: int
    description: str
    description_is_protected: bool
    description_raw: str
    developers: list
    discussions_count: int
    events_count: int
    genres: List[RawgGenre]
    imgur_count: int
    metacritic_url: str
    movies_count: int
    parent_achievements_count: int
    persons_count: int
    platforms: List[RawgPlatform]
    publishers: list
    reddit_count: int
    reddit_description: str
    reddit_logo: str
    reddit_name: str
    reddit_url: str
    screenshots_count: int
    stores: List[RawgStore]
    tags: list
    twitch_count: int
    updated: str
    website: str
    youtube_count: int

    # Optional fields
    alternative_names: Optional[list]
    background_image_additional: Optional[str]
    esrb_rating: Optional[dict]
    reactions: Optional[dict]
    redirect: Optional[str]

    seo_description: Optional[str]
    seo_descriptions: Optional[dict]
    seo_h1: Optional[str]
    seo_title: Optional[str]


class RawgSearch(RawgBase):
    count: int
    results: List[RawgGameSearch]

    # Optional fields
    next: Optional[str]
    previous: Optional[str]


class RawgSuggested(RawgBase):
    count: int
    results: List[RawgGameSuggested]

    updated: str
    seo_text: str

    # Optional fields
    next: Optional[str]
    previous: Optional[str]

    seo_title: Optional[str]
    seo_description: Optional[str]
    seo_h1: Optional[str]
    seo_descriptions: Optional[dict]
