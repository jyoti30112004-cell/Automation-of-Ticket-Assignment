# Automation of Ticket Assignment

## Overview
Automation of Ticket Assignment is a Python project that assigns tickets based on attendance data stored in an Excel file.

## Features
- Fetches ticket information
- Reads attendance from Excel
- Identifies Employees and Vendors
- Allocates tickets using a 30:70 split
- Posts/displays the final allocation
- Modular Python structure

## Tech Stack
- Python 3
- Pandas
- OpenPyXL

## Project Structure

```
main.py
step1_fetch_tickets.py
step2_attendance.py
step3_allocate.py
step4_post_tickets.py
solvernot2.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Input
- Excel file (`RAWDATA4.xlsx`) containing attendance and mapping information.

## Output
- Ticket allocation for Employees and Vendors.
- Allocation summary printed in the terminal.

## Future Improvements
- GUI using Tkinter or Streamlit
- Database integration
- Automatic email notifications
- Logging and error handling

## Author
Jyoti Yadav