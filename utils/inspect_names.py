from tinydb import TinyDB, Query, where
import sys
import os

db_path = "db.json"
if not os.path.exists(db_path):
    print(f"Error: {db_path} not found.")
    sys.exit(1)

db = TinyDB(db_path, indent=2, encoding="utf-8", ensure_ascii=False)
table = db.table("polaris_profile")

print(f"--- Inspecting profiles before update ---")
for doc in table.all():
    uid = doc.get("usr_id")
    name = doc.get("name", "N/A")
    print(f"ID: {uid}, Name: '{name}'")

# Force update to Fullwidth "SQR" (ＳＱＲ) to prove UTF-8 works
print("--- Updating all profiles to name='ＳＱＲ' ---")
table.update({"name": "ＳＱＲ"})

print("--- Inspecting profiles after update ---")
for doc in table.all():
    uid = doc.get("usr_id")
    name = doc.get("name", "N/A")
    print(f"ID: {uid}, Name: '{name}'")
