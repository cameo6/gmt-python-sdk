from typing import List, Literal, Optional, Union

from ..._models import BaseModel
from ..purchase_list_response import Price, PurchaseListResponse

PurchaseStatus = Literal["PENDING", "SUCCESS", "ERROR", "REFUND", "EXPIRED"]
PurchaseSort = Literal["date_asc", "date_desc"]


class PurchasePageMeta(BaseModel):
    current_page: int
    page_size: int
    total_items: int
    total_pages: int
    has_next: bool
    has_previous: bool


class BulkListItem(BaseModel):
    bulk_purchase_id: int
    country_code: str
    quantity: int
    status: PurchaseStatus
    created_at: str
    refunded_quantity: int
    total_price: Price


class BulkListResponse(BaseModel):
    items: List[BulkListItem]
    pagination: PurchasePageMeta


class HistoryPurchase(PurchaseListResponse):
    kind: Literal["purchase"]


class HistoryBulk(BaseModel):
    kind: Literal["bulk"]
    id: int
    country_code: str
    status: PurchaseStatus
    created_at: str
    refunded_quantity: int
    quantity: int
    price: Optional[Price] = ...


class PurchaseHistoryResponse(BaseModel):
    items: List[Union[HistoryPurchase, HistoryBulk]]
    pagination: PurchasePageMeta
