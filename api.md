# Service

Types:

```python
from gmt.types import ServiceGetServerTimeResponse, ServiceHealthCheckResponse
```

Methods:

- <code title="get /v1/service/time">client.service.<a href="./src/gmt/resources/service.py">get_server_time</a>() -> <a href="./src/gmt/types/service_get_server_time_response.py">ServiceGetServerTimeResponse</a></code>
- <code title="get /v1/service/health">client.service.<a href="./src/gmt/resources/service.py">health_check</a>() -> <a href="./src/gmt/types/service_health_check_response.py">ServiceHealthCheckResponse</a></code>

# Accounts

Types:

```python
from gmt.types import AccountRetrieveResponse, AccountListResponse, AccountListCountriesResponse
```

Methods:

- <code title="get /v1/accounts/{country_code}">client.accounts.<a href="./src/gmt/resources/accounts.py">retrieve</a>(country_code) -> <a href="./src/gmt/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /v1/accounts/">client.accounts.<a href="./src/gmt/resources/accounts.py">list</a>(\*\*<a href="src/gmt/types/account_list_params.py">params</a>) -> <a href="./src/gmt/types/account_list_response.py">SyncPageNumber[AccountListResponse]</a></code>
- <code title="get /v1/accounts/countries">client.accounts.<a href="./src/gmt/resources/accounts.py">list_countries</a>(\*\*<a href="src/gmt/types/account_list_countries_params.py">params</a>) -> <a href="./src/gmt/types/account_list_countries_response.py">SyncPageNumber[AccountListCountriesResponse]</a></code>

# Profile

Types:

```python
from gmt.types import (
    ProfileRetrieveResponse,
    ProfileChangeLanguageResponse,
    ProfileChangeLoginResponse,
    ProfileChangePasswordResponse,
    ProfileUnbindTelegramResponse,
)
```

Methods:

- <code title="get /v1/profile/">client.profile.<a href="./src/gmt/resources/profile/profile.py">retrieve</a>() -> <a href="./src/gmt/types/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="patch /v1/profile/language">client.profile.<a href="./src/gmt/resources/profile/profile.py">change_language</a>(\*\*<a href="src/gmt/types/profile_change_language_params.py">params</a>) -> <a href="./src/gmt/types/profile_change_language_response.py">ProfileChangeLanguageResponse</a></code>
- <code title="patch /v1/profile/change-login">client.profile.<a href="./src/gmt/resources/profile/profile.py">change_login</a>(\*\*<a href="src/gmt/types/profile_change_login_params.py">params</a>) -> <a href="./src/gmt/types/profile_change_login_response.py">ProfileChangeLoginResponse</a></code>
- <code title="patch /v1/profile/change-password">client.profile.<a href="./src/gmt/resources/profile/profile.py">change_password</a>(\*\*<a href="src/gmt/types/profile_change_password_params.py">params</a>) -> <a href="./src/gmt/types/profile_change_password_response.py">ProfileChangePasswordResponse</a></code>
- <code title="patch /v1/profile/unbind-telegram">client.profile.<a href="./src/gmt/resources/profile/profile.py">unbind_telegram</a>() -> <a href="./src/gmt/types/profile_unbind_telegram_response.py">ProfileUnbindTelegramResponse</a></code>

## Discount

Types:

```python
from gmt.types.profile import DiscountRetrieveResponse
```

Methods:

- <code title="get /v1/profile/discount">client.profile.discount.<a href="./src/gmt/resources/profile/discount.py">retrieve</a>() -> <a href="./src/gmt/types/profile/discount_retrieve_response.py">DiscountRetrieveResponse</a></code>

## Referral

Types:

```python
from gmt.types.profile import ReferralRetrieveResponse, ReferralTransferBalanceResponse
```

Methods:

