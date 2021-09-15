from Gem import Gem
import os
from datetime import datetime

print("Building Gemini Capsule")

directory = "/home/Projects/pkingston/blog/pages/"

# Get list of gems
gems = [Gem(directory + i) for i in os.listdir(directory) if ".md" in i]

print("Converting md to gmi")
# Convert md to gmi
for gem in gems:
    gem.toGem()

# Sort list by date
gems.sort(key = lambda date: datetime.strptime(str(date), '%d/%m/%Y'))
gems.reverse()

final = open("/home/Projects/pkingston/gemini/index.gmi", "w")
initial = open("/home/Projects/pkingston/gemini/initial", "r")

final.writelines(initial.readlines())

initial.close()

final.write("# Diary\n")

for gem in gems:
    if "gem_" in gem.source:
        final.write("=> " + gem.source[:-2] + "gmi " + gem.date + " " + gem.title)
        final.write("\n")
        final.write("\n")

final.write("# Blog page mirrors\n")

print("Making index")
for gem in gems:
    if "gem_" not in gem.source:
        final.write("=> " + gem.source[:-2] + "gmi " + gem.date + " " + gem.title)
        final.write("\n")
        final.write("\n")
final.close()
