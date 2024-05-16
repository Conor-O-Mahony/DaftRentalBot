class DaftRentalBotCityString(Exception):
    """city_name should be of type str."""

class DaftRentalBotRadiusString(Exception):
    """radius should be of type str."""

class DaftRentalBotCityStr(Exception):
    """city_name should be of type String."""

class DaftRentalBotInvalidCity(Exception):
    """city_name should be a part of available_cities"""

class DaftRentalBotInvalidRadius(Exception):
    """radius should be a part of available_radius"""

class DaftRentalBotFacilitiesList(Exception):
    """facilities should be of type List."""


class DaftRentalBotFacilitiesStr(Exception):
    """Each item inside facilities should be of type String."""


class DaftRentalBotInvalidFacilities(Exception):
    """Each item inside facilities shold be a part of available_facilities"""


class DaftRentalBotLoginError(Exception):
    """Incorrect username or password. Please try again."""