- <code title="get /v1/profile/referral">client.profile.referral.<a href="./src/gmt/resources/profile/referral/referral.py">retrieve</a>() -> <a href="./src/gmt/types/profile/referral_retrieve_response.py">ReferralRetrieveResponse</a></code>
- <code title="post /v1/profile/referral/transfer-balance">client.profile.referral.<a href="./src/gmt/resources/profile/referral/referral.py">transfer_balance</a>(\*\*<a href="src/gmt/types/profile/referral_transfer_balance_params.py">params</a>) -> <a href="./src/gmt/types/profile/referral_transfer_balance_response.py">ReferralTransferBalanceResponse</a></code>

### Transaction

Types:

```python
from gmt.types.profile.referral import TransactionListResponse
```

Methods:

- <code title="get /v1/profile/referral/transaction">client.profile.referral.transaction.<a href="./src/gmt/resources/profile/referral/transaction.py">list</a>(\*\*<a href="src/gmt/types/profile/referral/transaction_list_params.py">params</a>) -> <a href="./src/gmt/types/profile/referral/transaction_list_response.py">SyncPageNumber[TransactionListResponse]</a></code>

# Purchases

Types:

```python
from gmt.types import (
    PurchaseCreateResponse,
    PurchaseRetrieveResponse,
    PurchaseListResponse,
    PurchaseRefundResponse,
    PurchaseRequestVerificationCodeResponse,
)
```

Methods:

- <code title="post /v1/purchases/">client.purchases.<a href="./src/gmt/resources/purchases/purchases.py">create</a>(\*\*<a href="src/gmt/types/purchase_create_params.py">params</a>) -> <a href="./src/gmt/types/purchase_create_response.py">PurchaseCreateResponse</a></code>
- <code title="get /v1/purchases/{purchase_id}">client.purchases.<a href="./src/gmt/resources/purchases/purchases.py">retrieve</a>(purchase_id) -> <a href="./src/gmt/types/purchase_retrieve_response.py">PurchaseRetrieveResponse</a></code>
- <code title="get /v1/purchases/">client.purchases.<a href="./src/gmt/resources/purchases/purchases.py">list</a>(\*\*<a href="src/gmt/types/purchase_list_params.py">params</a>) -> <a href="./src/gmt/types/purchase_list_response.py">SyncPageNumber[PurchaseListResponse]</a></code>
- <code title="post /v1/purchases/{purchase_id}/refund">client.purchases.<a href="./src/gmt/resources/purchases/purchases.py">refund</a>(purchase_id) -> <a href="./src/gmt/types/purchase_refund_response.py">PurchaseRefundResponse</a></code>
- <code title="post /v1/purchases/{purchase_id}/request-code">client.purchases.<a href="./src/gmt/resources/purchases/purchases.py">request_verification_code</a>(purchase_id, \*\*<a href="src/gmt/types/purchase_request_verification_code_params.py">params</a>) -> <a href="./src/gmt/types/purchase_request_verification_code_response.py">PurchaseRequestVerificationCodeResponse</a></code>

## Bulk

Types:

```python
from gmt.types.purchases import BulkCreateResponse, BulkRetrieveResponse
```

Methods:

- <code title="post /v1/purchases/bulk">client.purchases.bulk.<a href="./src/gmt/resources/purchases/bulk.py">create</a>(\*\*<a href="src/gmt/types/purchases/bulk_create_params.py">params</a>) -> <a href="./src/gmt/types/purchases/bulk_create_response.py">BulkCreateResponse</a></code>
- <code title="get /v1/purchases/bulk/{purchase_id}">client.purchases.bulk.<a href="./src/gmt/resources/purchases/bulk.py">retrieve</a>(purchase_id) -> <a href="./src/gmt/types/purchases/bulk_retrieve_response.py">BulkRetrieveResponse</a></code>
- <code title="get /v1/purchases/bulk/{purchase_id}/download">client.purchases.bulk.<a href="./src/gmt/resources/purchases/bulk.py">download</a>(purchase_id) -> BinaryAPIResponse</code>

# PurchasesByHash

Types:

```python
from gmt.types import (
    PurchasesByHashRetrieveResponse,
    PurchasesByHashRequestVerificationCodeResponse,
)
```

