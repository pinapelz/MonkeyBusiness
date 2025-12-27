from tinydb import TinyDB, Query
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

db = TinyDB("db.json", indent=2, encoding="utf-8", ensure_ascii=False)
table = db.table("polaris_profile")

print("Updating all Polaris profiles to set name='TESTUSER'...")
table.update({"name": "TESTUSER"})
print("Done.")
