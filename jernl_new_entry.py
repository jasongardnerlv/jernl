import sublime, sublime_plugin, datetime

class JernlnewentryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        def scrollToBottom():
            v = 0, self.view.layout_extent()[1]
            self.view.set_viewport_position(v)
        dateFormat = "%d/%m/%Y";
        if (self.view.settings().get("jernl-date-format") is not None):
            dateFormat = self.view.settings().get("jernl-date-format");
        out = "\n";
        out = out + "**** ";
        out = out + datetime.date.today().strftime(dateFormat);
        out = out + " ********************************************************************************************************";
        out = out + "\n\n  > ";
        self.view.insert(edit, self.view.sel()[0].begin(), out);
        scrollToBottom()
