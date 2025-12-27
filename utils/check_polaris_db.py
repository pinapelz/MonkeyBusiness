from tinydb import TinyDB, Query
import sys
import os

# Add root to sys.path to import core_database
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

db = TinyDB("db.json", indent=2, encoding="utf-8", ensure_ascii=False)
table = db.table("polaris_profile")

print(f"Polaris Profile Count: {len(table.all())}")
for item in table.all():
    print(f"User: {item.get('name')} (ID: {item.get('usr_id')})")
    print(f"  Tutorial Cleared: {item.get('is_tutorial_cleared')}")
    print(f"  RefID: {item.get('refid')}")
    print(f"  DataID: {item.get('dataid')}")
    print(f"  Card: {item.get('card')}")
