# ============================================================
#  main.py — Ticket Management System — Full Auto Flow
#
#  Steps:
#   1. API se ticket list fetch karo  → Excel + JSON save
#   2. Attendance check karo          → Present / Absent alag
#   3. 70-30 split mein tickets baanto → sirf Solvers ko
#   4. API ke through assign karo     → result Excel mein save
#
#  Run: python main.py
# ============================================================

from step1_fetch_tickets import fetch_tickets
from step2_attendance    import check_attendance
from step3_allocate      import allocate_tickets
from step4_post_tickets  import post_tickets


def main():
    print("\n" + "★"*55)
    print("   TICKET MANAGEMENT SYSTEM — Full Auto Flow")
    print("★"*55)

    # ── Date input ──────────────────────────────────────────
    date = input("\nEnter date (DD-MM-YYYY): ").strip()

    total_override = input("Total tickets (Enter dabao default ke liye): ").strip()
    total_tickets  = int(total_override) if total_override.isdigit() else None

    # ── STEP 1: API Fetch ───────────────────────────────────
    excel_file, ticket_numbers = fetch_tickets()

    # ── STEP 2: Attendance ──────────────────────────────────
    present, absent, row = check_attendance(date)

    if present is None:
        print("\n❌ Attendance nahi mila. Program band.")
        return

    # ── STEP 3: Allocation ──────────────────────────────────
    allocation = allocate_tickets(present, total_tickets)

    if not allocation:
        print("\n⚠️  Kisi ko bhi tickets nahi mile. Program band.")
        return

    # ── STEP 4: Post via API ────────────────────────────────
    confirm = input("\n⚡ Tickets API se assign karein? (y/n): ").strip().lower()

    if confirm == "y":
        post_tickets(allocation, ticket_numbers)
    else:
        print("\n⏩ API posting skip ki gayi.")

    print("\n" + "★"*55)
    print("   ✅ Done!")
    print("★"*55)


if __name__ == "__main__":
    main()
