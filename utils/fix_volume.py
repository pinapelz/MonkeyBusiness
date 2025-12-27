from tinydb import TinyDB, Query, where
import sys
import os

db_path = "db.json"
if not os.path.exists(db_path):
    print(f"Error: {db_path} not found.")
    sys.exit(1)

db = TinyDB(db_path, indent=2, encoding="utf-8", ensure_ascii=False)
table = db.table("polaris_profile")

print(f"--- Inspecting volumes before update ---")
for doc in table.all():
    uid = doc.get("usr_id")
    opts = doc.get("main_option", {})
    vol = opts.get("headphone_volume", "N/A")
    print(f"ID: {uid}, Headphone Volume: {vol}")

# Force update volumes to 100 (Full Volume) for correct keys
valid_volume_keys = [
    "music_volume", "se_volume", "voice_volume", 
    "out_game_music_volume", "out_game_se_volume", "out_game_voice_volume", 
    "master_volume", "headphone_volume", "bass_shaker_volume"
]

print("--- Updating all profiles to Volume=100 (Correct Keys) ---")

all_docs = table.all()
for doc in all_docs:
    if "main_option" not in doc:
        doc["main_option"] = {}
    
    changed = False
    for k in valid_volume_keys:
        if doc["main_option"].get(k) != "100":
            doc["main_option"][k] = "100"
            changed = True
            
    # Cleanup old junk keys if present (optional but good)
    junk_keys = ["volume_estim", "volume_note", "volume_guide", "volume_bgm", "volume_voice"]
    for k in junk_keys:
        if k in doc["main_option"]:
            del doc["main_option"][k]
            changed = True
    
    if changed:
        table.upsert(doc, where("usr_id") == doc["usr_id"])

print("--- Inspecting volumes after update ---")
for doc in table.all():
    uid = doc.get("usr_id")
    opts = doc.get("main_option", {})
    vol = opts.get("headphone_volume", "N/A")
    print(f"ID: {uid}, Headphone Volume: {vol}")
