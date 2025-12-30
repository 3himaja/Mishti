# --- STEP 1: INSTALL DEPENDENCIES ---
!pip install -q gradio supabase requests

# --- STEP 2: FETCH THE GOLDEN IMAGE ---
import requests

url = "https://raw.githubusercontent.com/sudhir-voleti/mishtee-magic/refs/heads/main/cust_view_app.py"

try:
    response = requests.get(url)
    if response.status_code == 200:
        with open("instructor_app.py", "w") as f:
            f.write(response.text)
        print("✅ Verified script successfully downloaded from GitHub.")
    else:
        print(f"❌ Failed to fetch script (Status: {response.status_code}).")
except Exception as e:
    print(f"❌ Error: {e}")

# --- STEP 3: LAUNCH THE PORTAL ---
%run instructor_app.py
