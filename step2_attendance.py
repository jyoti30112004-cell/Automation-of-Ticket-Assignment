# ============================================================
#  step2_attendance.py
#  Excel se attendance padhta hai — Present / Absent alag dikhata hai
#  Columns expected in RAWDATA4.xlsx:
#    Date | Name | Emp/Ven | Solver/Not | <person_name_columns...>
# ============================================================

import pandas as pd
from config import EXCEL_FILE


def check_attendance(date):
    """
    Diye gaye date ke liye attendance check karta hai.

    Returns:
        present (dict) : { "Emp": [{name, solver},...], "Ven": [...] }
        absent  (dict) : { "Emp": [name,...],           "Ven": [...] }
        row     (Series or None)
    """

    print("\n" + "="*55)
    print("  STEP 2 : Attendance Check")
    print("="*55)

    # ---- File padhna ----
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        print(f"  ❌ File nahi mili: {EXCEL_FILE}")
        return None, None, None

    df.columns = df.columns.str.strip()

    # ---- Date format ----
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d-%m-%Y")

    # ---- Date dhundhna ----
    row = df[df["Date"] == date]
    if row.empty:
        print(f"  ❌ Date '{date}' file mein nahi mili.")
        return None, None, None

    row = row.iloc[0]

    # ---- Name/Role/Solver mapping ----
    mapping = df[["Name", "Emp/Ven", "Solver/Not"]].dropna()

    present = {"Emp": [], "Ven": []}
    absent  = {"Emp": [], "Ven": []}

    # ---- Table Header ----
    print(f"\n  📅 Date : {date}\n")
    print(f"  {'Name':<22} {'Type':<6} {'Solver':<12} Status")
    print(f"  {'-'*52}")

    for _, r in mapping.iterrows():
        name   = str(r["Name"]).strip()
        role   = str(r["Emp/Ven"]).strip()      # Emp / Ven
        solver = str(r["Solver/Not"]).strip()   # Y / N

        # Attendance column mein value lena
        status = str(row.get(name, "")).strip().upper()

        solver_label = "Solver    " if solver == "Y" else "Not Solver"

        if status == "P":
            present[role].append({"name": name, "solver": solver})
            icon = "✅ Present"
        else:
            absent[role].append(name)
            icon = "❌ Absent "

        print(f"  {name:<22} {role:<6} {solver_label:<12} {icon}")

    # ---- Summary ----
    print(f"\n  ── SUMMARY ──────────────────────────────────")
    print(f"  Present Employees : {[p['name'] for p in present['Emp']] or 'None'}")
    print(f"  Present Vendors   : {[p['name'] for p in present['Ven']] or 'None'}")
    print(f"  Absent Employees  : {absent['Emp'] or 'None'}")
    print(f"  Absent Vendors    : {absent['Ven'] or 'None'}")

    return present, absent, row


# ---- Standalone run ----
if __name__ == "__main__":
    date = input("\nEnter date (DD-MM-YYYY): ").strip()
    present, absent, row = check_attendance(date)
