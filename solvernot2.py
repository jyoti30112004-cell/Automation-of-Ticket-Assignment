import pandas as pd

df = pd.read_excel("RAWDATA4.xlsx")
df.columns = df.columns.str.strip()

attendance = df.iloc[:30]
mapping = df[["Name", "Emp/Ven", "Solver/Not"]].dropna()

attendance["Date"] = pd.to_datetime(attendance["Date"]).dt.strftime("%d-%m-%Y")

date = input("Enter date (DD-MM-YYYY): ")
row = attendance.loc[attendance["Date"] == date]

if row.empty:
    print("Date not found!")
else:
    row = row.iloc[0]

    total = 16
    split = {"Emp": round(total * 0.3)}
    split["Ven"] = total - split["Emp"]

    for role in ["Emp", "Ven"]:

        people = [
            r["Name"]
            for _, r in mapping.iterrows()
            if r["Emp/Ven"] == role
            and r["Solver/Not"] == "Y"
            and str(row[r["Name"]]).upper() == "P"
        ]

        print(f"\n{role} Tickets = {split[role]}")

        for i, p in enumerate(people):
            t = split[role] // len(people) + (i < split[role] % len(people))
            print(f"{p} -> {t}")