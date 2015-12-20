import sublime, sublime_plugin, datetime

class JernlnewentryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        def scrollToBottom():
            v = 0, self.view.layout_extent()[1]
            self.view.set_viewport_position(v)
        out = "\n";
        out = out + "**** ";
        out = out + datetime.date.today().strftime("%m/%d/%Y");
        out = out + " ********************************************************************************************************";
        out = out + "\n\n  > ";
        self.view.insert(edit, self.view.sel()[0].begin(), out);
        scrollToBottom()
