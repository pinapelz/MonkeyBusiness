try:
    from kbinxml import KBinXML
    
    # Inspect class attributes for mapping
    print("KBinXML Attributes:")
    for x in dir(KBinXML):
        print(x)
        
    # Try common variations
    from lxml import etree
    xml_str = '<root><str>TEST</str></root>'
    root = etree.fromstring(xml_str)
    k = KBinXML(root)
    
    candidates = ["UTF-8", "utf8", "ascii", "us-ascii", "shift_jis", "cp932", "EUH"] 
    # EUH etc might be specific keys
    
    for c in candidates:
        try:
            k.to_binary(encoding=c)
            print(f"Supported: {c}")
        except KeyError:
            print(f"Unsupported: {c}")
        except Exception as e:
            print(f"Error {c}: {e}")

except Exception as e:
    print(e)
