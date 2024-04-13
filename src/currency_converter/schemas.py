from pydantic import BaseModel, ConfigDict, Field


class ConverterSchema(BaseModel):
    from_currency: str = Field(alias="from", min_length=3, max_length=3)
    to_currency: str = Field(alias="to", min_length=3, max_length=3)
    value: int

    model_config = ConfigDict(populate_by_name=True)


class ConverterResultSchema(BaseModel):
    result: float
