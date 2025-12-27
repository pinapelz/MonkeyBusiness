import sys
import os

# Add parent directory to path
sys.path.append(os.getcwd())

try:
    import modules
    print("--- Modules Loaded ---")
    
    target = "polaris_gacha_get_gacha_info"
    if hasattr(modules, target):
        print(f"SUCCESS: {target} found in modules.")
    else:
        print(f"FAILURE: {target} NOT found in modules.")
        print("Available polaris items:")
        for x in dir(modules):
            if "polaris" in x:
                print(x)
                
except Exception as e:
    print(e)
