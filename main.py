from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser =QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)

        back_btn.setStatusTip("Back to previous page")

        back_btn.triggered.connect(self.browser.back)

        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to the next page")

        next_btn.triggered.connect(self.browser.forward)

        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        reload_btn.triggered.connect(self.browser.reload)

        navtb.addAction(reload_btn)

        #Home Button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        #Separator
        navtb.addSeparator()

        self.urlbar = QLineEdit()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.show()
    def update_title(self, *__args):
        title = self.browser.page().title()
        self.setWindowTitle("% s  " % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        a = QUrl(self.urlbar.text())

        if a.scheme() == "":
            a.setScheme("https")

        self.browser.setUrl(a)

    def update_urlbar(self, a):
        self.urlbar.setText(a.toString())

        self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)

app.setApplicationName("Browser")

window = MainWindow()

app.exec_()






