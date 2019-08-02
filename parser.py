import xml.dom.minidom
import os

path = os.getcwd() + '/BioInfer'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(os.path.join(r, file))

def getWord(node):
    oracion = ""
    for parent in node.childNodes:
        if parent.nodeType != parent.TEXT_NODE:
            print(parent.getAttribute("origText"))
            if parent.getAttribute("origText") != "":
                oracion += parent.getAttribute("origText") + " "
            else:
                oracion += getWord(parent)
    
    return oracion

for i, f in enumerate(files):
    
    path2 = f.replace("BioInfer_corpus_1.1.1", "raw")
    name2 = path2.replace(".xml", ".txt")
    if not os.path.exists(os.path.dirname(name2)):
        os.makedirs(os.path.dirname(name2))
    
    print (name2 + "\n" )

    file2 = open(name2, "a+")

    doc = xml.dom.minidom.parse(f);
    sentence = doc.getElementsByTagName("sentence")
    for tag in sentence:
        print (getWord(tag))
        #print(tag)
        #file2.write(getWord(tag).encode('utf8') + "\n")
    
    file2.close()
