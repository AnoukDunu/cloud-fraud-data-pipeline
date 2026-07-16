# This file it so generate random data to simulates real-world scenarios
import pandas as pd
import random
from datetime import datetime

def generate_transations(n=10000):
    data = []

    for _ in range(n):
        data.append({
            "transaction_id": str(random.randint(100000, 999999)),
            "user_id": str(random.randint(1, 1000)),
            "amount": float(random.uniform(10,1000), 2),
            "location": random.choice(["AU", "US", "UK", "IN"]),
            "timestamp": datetime.now()
        })

    return pd.DataFrame(data)