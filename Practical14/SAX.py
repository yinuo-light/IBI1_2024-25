import xml.sax
from datetime import datetime

# Define a custom SAX handler class to process the XML file
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        # Initialize variables to store current parsing state and collected data
        self.current_data = ""
        # Store the id, name,namespace of the term
        self.id = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0
        # Set a list to store all processed terms
        self.terms = []
        
 
    def startElement(self, tag, attributes):
        self.current_data = tag
        # Reset variables for a new term
        if tag == "term":
            self.id = ""
            self.name = ""
            self.is_a_count = 0
            self.namespace = ""
        # Count the <is_a> number for the current term
        elif tag == "is_a":
            self.is_a_count += 1
            
    def characters(self, content):
        # Append content to the appropriate variable 
        if self.current_data == "id":
            self.id += content
        elif self.current_data == "name":
            self.name += content
        elif self.current_data == "namespace":
            self.namespace += content
            
    def endElement(self, tag):
        # Check if the term belongs to one of the namespaces  
        if tag == "term":
            # Store the term information in the list
            if self.namespace in ["molecular_function", "biological_process", "cellular_component"]:
                self.terms.append({
                    # Remove any leading/trailing whitespace
                    "id": self.id.strip(),
                    "name": self.name.strip(),
                    "namespace": self.namespace.strip(),
                    "is_a_count": self.is_a_count
                })
        self.current_data = ""

def analyze_with_sax(xml_file):
    # Record the start time
    start_time = datetime.now()
    
    # Create a SAX parser
    parser = xml.sax.make_parser()
    # Turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    # Create handler
    handler = GOHandler()
    parser.setContentHandler(handler)
    
    # Parse the XML
    parser.parse(xml_file)
    
    # Process results
    results = {
        "molecular_function": {"max_count": 0, "term": None},
        "biological_process": {"max_count": 0, "term": None},
        "cellular_component": {"max_count": 0, "term": None}
    }
    
    for term in handler.terms:
        namespace = term["namespace"]
        # Check if the current term has more <is_a> elements than the previously recorded maximum
        if term["is_a_count"] > results[namespace]["max_count"]:
            results[namespace]["max_count"] = term["is_a_count"]
            results[namespace]["term"] = term
    
    # Record the end time
    end_time = datetime.now()
    time_taken = end_time - start_time
    
    return results, time_taken

if __name__ == "__main__":
    xml_file = "go_obo.xml"
    
    # SAX analysis
    sax_results, sax_time = analyze_with_sax(xml_file)
    
    print("\nResults using SAX API:")
    for namespace, data in sax_results.items():
        term = data["term"]
        if term:
            print(f"{namespace}: {term['id']} with {term['is_a_count']} <is_a> elements")
        else:
            print(f"{namespace.replace('_', ' ').title()}: No terms found")
    
    print(f"\nSAX processing time: {sax_time.total_seconds():.4f} seconds")

    # Compared to the DOM API, SAX has a relatively shorter processing time.

