import pandas as pd

adult = pd.read_csv("adult.txt", names = ["Age","Work-Class", "fnlwgt", "Education", "Education-Num","Marital-Status", 
"Occupation", "Relationship", "Race", "Sex", "Capital-gain", "Capital-lass", "Hours-per-week", "Native-Country", "Earnings-Raw"])

print(adult[:5])

print(adult["Work-Class"].unique())

adult["LongHours"] = adult["Hours-per-week"] > 40