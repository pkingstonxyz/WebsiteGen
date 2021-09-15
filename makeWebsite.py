from Page import Page
import os
from datetime import datetime

print("Building Website")

directory = "/home/Projects/pkingston/blog/pages/"

print("Making html")
# Turn md files into html
os.chdir(directory)
os.system("../scripts/compiledocs")

# Get list of pages
initial_pages = [Page(directory + i) for i in os.listdir(directory) if ".html" not in i]
pages = [i for i in initial_pages if "gem_" not in i.source]

# Sort list by date
pages.sort(key = lambda date: datetime.strptime(str(date), '%d/%m/%Y'))


print("Making blog indicies")
allPosts = []
allPosts.append("<ul>\n")
for page in pages:
    allPosts.append(page.listItem())
allPosts.append("</ul>\n")

recentPosts = []
pages.reverse()
for i in range(len(pages)):
    if i < 10:
        recentPosts.append(pages[i].timestampedlistItem())

postsByTag = []
tagList = []
for page in pages:
    for tag in page.tags:
        if tag not in tagList:
            tagList.append(tag)
for tag in tagList:
    postsByTag.append("<h3>" + tag + "</h3>\n<ul>")
    for page in pages:
        if tag in page.tags:
            postsByTag.append(page.listItemwithTags())
    postsByTag.append("</ul>")


template = open("/home/Projects/pkingston/blog/templates/blog.temp.html", 'r')
blog = open("/home/Projects/pkingston/blog/blog.html", 'w')

for line in template.readlines():
    if "{RECENT}" in line:
        blog.writelines(recentPosts)
    elif "{TAGS}" in line:
        blog.writelines(postsByTag)
    elif "{ALL}" in line:
        blog.writelines(allPosts)
    else:
        blog.write(line)

template.close()
blog.close()

os.system("uwebsite")
