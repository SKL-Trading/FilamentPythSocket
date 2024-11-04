# Constants for API
API_BASE_URL = "https://orderbook.filament.finance/sei"
EXCHANGE_URL = f"{API_BASE_URL}/filament/api/v1/exchange"

BEARER_TOKEN = ""  # Use your token
SIGNING_KEY = "
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json",
}
INDEX_TOKEN = "BTC"  # BTC Index Token as example
ACOUNT = ""

NUM_ORDERS = 5

# WebSocket URLs
WEB_SOCKET_URL = (
    "https://orderbook.filament.finance/sei/api/order-book/orderbook-websocket"
)
