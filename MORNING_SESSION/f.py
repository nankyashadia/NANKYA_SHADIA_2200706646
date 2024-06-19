import xml.etree.ElementTree as ET

def write_xml(file_name):
    # Create the root element
    root = ET.Element("vehicles")

    # Create a sub-element
    car = ET.SubElement(root, "car")
    ET.SubElement(car, "make").text = "Toyota"
    ET.SubElement(car, "model").text = "Corolla"
    ET.SubElement(car, "year").text = "2020"

    bike = ET.SubElement(root, "bike")
    ET.SubElement(bike, "make").text = "Yamaha"
    ET.SubElement(bike, "type").text = "Sport"
    ET.SubElement(bike, "year").text = "2019"

    truck = ET.SubElement(root, "truck")
    ET.SubElement(truck, "make").text = "Ford"
    ET.SubElement(truck, "capacity").text = "F-150"
    ET.SubElement(truck, "year").text = "2021"

    # Create a new XML file with the results
    tree = ET.ElementTree(root)
    tree.write(file_name)

def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for vehicle in root:
        print(f"Vehicle Type: {vehicle.tag}")
        for detail in vehicle:
            print(f"{detail.tag.capitalize()}: {detail.text}")
        print()

# Example usage
write_xml("vehicles.xml")
read_xml("vehicles.xml")