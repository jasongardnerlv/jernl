import sublime, sublime_plugin, datetime, os, glob

class JernlCommand(sublime_plugin.TextCommand):

    tags = []
    tagsLines = []
    lineSummaryMap = []

    def run(self, edit):
        if (self.view.settings().get("jernl-dir") is None):
            sublime.error_message("User setting 'jernl-dir' not specified!")
            return
        self.tags = []
        self.tagsLines = []
        self.lineSummaryMap = []
        mainCommands = []
        if self.isJournalOpen():
            mainCommands.append("New Entry")
        else:
            mainCommands.append("Open Journal")
        mainCommands.append("Search")
        self.view.window().show_quick_panel(mainCommands, self.onCommandSelect)

    def isJournalOpen(self):
        return (self.view.file_name() is not None and self.view.file_name().endswith(".jernl"))

    def onCommandSelect(self, idx):
        if (idx == 0):
            if self.isJournalOpen():
                self.view.run_command("jernlnewentry")
            else:
                self.openJournal()
        elif (idx == 1):
            self.search()

    def openJournal(self):
        logdir = self.view.settings().get("jernl-dir")
        logdir = logdir if (logdir.endswith("/")) else logdir + "/"
        logfile = logdir + str(datetime.date.today().year) + ".jernl"
        newview = self.view.window().open_file(logfile)
        def scrollToBottom():
            if newview.is_loading():
                sublime.set_timeout(scrollToBottom, 100)
            else:
                v = 0, newview.layout_extent()[1]
                newview.set_viewport_position(v)
                # trying to use "newview.sel()" to set the cursor position, but it's not working reliably ?!
        scrollToBottom()

    def search(self):
        for filename in glob.glob(os.path.join(self.view.settings().get("jernl-dir"), '*.jernl')):
            with open(filename, encoding="utf-8") as f:
                linenum = 0
                for line in f:
                    words = line.split()
                    for word in words:
                        if word.startswith("@") and word.endswith("@"):
                            tagArr = word.replace("@", "").split(",")
                            for indtag in tagArr:
                                try:
                                    idx = self.tags.index(indtag)
                                except ValueError:
                                    idx = -1
                                if (idx < 0 and indtag != ""):
                                    self.tags.append(indtag)
                                taginfo = indtag,linenum,filename,line
                                self.tagsLines.append(taginfo);
                    linenum+=1
        self.tags.sort()
        sublime.set_timeout(lambda: self.view.window().show_quick_panel(self.tags, self.onSelectTag), 10)

    def onSelectTag(self, idx):
        if idx == -1:
            return
        lines = self.getTaglinesForTag(self.tags[idx])
        lineSummaries = []
        for line in lines:
            self.lineSummaryMap.append(line)
            lineSummaries.append(self.getLineSummary(line))
        sublime.set_timeout(lambda: self.view.window().show_quick_panel(lineSummaries, self.onSelectLine), 10)

    def onSelectLine(self, idx):
        if idx == -1:
            return
        selectedLine = self.lineSummaryMap[idx]
        view = self.view.window().open_file(selectedLine[2])
        def scrollToLine():
            if view.is_loading():
                sublime.set_timeout(scrollToLine, 100)
            else:
                pt = view.text_point(selectedLine[1]-1, 0)
                vector = view.text_to_layout(pt)
                view.set_viewport_position(vector)
        scrollToLine()

    def getTaglinesForTag(self, tag):
        lines = []
        for tagline in self.tagsLines:
            if (tagline[0] == tag):
                lines.append(tagline)
        return lines

    def getLineSummary(self, line):
        summ = line[3][:line[3].index("@")];
        if (len(summ) > 50):
            summ = summ[:50] + "..."
        return summ.replace("  > ", "")