from typing import Callable, get_type_hints

import pytest

from gmt.resources.accounts import AccountsResource, AsyncAccountsResource
from gmt.resources.purchases.bulk import AsyncBulkResource, BulkResource
from gmt.resources.purchases.purchases import AsyncPurchasesResource, PurchasesResource


@pytest.mark.parametrize(
    "method",
    (
        AccountsResource.list,
        AsyncAccountsResource.list,
        PurchasesResource.list,
        AsyncPurchasesResource.list,
        BulkResource.download,
        AsyncBulkResource.download,
    ),
    ids=lambda method: method.__qualname__,
)
def test_public_list_and_download_annotations_are_readable(method: Callable[..., object]) -> None:
    assert "return" in get_type_hints(method)
