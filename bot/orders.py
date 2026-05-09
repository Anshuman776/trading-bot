from binance.exceptions import BinanceAPIException
from bot.logging_config import logger
import time

def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        payload = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":
            payload["price"] = price
            payload["timeInForce"] = "GTC"

        logger.info(f"Order Request: {payload}")

        # Place order
        response = client.futures_create_order(**payload)

        logger.info(f"Initial Response: {response}")

        # Wait for Binance to process order
        time.sleep(2)

        # Fetch updated order details
        updated_order = client.futures_get_order(
            symbol=symbol.upper(),
            orderId=response["orderId"]
        )

        logger.info(f"Updated Response: {updated_order}")

        return updated_order

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise