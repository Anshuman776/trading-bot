import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_order(
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.price:
            print(f"Price    : {args.price}")

        client = get_client()

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")

        print("\nOrder placed successfully!")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
