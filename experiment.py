from src.binance_historical_data import BinanceDataDumper
import os


if __name__ == "__main__":
    data_dumper = BinanceDataDumper(os.getcwd(),"spot","klines","1d")
    data_dumper.dump_data(["BTCUSDT"], date_start=None, date_end="2025-03-30", is_to_update_existing=False, int_max_tickers_to_get=None,tickers_to_exclude=["UST"])