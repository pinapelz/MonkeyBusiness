from kbinxml import KBinXML
import lxml.etree as ET

def test_encoding():
    root = ET.Element("test")
    xml = KBinXML(root)
    try:
        # Test with encoding arg
        bin_data = xml.to_binary(encoding="UTF-8")
        print("Success: encoding argument supported")
    except TypeError:
        print("Failure: encoding argument NOT supported")
    except Exception as e:
        print(f"Failure: {e}")

if __name__ == "__main__":
    test_encoding()
