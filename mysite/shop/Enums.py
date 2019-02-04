from enum import Enum


class Order_state(Enum):
    DRAFT = "Draft"
    PUBLISHED = "Published"
    REOPEN = "Reopen"


class Product_transportation_class(Enum):
    EXPRESS = "Express Post"
    NORMAL = "Normal Post"
    TIEPAKS = "Tiepaks Post"


class Product_types(Enum):
    DOWNLOAD = "Download"
    POSTAL = "Postal"


class Product_In_Stock(Enum):
    AVAILABLE = 'Available'
    UNAVAILABLE = 'Unavailable'
    PREBUY = "In Prebuy"
