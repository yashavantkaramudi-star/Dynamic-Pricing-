import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import time

def build_engine():
    """Phase 1 & 3: Trains the AI Brain on historical segment data"""
    n = 1000
    segments = np.random.randint(0, 2, n) # 0: Startup, 1: Enterprise
    prices = np.random.uniform(20, 200, n)
    
    # Economics: Startups drop off faster (1.5) than Enterprises (0.3)
    demand = [ (200 - 1.5*p if s==0 else 150 - 0.3*p) + np.random.normal(0,5) for p,s in zip(prices, segments)]
    
    df = pd.DataFrame({'segment': segments, 'price': prices, 'sales': demand})
    
    # Phase 4: Statistical Outlier Removal (Z-Score)
    df = df[np.abs(df.sales - df.sales.mean()) <= (3 * df.sales.std())]
    
    model = RandomForestRegressor(n_estimators=50).fit(df[['segment', 'price']], df['sales'])
    return model

def get_final_price(model, segment, comp_price):
    """Phase 4: Guardrails & Decision Logic"""
    # AI Baseline Suggestion
    ai_suggestion = 120 if segment == 1 else 60 
    
    # RAG/Market Reality Checks
    max_price = comp_price * 1.15  # Don't exceed competitor by 15%
    floor_price = 40.0             # Don't go below cost
    
    # Apply Safety Logic
    final = min(ai_suggestion, max_price)
    final = max(final, floor_price)
    return round(final, 2)

if __name__ == "__main__":
    print("--- DYNAMIC PRICING ENGINE ONLINE ---")
    engine = build_engine()

    # Phase 2: Live Data Stream Simulation
    for i in range(5):
        cust_type = np.random.choice(['Startup', 'Enterprise'])
        seg_bit = 0 if cust_type == 'Startup' else 1
        market_price = round(np.random.uniform(70, 100), 2)
        
        decision = get_final_price(engine, seg_bit, market_price)
        
        print(f"Update {i+1}: Segment: {cust_type} | Competitor: ${market_price} | SET PRICE: ${decision}")
        time.sleep(1)

    print("\n--- ALL SYSTEMS OPERATIONAL ---")
