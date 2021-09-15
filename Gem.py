import re
import pyfiglet

class Gem:
    def __init__(self, file):
        page = open(file, 'r')
        self.file = file
        self.source = file
        self.source = self.source[30:]
        for line in page.readlines():
            if "tags: " in line:
                tags = line[5:].split(',')
                self.tags = [i.strip() for i in tags]
            elif "title: " in line:
                self.title = line[6:].strip()
            elif "date: " in line:
                self.date = line[5:].strip()
    def __repr__(self):
        return self.date
    def toGem(self):
        markdown = open(self.file, 'r')
        gem = open("/home/Projects/pkingston/gemini" + "/" + self.source[:-2] + "gmi", 'w')
        titleheading = pyfiglet.figlet_format(self.title)
        dateline = "Written on: " + self.date
        gem.write("```")
        gem.write("\n")
        gem.write(titleheading)
        gem.write("\n")
        gem.write("```")
        gem.write("\n")
        gem.write(dateline)

        for line in markdown.readlines():
            if "---" in line:
                pass
            elif "title: " in line:
                pass
            elif "date: " in line:
                pass
            elif "tags: " in line:
                pass
            else:
                if re.search("\[.*\](.*)", line):
                    text = re.search("\[.*\]", line).group()[1:-1]
                    link = re.search("\(.*\)", line).group()[1:-1]
                    if ".html" in link and "http" not in link:
                        link = link[:-4] + "gmi"
                    out = re.sub("\[.*\](.*)", text, str(line))
                    gem.write(out)
                    gem.write("=> " + link + " " + text)
                else:
                    gem.write(line)
        gem.close()
