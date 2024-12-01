import os

searchFolder = "./docs/learning-course/"

# Find all markdown files in the search folder
allMarkdownFiles = []
for root, dirs, files in os.walk(searchFolder):
    for file in files:
        if file.endswith(".md"):
            allMarkdownFiles.append(os.path.join(root, file))

#Find Slideshow Containers 
#<div class="slideshow-container">

for file in allMarkdownFiles:
    with open(file, 'r', encoding="utf8") as f:
        lines = f.readlines()
        interestingLines = []
        for line in lines:
            if "<img" in line or "<figcaption>" in line:
                interestingLines.append(line)
        
        for i in range(len(interestingLines)):
            if(i < len(interestingLines) - 1):
                #Check if the current line is a image and the next line is a caption
                if "<img" in interestingLines[i] and "<figcaption>" in interestingLines[i+1]:
                    caption = interestingLines[i+1].replace("<figcaption>", "").replace("</figcaption>", "").strip()
                    #Put caption in the data-description of the image
                    imageLine = interestingLines[i]
                    imageLine = imageLine.replace(">", " data-description=\"" + caption + "\">")

                    #Replace the old line with the new line
                    lines[lines.index(interestingLines[i])] = imageLine

        with open(file, 'w', encoding="utf8") as f:
            f.writelines(lines)
            print("Annotated file: " + file)




                
        

                
