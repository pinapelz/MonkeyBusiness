from tinydb import TinyDB

db = TinyDB("db.json", indent=2, encoding="utf-8", ensure_ascii=False)
table = db.table("polaris_profile")
print(f"Before cleanup: {len(table.all())} profiles.")
table.truncate()
print(f"After cleanup: {len(table.all())} profiles.")
print("polaris_profile table cleared successfully.")
