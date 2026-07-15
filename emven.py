import pandas as pd

# Read Excel file
df = pd.read_excel("RAWDATA4.xlsx")
df.columns = df.columns.str.strip()

# Format Date column
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d-%m-%Y")

# User inputs
date = input("Enter date (DD-MM-YYYY): ")
total_tickets = int(input("Enter total tickets: "))

# Get record for selected date
row = df[df["Date"] == date]

if row.empty:
    print("Date not found!")

else:
    row = row.iloc[0]

    # Employee and Vendor lists
    emp_present = []
    ven_present = []

    # Check attendance
    for _, r in df[["Name", "Emp/Ven"]].dropna().iterrows():

        name = r["Name"]

        if name in df.columns and str(row[name]).upper() == "P":

            if r["Emp/Ven"] == "Emp":
                emp_present.append(name)

            elif r["Emp/Ven"] == "Ven":
                ven_present.append(name)

    # 30-70 split
    emp_tickets = round(total_tickets * 0.30)
    ven_tickets = total_tickets - emp_tickets

    print("\nTicket Allocation")

    # Employee allocation
    print(f"\nEmployee Tickets = {emp_tickets}")

    if emp_present:
        for i, person in enumerate(emp_present):

            tickets = emp_tickets // len(emp_present)

            if i < emp_tickets % len(emp_present):
                tickets += 1

            print(f"{person} -> {tickets} tickets")

    # Vendor allocation
    print(f"\nVendor Tickets = {ven_tickets}")

    if ven_present:
        for i, person in enumerate(ven_present):

            tickets = ven_tickets // len(ven_present)

            if i < ven_tickets % len(ven_present):
                tickets += 1

            print(f"{person} -> {tickets} tickets")