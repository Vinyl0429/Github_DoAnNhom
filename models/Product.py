from enum import Enum

class Size(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"

class SugarLevel(Enum):
    NONE = "0%"
    LOW = "30%"
    MEDIUM = "50%"
    HIGH = "70%"
    FULL = "100%"

class IceLevel(Enum):
    NONE = "0%"
    LOW = "30%"
    MEDIUM = "50%"
    HIGH = "70%"
    FULL = "100%"

class Product:
    def __init__(self, id, name, category, price, quantity, image,
                 description="", sizes=None, sugar_levels=None, ice_levels=None):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.image = image
        self.description = description

        # Lưu danh sách size, đường, đá
        self.sizes = sizes if sizes else []
        self.sugar_levels = sugar_levels if sugar_levels else []
        self.ice_levels = ice_levels if ice_levels else []

    def __str__(self):
        return (f"ID: {self.id} | Name: {self.name} | Category: {self.category} | "
                f"Price: {self.price} VND | Quantity: {self.quantity} | Image: {self.image} | "
                f"Description: {self.description} | Sizes: {', '.join(self.sizes) if self.sizes else 'N/A'} | "
                f"Sugar Levels: {', '.join(self.sugar_levels) if self.sugar_levels else 'N/A'} | "
                f"Ice Levels: {', '.join(self.ice_levels) if self.ice_levels else 'N/A'}")
