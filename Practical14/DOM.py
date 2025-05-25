import xml.dom.minidom
from datetime import datetime

# Use datetime to record the start time
start_time = datetime.now()
# Load the XML file
doc = xml.dom.minidom.parse("go_obo.xml")

# Find all <term> nodes
terms = doc.getElementsByTagName("term")

# Initialize variables
max_is_a = {}
for namespace in ["molecular_function", "biological_process", "cellular_component"]:
    max_is_a[namespace] = {"id": None, "count": 0}

# Traverse each term
for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.data
    is_a_elements = term.getElementsByTagName("is_a")
    count = len(is_a_elements)
    
    if count > max_is_a[namespace]["count"]:
        max_is_a[namespace]["id"] = term.getElementsByTagName("id")[0].firstChild.data
        max_is_a[namespace]["count"] = count

# Record the end time
end_time = datetime.now()

# Print the results
for namespace, data in max_is_a.items():
    print(f"{namespace}: {data['id']} with {data['count']} <is_a> elements")

print("DOM processing time:", end_time - start_time,"seconds")

# Compared to the SAX API, DOM has a relatively longer processing time.
