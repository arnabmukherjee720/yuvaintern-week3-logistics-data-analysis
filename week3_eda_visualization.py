"""Week 3: Advanced Data Analysis and Visualization in Logistics. Dataset is simulated."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
DATA=BASE/"week3_logistics_eda_simulated.csv"
def main():
    df=pd.read_csv(DATA)
    numeric=["Distance_km","Weight_kg","Shipment_Volume_units","Delivery_Days","Shipping_Cost_INR"]
    print("Dataset shape:",df.shape)
    print("\\nMissing values:\\n",df.isna().sum())
    print("\\nDescriptive statistics:\\n",df[numeric].describe().round(2))
    print("\\nStatus percentages:\\n",(df.Delivery_Status.value_counts(normalize=True)*100).round(2))
    print("\\nRegional summary:\\n",df.groupby("Region").agg(Orders=("Order_ID","count"),Avg_Delivery_Days=("Delivery_Days","mean"),Avg_Cost=("Shipping_Cost_INR","mean")).round(2))
    print("\\nCorrelations:\\n",df[numeric].corr().round(2))
    plt.figure(figsize=(8,5)); plt.hist(df.Delivery_Days,bins=14,edgecolor="black"); plt.title("Distribution of Delivery Time"); plt.xlabel("Days"); plt.ylabel("Orders"); plt.tight_layout(); plt.savefig(BASE/"chart_delivery_time_distribution.png"); plt.close()
    plt.figure(figsize=(8,5)); plt.scatter(df.Distance_km,df.Shipping_Cost_INR,alpha=.75); plt.title("Distance vs Shipping Cost"); plt.xlabel("Distance (km)"); plt.ylabel("Cost (INR)"); plt.tight_layout(); plt.savefig(BASE/"chart_distance_vs_cost.png"); plt.close()
    df.groupby("Region").Delivery_Days.mean().plot(kind="bar",title="Average Delivery Time by Region"); plt.ylabel("Days"); plt.tight_layout(); plt.savefig(BASE/"chart_region_delivery.png"); plt.close()
    c=df[numeric].corr(); plt.figure(figsize=(7,5)); plt.imshow(c.values,vmin=-1,vmax=1); plt.xticks(range(len(numeric)),numeric,rotation=35,ha="right"); plt.yticks(range(len(numeric)),numeric); plt.colorbar(); plt.title("Correlation Matrix"); plt.tight_layout(); plt.savefig(BASE/"chart_correlation_matrix.png"); plt.close()
if __name__=="__main__": main()
