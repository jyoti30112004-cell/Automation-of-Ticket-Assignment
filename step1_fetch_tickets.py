# ============================================================
#  step1_fetch_tickets.py
#  API se ticket list fetch karo aur Excel + JSON mein save karo
#  Output : tickets_ddmmyy_hhmmss.xlsx  |  output.json
# ============================================================

import requests
import json
import pandas as pd
from datetime import datetime
from config import API_URL, API_KEY, ORG_ID, INSTANCE, WORKGROUP


def fetch_tickets(page_size=100):
    """
    API call karke assigned tickets laata hai.
    Returns: (excel_filename, ticket_number_list)
    """

    print("\n" + "="*55)
    print("  STEP 1 : API se Ticket List Fetch kar raha hoon")
    print("="*55)

    payload = {
        "ServiceName": "IM_GetIncidentList",
        "objCommonParameters": {
            "_ProxyDetails": {
                "AuthType": "APIKey",
                "APIKey": API_KEY,
                "ProxyID": 0,
                "ReturnType": "json",
                "OrgID": ORG_ID,
                "TokenID": ""
            },
            "objIncidentCommonFilter": {
                "WorkgroupName": WORKGROUP,
                "CurrentPageIndex": 0,
                "PageSize": page_size,
                "OrgID": str(ORG_ID),
                "Instance": INSTANCE,
                "Status": "Assigned",
                "IsWebServiceRequest": True
            }
        }
    }

    try:
        print("  🔄 API call ho rahi hai...")
        response = requests.post(API_URL, json=payload, timeout=30)
        print(f"  Status Code : {response.status_code}")

        # ---- Failure check ----
        if response.status_code != 200:
            print("  ❌ API ne 200 nahi diya. Response:")
            print("    ", response.text[:300])
            return None, []

        data = response.json()

        # ---- Raw JSON save ----
        with open("output.json", "w") as f:
            json.dump(data, f, indent=4)
        print("  ✅ Raw JSON saved  → output.json")

        # ---- Extract tickets ----
        tickets = data.get("OutputObject", {}).get("MyTickets", [])

        if not tickets:
            print("  ⚠️  Response mein koi ticket nahi mila.")
            return None, []

        print(f"  📋 Total Tickets mili : {len(tickets)}")

        # ---- JSON → DataFrame → Excel ----
        df = pd.DataFrame(tickets)
        timestamp     = datetime.now().strftime("%d%m%y_%H%M%S")
        excel_filename = f"tickets_{timestamp}.xlsx"
        df.to_excel(excel_filename, index=False)
        print(f"  ✅ Excel saved         → {excel_filename}")

        # ---- Ticket numbers list ----
        if "Ticket_No" in df.columns:
            ticket_numbers = df["Ticket_No"].astype(str).tolist()
        else:
            ticket_numbers = []
            print("  ⚠️  'Ticket_No' column nahi mili DataFrame mein.")

        return excel_filename, ticket_numbers

    except requests.exceptions.ConnectionError:
        print("  ❌ Server se connect nahi ho paaya. Network/URL check karo.")
        return None, []
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return None, []


# ---- Standalone run ----
if __name__ == "__main__":
    excel_file, tickets = fetch_tickets()
    if tickets:
        print(f"\n  Ticket Numbers : {tickets[:5]} ... (total {len(tickets)})")
