#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse


def extract_methods(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
        if not content.startswith("<"):
            raise ValueError("File does not appear to contain XML Content.")
        if not content.startswith("<root>"):
            content = "<root>" + content + "</root>"

            try:
                root = ET.formstring(content)
            except ET.ParseError as e:
                print(f"Error parsing XML: {e}")
                return

            for elem in root.iter('string'):
                if elem.text:
                    print(elem.text)

                    def main():
                        parser = argparse.ArgumentParser(description="XML-RPC")
                        parser.add_argument("filename", help="XML file calls.")
                        args = parser.parse_args()

                        extract_methods(args.filename)

                        if __name__ == "__main__":
                            main()