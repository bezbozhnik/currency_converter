import aiohttp

from src.config import settings
from src.currency_converter.exceptions import BadExchangerateRequest
from src.currency_converter.schemas import (ConverterResultSchema,
                                            ConverterSchema)


async def get_currency_exchange_rate(data: ConverterSchema):
    url = settings.converter_service_url + data.from_currency + '/' + data.to_currency
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if result := (await response.json()).get('conversion_rate'):
                return ConverterResultSchema(result=(result * data.value))
            raise BadExchangerateRequest
