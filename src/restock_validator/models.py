"""A Pydantic v2 model named RestockItem with these fields:

sku: str
warehouse: str
quantity: int — must be greater than 0 (reject zero and negative values)
unit_cost: float — must be greater than 0
category: Literal["electronics", "perishable", "apparel", "hardware"]
"""
from typing import Literal
from pydantic import BaseModel, Field

Category = Literal["electronics", "perishable", "apparel", "hardware"]

class RestockItem(BaseModel):

    sku: str
    warehouse: str
    quantity: int = Field(gt=0)
    unit_cost: float = Field(gt=0)
    category: Category

