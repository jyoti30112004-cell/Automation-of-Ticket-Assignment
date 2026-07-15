============================================================
  TICKET MANAGEMENT SYSTEM — Project Guide
============================================================

── PROJECT FILES ───────────────────────────────────────────

  config.py              → Saari settings yahan badlo
  main.py                → Poora flow chalao (yahi run karo)

  step1_fetch_tickets.py → API se tickets fetch → Excel save
  step2_attendance.py    → Attendance: Present / Absent
  step3_allocate.py      → 30-70 split, sirf Solvers ko tickets
  step4_post_tickets.py  → API se tickets assign karo

  guessno.py             → 4-Digit Guessing Game (bonus!)

── SETUP ───────────────────────────────────────────────────

  1. Python install karo (3.8+)
  2. Libraries install karo:
       pip install requests pandas openpyxl

  3. config.py kholo aur ye fields set karo:
       API_URL       → server ka address
       API_KEY       → tumhara API key
       EXCEL_FILE    → RAWDATA4.xlsx (ya jo bhi file ho)
       TOTAL_TICKETS → kitne tickets hain
       ASSIGNED_EMAIL→ engineer ka email

── EXCEL FILE FORMAT (RAWDATA4.xlsx) ───────────────────────

  Columns:
    Date        | DD-MM-YYYY ya Excel date format
    Name        | Person ka naam (baaki columns ke header se match kare)
    Emp/Ven     | "Emp" ya "Ven"
    Solver/Not  | "Y" ya "N"
    JYOTI       | P (Present) ya A (Absent)
    AARUSHI     | P ya A
    AKSHITA     | P ya A
    ... (baaki log aise hi)

── RUN KARO ────────────────────────────────────────────────

  Poora system ek saath:
    python main.py

  Alag alag step:
    python step1_fetch_tickets.py
    python step2_attendance.py
    python step3_allocate.py
    python step4_post_tickets.py

  Game:
    python guessno.py

── OUTPUT FILES ────────────────────────────────────────────

  tickets_ddmmyy_hhmmss.xlsx        → Step 1: API se aaye tickets
  output.json                        → Step 1: Raw JSON response
  assignment_result_ddmmyy_hhmmss.xlsx → Step 4: Kaun se tickets assign hue

── RULES ───────────────────────────────────────────────────

  • Employees  → 30% tickets
  • Vendors    → 70% tickets
  • Sirf Solver/Not = Y wale log tickets paate hain
  • Agar koi Solver present nahi → us role ke tickets skip
  • Remaining tickets equally distribute hote hain

============================================================
