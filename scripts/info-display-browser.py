#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import argparse
import logging


class WebPage(QWebPage):
    def javaScriptConsoleMessage(self, *args, **kwargs):
        print(args, kwargs)

        super().javaScriptConsoleMessage(*args, **kwargs)


def run_browser(url):
    app = QApplication(['info-display'])
    browser = QWebView()
    page = WebPage()
    browser.setPage(page)
    browser.load(QUrl(url))
    browser.show()

    app.exec()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(type=str, dest='url', nargs='?',
                            default='http://localhost:8080/main-screen/')

    args = arg_parser.parse_args()

    run_browser(args.url)
