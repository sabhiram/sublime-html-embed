#!/usr/bin/env python

import sublime
import sublime_plugin

import sys, os, re


"""
Python 2 vs Python 3 - Compatibility - reduce() is functools.reduce
"""
try:
    # Python 2
    _reduce = reduce
except NameError:
    # Python 3
    import functools
    _reduce = functools.reduce


"""
Fetch sublime version
"""
version = sublime.version()


"""
Helper functions
"""
def insertTextToView(view, text):
    view.run_command("append", {"characters": text})

def isSelectionEmbeded(selected_text):
    RE_is_embed = re.compile(r"^\s*?\".*\"(,|)$")
    lines       = selected_text.split("\n")
    for line in lines:
        match = RE_is_embed.match(line)
        if not match:
            return False
    return True

"""
Sublime commands that this plugin implements
"""
class ToggleHtmlEmbedCommand(sublime_plugin.TextCommand):
    """
    Command to embed / un-embed HTML
    """
    def run(self, edit):
        """
        """
        current_window   = self.view.window()
        active_file_path = self.view.file_name()

        # Figure out if what the user has selected is text to embed
        # or if it is already embeded and can be stripped
        current_selection = self.view.sel()
        if len(current_selection) != 1:
            print("HTML Embed: Only single selections are permitted.")
            return

        region        = current_selection[0]
        selection_txt = self.view.substr(region)
        output_txt    = None

        if isSelectionEmbeded(selection_txt):
            print("HTML Embed: Embedded Selection")
            output_txt = self.un_embed_selection(selection_txt)
        else:
            print("HTML Embed: Normal Selection")
            output_txt = self.embed_selection(selection_txt)

        if output_txt:
            self.view.replace(edit, region, output_txt)


    def un_embed_selection(self, txt):
        """
        """
        out_lines = [re.sub(r"^(\s*)\"(.*)\"(,|)$", r"\1\2", l) for l in txt.split("\n")]
        return "\n".join(out_lines)


    def embed_selection(self, txt):
        """
        """
        out_lines = ["\"" + l + "\"," for l in txt.split("\n")]
        return "\n".join(out_lines)
