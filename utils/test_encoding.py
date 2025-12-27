try:
    from lxml.builder import ElementMaker
    from kbinxml import KBinXML
except ImportError:
    print("Missing specific libs, simulating logic manually with standard libs")

def test_encoding():
    # Simulate DB data
    name = "ＳＱＲ" # Fullwidth SQR
    shop = "未設定"
    
    # 1. Create XML content (simplified)
    # <usr><usr_profile><usr_name>ＳＱＲ</usr_name></usr_profile></usr>
    # In core_common, we rely on KBinXML/lxml to generate the string.
    # Let's assume KBinXML.to_text() returns standard python string with UTF-8 declaration by default.
    
    # Simulating what KBinXML.to_text() likely outputs:
    xml_text_raw = f'<?xml version="1.0" encoding="UTF-8"?>\n<usr>\n  <usr_profile>\n    <usr_name>{name}</usr_name>\n    <shop_name>{shop}</shop_name>\n  </usr_profile>\n</usr>'
    
    print(f"Original Text (Internal): {xml_text_raw}")
    
    # 2. Apply logic from core_common.py
    xml_text = xml_text_raw
    xml_text = xml_text.replace('encoding="UTF-8"', 'encoding="Windows-31J"')
    
    print(f"Modified Text Header: {xml_text}")
    
    try:
        xml_binary = xml_text.encode("cp932", errors="replace")
        print("Encoding 'cp932' SUCCESS")
        print(f"Bytes: {xml_binary}")
        
        # Check if bytes look right for SQR
        # Fullwidth S: 82 72 (in shift jis)
        # SQR -> 8272 8270 8271 ??? No match
        # ShiftJIS: S=8272 ?
        # Let's print hex
        print(f"Hex: {xml_binary.hex()}")
        
    except Exception as e:
        print(f"Encoding FAILED: {e}")

if __name__ == "__main__":
    test_encoding()
