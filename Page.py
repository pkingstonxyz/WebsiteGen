class Page:
    def __init__(self, file):
        page = open(file, 'r')
        self.source = file[:-2] + "html"
        self.source = self.source[24:]
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
    def listItem(self):
        out = "<a href=\"" + self.source + "\">" + "<li class=\"indexItem\">" + self.title + "</li></a>\n"
        return out
    def timestampedlistItem(self):
        date = self.date
        out = "<a href=\"" + self.source + "\">" + "<li class=\"indexItem\">" + self.date + " - " + self.title + "</li></a>\n"
        return out
    def listItemwithTags(self):
        tags = str(self.tags)[1:-1].replace("\'", "")
        out = "<a href=\"" + self.source + "\">" + "<li class=\"indexItem\">" + self.title +  " - " + tags + "</li></a>\n"
        return out

