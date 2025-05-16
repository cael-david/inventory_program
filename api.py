import json
from stock_controller import StockController

class Api:
    def __init__(self):
        self.window = None
        self.ctrl = StockController()
        self.current_stock_id = None
    
    
    