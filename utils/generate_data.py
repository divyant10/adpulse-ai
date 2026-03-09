import pandas as pd
import numpy as np

n = 100000

# Ads campaign dataset
ads_data = pd.DataFrame({
    "campaign_id": range(1, n+1),
    "impressions": np.random.randint(1000, 50000, n),
    "clicks": np.random.randint(50, 5000, n),
    "ctr": np.random.uniform(0.5, 10, n),
    "cpc": np.random.uniform(0.2, 5, n),
    "conversion_rate": np.random.uniform(0.1, 5, n),
    "campaign_type": np.random.choice(["Search","Display","Video","Shopping"], n),
    "budget": np.random.randint(100, 10000, n)
})

ads_data.to_csv("data/ads_campaign_data.csv", index=False)

# Support tickets dataset
support_data = pd.DataFrame({
    "ticket_id": range(1, n+1),
    "issue_type": np.random.choice(
        ["Billing","Login","Campaign Issue","Tracking Error","Account Suspension"], n),
    "priority": np.random.choice(["Low","Medium","High"], n),
    "resolution_time": np.random.randint(1, 72, n),
    "customer_type": np.random.choice(["Small Business","Agency","Enterprise"], n),
    "time_of_day": np.random.choice(["Morning","Afternoon","Evening","Night"], n),
    "status": np.random.choice(["Resolved","Pending","Escalated"], n)
})

support_data.to_csv("data/support_tickets.csv", index=False)

print("Datasets generated successfully!")