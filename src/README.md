# SaaS Dynamic Pricing AI

## Overview
An engineering-led approach to solving revenue loss in SaaS. This engine uses **Machine Learning** to calculate price elasticity and optimize pricing for different customer segments (Startup vs. Enterprise).

## Architecture
1. **Analytics:** Uses Linear Regression for Price Elasticity.
2. **Intelligence:** Random Forest Regressor for segmented demand forecasting.
3. **Guardrails:** Statistical Z-Score outlier removal and price-floor/ceiling logic.
4. **Simulation:** Real-time event ingestion simulation.

## Usage
Run `python src/main.py` to see the real-time pricing decisions.
