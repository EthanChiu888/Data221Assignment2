import pandas as panda

df = panda.read_csv("crime.csv")


def classify_risk(value):
    if value >= 0.50:
        return "High-Crime"
    else:
        return "LowCrime"

df["risk"] = df["ViolentCrimesPerPop"].apply(classify_risk)

avg_unemployment = df.groupby("risk")["PctUnemployed"].mean()

print("Average unemployment rate by risk group:")
print(f"High-Crime:{avg_unemployment['High-Crime']:.2f}")
print(f"LowCrime:{avg_unemployment['LowCrime']:.2f}")