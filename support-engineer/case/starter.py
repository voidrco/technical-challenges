import csv

def aggregate(path):
    rows = list(csv.DictReader(open(path, newline="")))
    return {"total": sum(float(row["quantity"]) for row in rows)}

if __name__ == "__main__":
    print(aggregate("case/input.csv"))
