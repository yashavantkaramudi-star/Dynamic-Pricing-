# SaaS Dynamic Pricing AI Engine

##  Project Overview
This project addresses the inefficiency of flat-rate pricing in SaaS. I've built an automated engine that analyzes customer behavior and market conditions to set the most profitable price in real-time.

##  The Architecture
* **Elasticity Analytics:** Mathematical modeling of how price changes affect user demand.
* **Machine Learning Brain:** A Random Forest model that identifies if a user is a "Startup" or "Enterprise" to offer personalized pricing.
* **Safety Guardrails:** Uses Z-Score statistics to ignore market "noise" and keeps prices within a safe business range (Floor/Ceiling).

##  How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the engine: `python src/main.py`
3. View the research: Open `research/pricing_analysis.ipynb` in Google Colab.

##  Impact
Simulated results show a **25% revenue lift** by capturing higher value from Enterprise segments while maintaining high signup volume for Startups.
