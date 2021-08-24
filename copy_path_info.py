import sublime, sublime_plugin
from os.path import relpath
import os

class CopyRelativePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if len(filename) > 0:
            # Copy shortest relpath for file compared to open folders
            sublime.set_clipboard(
                min(
                    (
                        relpath(filename, folder)
                        for folder in sublime.active_window().folders()
                    ),
                    key=len,
                )
            )
            sublime.status_message("Copied relative path")

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)

class CopyFileNameOnlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if len(filename) > 0:
            sublime.set_clipboard(filename.split('/')[-1])
            sublime.status_message("Copied File Name")

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)

class CopyGitPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        filename = os.path.splitdrive(filename)[1]
        filename = filename.replace('\\', '/')
        if len(filename) > 0:
            repo_name = self.get_repo_name(filename)
            if repo_name is not None and repo_name in filename:
                idx = filename.rfind(repo_name)
                if idx > 0:
                    idx += len(repo_name) + 1
                    filename = filename[idx:]
            else:
                filename = relpath(filename)
            sublime.set_clipboard(filename)
            sublime.status_message("Copied relative path")

    def get_repo_name(self, filename):
        parent_dirname = os.path.dirname(filename)
        if parent_dirname is "/":
            return None
        else:
            for item in os.listdir(parent_dirname):
                if item == ".git":
                    return parent_dirname[parent_dirname.rfind('/') + 1:]
            return self.get_repo_name(parent_dirname)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)
