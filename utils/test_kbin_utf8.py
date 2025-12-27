try:
    from kbinxml import KBinXML
    from lxml import etree
    
    print("--- Testing KBinXML(encoding='utf-8') ---")
    xml_str = '<root><str>TEST</str></root>'
    root = etree.fromstring(xml_str)
    
    k = KBinXML(root)
    try:
        # This is the line added to core_common.py
        binary = k.to_binary(encoding="utf-8")
        print("SUCCESS: Encoded with utf-8")
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")
        
except ImportError:
    print("kbinxml not found")
