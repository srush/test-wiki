import yaml
import xml.etree.ElementTree as ET
tree = ET.parse('/tmp/q.txt')
root = tree.getroot()


data = {"snippets" : []}
my_tree = data["snippets"]

class Processor:
    def __init__(self):
        self.head = None
        self.title = None
        self.table_head = None
        self.active_questions = {}
        
    def process(self, root): 
        if root.tag == "doc":
            self.title = root.attrib["title"]
            self.active_questions["pages"] = [f"Please describe {self.title}"]
        elif root.tag == "table":
            self.table_head = root[0].text
            self.active_questions["table"] = [f"Give facts about {self.title}"]
        elif root.tag == "row":
            my_tree.append({"text": " | ".join([c.text for c in root]),
                            "questions": [q for v in self.active_questions.values() for q in v],
            })
            
        elif root.tag == "head":
            self.head = root.text
            if self.head != self.title:
                self.active_questions["header"] = [f"Please describe {self.head} with respect to {self.title}"]
        elif root.tag == "p":
            #print("head", [q for v in self.active_questions.values() for q in v],
            #      "text", root.text)
            my_tree.append({"text": root.text, "questions": [q for v in self.active_questions.values() for q in v],
            } )
            
        for child in root:  
            self.process(child)


        if root.tag == "doc":
            pass
        elif root.tag == "table":
            self.active_questions["table"] = []
            self.table_head = None
        elif root.tag == "row":
            pass
        elif root.tag == "head":
            pass
        elif root.tag == "p":
            pass
            
Processor().process(root)
print(yaml.dump(data))
