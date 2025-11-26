"""Module allowing for `python -m kevinbotlib_theme.widget_gallery`."""
import sys

import kevinbotlib_theme
from kevinbotlib_theme.qtpy.QtWidgets import QApplication
from kevinbotlib_theme.widget_gallery.main_window import WidgetGallery

if __name__ == "__main__":
    kevinbotlib_theme.enable_hi_dpi()
    app = QApplication(sys.argv)
    kevinbotlib_theme.setup_theme("auto")
    win = WidgetGallery()
    win.show()
    app.exec()
