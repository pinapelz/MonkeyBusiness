from kbinxml import KBinXML
import lxml.etree as ET

root = ET.Element("test")
root.text = "테스트" # Korean text to test encoding
try:
    k = KBinXML(root)
    print("Items in KBinXML object:", dir(k))
    if hasattr(k, "encoding"):
        print(f"Current encoding: {k.encoding}")
        k.encoding = "UTF-8"
        print("Set encoding to UTF-8")
        
    binary = k.to_binary()
    print(f"Binary generated, len={len(binary)}")
    print(f"Binary content sample: {binary[:20]}")
    
except Exception as e:
    print(f"Error: {e}")
