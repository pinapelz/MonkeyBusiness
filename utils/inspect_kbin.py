try:
    from kbinxml import KBinXML
    from lxml import etree
    import inspect
    
    print("--- KBinXML.to_binary Signature ---")
    try:
        print(inspect.signature(KBinXML.to_binary))
    except:
        print("Cannot get signature")
    
    print("\n--- Testing Encoding ---")
    # Case 1: Unicode S (Fullwidth)
    xml_str = '<root><str>Ｓ</str></root>'
    root = etree.fromstring(xml_str)
    
    k = KBinXML(root)
    binary = k.to_binary()
    print("Binary Output Hex:", binary.hex())
    
    # 0x8272 is ShiftJIS 'S'. 0xEFBCB3 is UTF8 'S'.
    if b'\x82\x72' in binary:
        print("DETECTED: Shift-JIS")
    elif b'\xef\xbc\xb3' in binary:
        print("DETECTED: UTF-8")
    else:
        print("DETECTED: Unknown")

except Exception as e:
    print(f"Error: {e}")
