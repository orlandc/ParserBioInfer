import xml.dom.minidom
import os

path = os.getcwd() + '/BioInfer'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(os.path.join(r, file))

for i, f in enumerate(files):
    
    
    path2 = f.replace("BioInfer/", "raw/")
    name2 = path2.replace("_1.1.1.xml", "_raw.txt")
    if not os.path.exists(os.path.dirname(name2)):
        os.makedirs(os.path.dirname(name2))
    
    print (name2 + "\n" )

    file2 = open(name2, "a+")

    doc = xml.dom.minidom.parse(f);
    sentence = doc.getElementsByTagName("sentence")
    
    for tag in sentence:
        word = tag.getAttribute("origText")
        file2.write(word + "\n")
    
    file2.close()
