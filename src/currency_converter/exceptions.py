from src.currency_converter.constants import ErrorCode
from src.exceptions import BadRequest


class BadExchangerateRequest(BadRequest):
    DETAIL = ErrorCode.BAD_EXCHANGERATE_REQUEST
