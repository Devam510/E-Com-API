from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderBase(BaseModel):
    shipping_address: Dict[str, Any]

class OrderCreate(OrderBase):
    items: List[OrderItem]

class OrderResponse(OrderBase):
    id: int
    user_id: int
    total_amount: float
    status: str
    items: List[Dict[str, Any]]
    created_at: datetime

    class Config:
        from_attributes = True