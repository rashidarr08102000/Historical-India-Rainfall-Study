import pandas as pd

df = pd.read_csv(r"/storage/emulated/0/Download/district wise rainfall normal.csv")

#print(df.head()) 
#print(df.dtypes)
#print(df.isnull().sum())
#Top Ten Wettest Districts - Annual
print("\n Top 10 Wettest Districts (Annual Rainfall):")

top_10_wettest_dist =df.sort_values(by="ANNUAL", ascending=False).head(10)
print(top_10_wettest_dist)

#Top Ten Driest District-Annual
print("\n Top 10 Driest Districts (Annual Rainfall):")

top_10_driest_dist=df.sort_values(by="ANNUAL", ascending=True).head(10)
print(top_10_driest_dist)

#State wise Average Annual Rainfall
print("\n State-wise Average Annual Rainfall:")
statewise_avg_annual_rf =df.groupby("STATE_UT_NAME")["ANNUAL"].mean().sort_values(ascending=False)
print(statewise_avg_annual_rf)

#State's District with the Most rainfall
print("\n District with the Highest Rainfall in Each State:")

sorted_df = df.sort_values(["STATE_UT_NAME", "ANNUAL"], ascending=[True, False])
max_rainfall_districts = sorted_df.drop_duplicates("STATE_UT_NAME", keep="first")
most_rf_dist=max_rainfall_districts[["STATE_UT_NAME", "DISTRICT", "ANNUAL"]].sort_values(by="ANNUAL", ascending=False)
print(most_rf_dist)

#Cumulative Rainfall Across Districts in Each State
print("\n Cumulative Annual Rainfall per State (All Districts Combined):")

cum_state_rf =df.groupby("STATE_UT_NAME")["ANNUAL"].sum().sort_values(ascending=False)
print(cum_state_rf) 
#New Column for avg monthly rainfall

df["AVG_MONTHLY"] = df[["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]].mean(axis=1)
print("\n Average Monthly Rainfall:")
print(df[["DISTRICT", "AVG_MONTHLY"]].head())

#Rainfall in Monsoon VS Non-Monsoon
print("\n📌 Monsoon VS Non-Monsoon:")

df["Monsoon_Share"] = df["Jun-Sep"] / df["ANNUAL"]
top_monsoon_share =df[["DISTRICT", "Monsoon_Share"]].sort_values(by="Monsoon_Share", ascending=False).head()
print(top_monsoon_share)

#State with most Seasonal Variations
print("\n State with Most Seasonal Variations:")

df["SEASONAL_RANGE"] = df[["Jan-Feb", "Mar-May", "Jun-Sep", "Oct-Dec"]].max(axis=1) - df[["Jan-Feb", "Mar-May", "Jun-Sep", "Oct-Dec"]].min(axis=1)
state_most_seasonal_variations =df.sort_values("SEASONAL_RANGE", ascending=False).head()
print(state_most_seasonal_variations)

#Uniform Rainfall Districts
print("\n Uniform Rainfall Districts:")

df["MONTHLY_STD"] = df[["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]].std(axis=1)
print(df.sort_values("MONTHLY_STD").head())

#Highest Rainfall Month in each Districts
print("\n Highest Rainfall Month in each Districts:")
df["Highest_Month"] = df[["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]].idxmax(axis=1)
print(df[["DISTRICT", "Highest_Month"]].head())

#National Level Rainfall Ranks -District wise
print("\n National Level Rainfall Ranks to each District:")
df["Rainfall_Rank"] = df["ANNUAL"].rank(ascending=False)
print(df[["DISTRICT", "ANNUAL", "Rainfall_Rank"]].sort_values("Rainfall_Rank").head()) 









