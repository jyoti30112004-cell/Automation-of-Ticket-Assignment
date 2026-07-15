import pandas as pd

df = pd.read_excel("RAWDATA4.xlsx")
df.columns = df.columns.str.strip()

df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d-%m-%Y")

date = input("Enter date (DD-MM-YYYY): ")

row = df[df["Date"] == date]

if row.empty:
    print("Date not found!")

else:
    row = row.iloc[0]

    print(f"\nAttendance for {date}")

    for name in df["Name"].dropna():

        if name in df.columns:

            if str(row[name]).upper() == "P":
                print(name, "- Present")

            elif str(row[name]).upper() == "A":
                print(name, "- Absent")