from tinydb import TinyDB, Query
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

db = TinyDB("db.json", indent=2, encoding="utf-8", ensure_ascii=False)
table = db.table("polaris_profile")
User = Query()

print("Updating all Polaris profiles to set is_tutorial_cleared=1...")
table.update({"is_tutorial_cleared": 1})
print("Done.")
