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

def isSelectionEmbeded(selection):
    for region in selection:
        print region

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
        current_window = self.view.window()

        active_view      = current_window.active_view()
        active_file_path = active_view.file_name()
        active_file_name = os.path.basename(active_file_path)

        # Figure out if what the user has selected is text to embed
        # or if it is already embeded and can be stripped
        current_selection = active_view.sel()
        is_embeded        = isSelectionEmbeded(current_selection)


