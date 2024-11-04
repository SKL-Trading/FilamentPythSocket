# Filament API Socket Connection Python

This is still a work in progress, so please use with caution! It is intended as a starting point for those wanting to use a Python-based trading engine to interact with Filament at a basic level.


## Features

- **WebSocket Connection with Authentication**: Connect to the exchange's WebSocket and authenticate.
- **Public and Private Data Subscription**: Subscribe to data streams (e.g., order book, live feed) for monitoring real-time updates.
- **REST API Integration**: Make REST API requests to public and private endpoints:
  - Retrieve bid/ask prices.
  - Place and cancel batch orders.
- **Heartbeat and Reconnect Mechanism**: Maintain an active connection and handle automatic reconnections if the connection is lost.

## Requirements

- Python 3.x
- Libraries: Refer to `requirements.txt` for the necessary Python packages.

## Setup and Usage

1. **Install Required Libraries**  
   Run the following command to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Constants**  
   Update `constants.py` with the necessary API keys, URLs, and account details. Ensure the WebSocket URL and API base URL are correct for your exchange environment.

3. **Run the Script**  
   Execute the `main.py` script to initialize the WebSocket connection, subscribe to channels, and perform order operations:
   ```bash
   python main.py
   ```

## Project Structure

- **`main.py`**: Manages the WebSocket connection and demonstrates sample operations using the REST API.
- **`filament_stomp_socket.py`**: Contains WebSocket connection setup and listener configuration.
- **`filament_api.py`**: Defines REST API functions for retrieving the order book, submitting orders, and handling order signatures.
- **`constants.py`**: Stores configuration details like API base URLs, account information, and WebSocket URLs.
- **`utils.py`**: Utility functions, including WebSocket URL processing.

## Example Workflow

1. **Connect to WebSocket**  
   The script authenticates and subscribes to a data stream (e.g., BTC order book).

2. **Fetch Order Book**  
   Fetch the current order book data via REST API.

3. **Submit and Cancel Orders**  
   Place batch limit orders via REST API. The script waits for a defined period before canceling the orders.

4. **Heartbeat Check**  
   The script sends periodic "ping" messages to maintain a live WebSocket connection and automatically reconnects if the connection fails.

## Key Functionalities

- **Order Book Streaming**  
  Subscribes to and prints real-time order book updates.

- **Batch Order Submission and Cancellation**  
  Places and cancels batch orders through the REST API to demonstrate interaction with private endpoints.

- **Connection Handling**  
  Pings the WebSocket server to check connection status and reconnects if needed.

## Files and Directories

```plaintext
/workspaces/FilamentPythSocket/
└── filament-api-socket-connection-master
    ├── __pycache__/
    ├── .gitignore
    ├── constants.py
    ├── filament_api.py
    ├── filament_stomp_socket.py
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── utils.py
```

## Additional Notes

- **Customization**: Modify parameters in `constants.py` to adjust order size, leverage, and other settings.
- **Testing**: This script is intended for testing and demonstration purposes. It does not handle live funds or trading accounts.
