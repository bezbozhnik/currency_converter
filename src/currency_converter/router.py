from typing import Annotated

from fastapi import APIRouter, Query, status

from src.currency_converter.schemas import (ConverterResultSchema,
                                            ConverterSchema)
from src.currency_converter.service import get_currency_exchange_rate

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK, response_model=ConverterResultSchema)
async def convert_currency(from_currency: Annotated[str, Query(alias="from", min_length=3, max_length=3)],
                           to_currency: Annotated[str, Query(alias="to", min_length=3, max_length=3)],
                           value: int) -> ConverterResultSchema:
    """
    Converts currency from one type to another.

    The list of available currencies for conversion is available
    at — https://www.exchangerate-api.com/docs/supported-currencies

    Parameters:
    - **from_currency** (str): The currency code to convert from. Must be 3 characters long.
    - **to_currency** (str): The currency code to convert to. Must be 3 characters long.
    - **value** (int): The amount of the first currency.

    """
    return await get_currency_exchange_rate(
        ConverterSchema(from_currency=from_currency, to_currency=to_currency, value=value))
