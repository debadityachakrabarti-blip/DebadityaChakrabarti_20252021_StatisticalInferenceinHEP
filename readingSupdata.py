import pandas as pd

data = pd.read_csv(
    "scp42.txt",
    sep=r"\s+"
)

print(data)