from deriv.client import DerivClient
from deriv.strategy import basic_candle_strategy

if __name__ == "__main__":
    client = DerivClient(strategy_callback=basic_candle_strategy)
    client.connect()
