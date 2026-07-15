# ============================================================
#  step3_allocate.py
#  Present + Solver logon ko 30-70 split mein tickets deta hai
#
#  Rule:
#    Employees  → 30% of total tickets
#    Vendors    → 70% of total tickets
#    Sirf Solver=Y wale logon ko milte hain tickets
#    Remaining tickets equally distribute hote hain
# ============================================================

from config import TOTAL_TICKETS, EMP_SPLIT


def allocate_tickets(present, total_tickets=None):
    """
    Ticket allocation karta hai.

    Args:
        present (dict): step2 se aaya {Emp:[{name,solver}], Ven:[...]}
        total_tickets (int): override karo ya config se lega

    Returns:
        allocation (dict): { person_name : ticket_count }
    """

    if total_tickets is None:
        total_tickets = TOTAL_TICKETS

    emp_total = round(total_tickets * EMP_SPLIT)
    ven_total = total_tickets - emp_total

    print("\n" + "="*55)
    print("  STEP 3 : Ticket Allocation  (Emp 30% | Ven 70%)")
    print("="*55)
    print(f"\n  Total Tickets    : {total_tickets}")
    print(f"  Employee Share   : {emp_total}  (30%)")
    print(f"  Vendor Share     : {ven_total}  (70%)")

    allocation = {}   # { name : ticket_count }

    for role, share in [("Emp", emp_total), ("Ven", ven_total)]:

        # Sirf Solver=Y aur Present log
        solvers = [p["name"] for p in present[role] if p["solver"] == "Y"]

        print(f"\n  ── {role} ({'Employees' if role=='Emp' else 'Vendors'}) ──────────────────")
        print(f"  Share : {share} tickets")

        if not solvers:
            print(f"  ⚠️  Koi Solver present nahi — tickets skip.")
            continue

        print(f"  Solvers Present : {solvers}")
        print()

        for i, name in enumerate(solvers):
            # Equal split + remainder ek-ek karke pehle walon ko
            t = share // len(solvers) + (1 if i < share % len(solvers) else 0)
            allocation[name] = t
            print(f"  {name:<25} → {t:>3} tickets")

    print(f"\n  ── FINAL ALLOCATION ─────────────────────────")
    for name, count in allocation.items():
        print(f"  {name:<25} : {count} tickets")

    return allocation


# ---- Standalone run ----
if __name__ == "__main__":
    # Test data
    sample_present = {
        "Emp": [{"name": "JYOTI",    "solver": "Y"},
                {"name": "AARUSHI",  "solver": "N"}],
        "Ven": [{"name": "AKSHITA",  "solver": "Y"},
                {"name": "ROBIN",    "solver": "Y"}]
    }
    allocate_tickets(sample_present)
