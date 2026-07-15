import pandas as pd

# Read the Excel file
df = pd.read_excel("RAWDATA4.xlsx")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date column into DD-MM-YYYY format
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d-%m-%Y")

# Take user input
date = input("Enter date (DD-MM-YYYY): ")
total_tickets = int(input("Enter total tickets: "))

# Find attendance record for the given date
row = df[df["Date"] == date]

# Check if date exists
if row.empty:
    print("Date not found!")

else:
    # Convert DataFrame row into a Series
    row = row.iloc[0]

    # Store all present people
    present_people = []

    # Check attendance of each person
    for name in df["Name"].dropna():

        # Ensure the person's name exists as a column
        if name in df.columns:

            # Add person if marked Present (P)
            if str(row[name]).upper() == "P":
                present_people.append(name)

    # Display ticket allocation
    print("\nTicket Allocation")

    # Distribute tickets equally among present people
    for i, person in enumerate(present_people):

        tickets = total_tickets // len(present_people)

        # Distribute remaining tickets one by one
        if i < total_tickets % len(present_people):
            tickets += 1

        print(f"{person} -> {tickets} tickets")