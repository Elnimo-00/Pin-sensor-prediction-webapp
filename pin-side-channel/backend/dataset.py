import pandas as pd

def load_dataset(path):
    rows = []

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 7:
                continue

            try:
                row = [float(x) for x in parts]
                label = int(row[0])
                if 0 <= label <= 9:
                    rows.append(row)
            except:
                continue

    df = pd.DataFrame(
        rows,
        columns=["label","f1","f2","f3","f4","f5","f6"]
    )

    return df.drop("label", axis=1), df["label"]