Methods:

- <code title="get /v1/purchases-by-hash/{hash}">client.purchases_by_hash.<a href="./src/gmt/resources/purchases_by_hash.py">retrieve</a>(hash) -> <a href="./src/gmt/types/purchases_by_hash_retrieve_response.py">PurchasesByHashRetrieveResponse</a></code>
- <code title="post /v1/purchases-by-hash/{hash}/request-code">client.purchases_by_hash.<a href="./src/gmt/resources/purchases_by_hash.py">request_verification_code</a>(hash, \*\*<a href="src/gmt/types/purchases_by_hash_request_verification_code_params.py">params</a>) -> <a href="./src/gmt/types/purchases_by_hash_request_verification_code_response.py">PurchasesByHashRequestVerificationCodeResponse</a></code>

# Telegram

Types:

```python
from gmt.types import TelegramGetPremiumPriceResponse, TelegramGetStarsPriceResponse
```

Methods:

- <code title="get /v1/telegram/premium">client.telegram.<a href="./src/gmt/resources/telegram/telegram.py">get_premium_price</a>(\*\*<a href="src/gmt/types/telegram_get_premium_price_params.py">params</a>) -> <a href="./src/gmt/types/telegram_get_premium_price_response.py">TelegramGetPremiumPriceResponse</a></code>
- <code title="get /v1/telegram/stars">client.telegram.<a href="./src/gmt/resources/telegram/telegram.py">get_stars_price</a>(\*\*<a href="src/gmt/types/telegram_get_stars_price_params.py">params</a>) -> <a href="./src/gmt/types/telegram_get_stars_price_response.py">TelegramGetStarsPriceResponse</a></code>

## Purchases

Types:

```python
from gmt.types.telegram import (
    PurchaseCreatePremiumResponse,
    PurchaseCreateStarsResponse,
    PurchaseListPremiumResponse,
    PurchaseListStarsResponse,
)
```

Methods:

- <code title="post /v1/telegram/purchases/premium">client.telegram.purchases.<a href="./src/gmt/resources/telegram/purchases.py">create_premium</a>(\*\*<a href="src/gmt/types/telegram/purchase_create_premium_params.py">params</a>) -> <a href="./src/gmt/types/telegram/purchase_create_premium_response.py">PurchaseCreatePremiumResponse</a></code>
- <code title="post /v1/telegram/purchases/stars">client.telegram.purchases.<a href="./src/gmt/resources/telegram/purchases.py">create_stars</a>(\*\*<a href="src/gmt/types/telegram/purchase_create_stars_params.py">params</a>) -> <a href="./src/gmt/types/telegram/purchase_create_stars_response.py">PurchaseCreateStarsResponse</a></code>
- <code title="get /v1/telegram/purchases/premium">client.telegram.purchases.<a href="./src/gmt/resources/telegram/purchases.py">list_premium</a>(\*\*<a href="src/gmt/types/telegram/purchase_list_premium_params.py">params</a>) -> <a href="./src/gmt/types/telegram/purchase_list_premium_response.py">SyncPageNumber[PurchaseListPremiumResponse]</a></code>
- <code title="get /v1/telegram/purchases/stars">client.telegram.purchases.<a href="./src/gmt/resources/telegram/purchases.py">list_stars</a>(\*\*<a href="src/gmt/types/telegram/purchase_list_stars_params.py">params</a>) -> <a href="./src/gmt/types/telegram/purchase_list_stars_response.py">SyncPageNumber[PurchaseListStarsResponse]</a></code>

# Webhooks

Types:

```python
from gmt.types import WebhookTestResponse
```

Methods:

- <code title="post /v1/webhooks/test">client.webhooks.<a href="./src/gmt/resources/webhooks.py">test</a>(\*\*<a href="src/gmt/types/webhook_test_params.py">params</a>) -> <a href="./src/gmt/types/webhook_test_response.py">WebhookTestResponse</a></code>
