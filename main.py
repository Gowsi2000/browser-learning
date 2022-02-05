from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

#Create The Main Window
class MainWindow(QMainWindow):

    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create QWebEngineView
        self.browser =QWebEngineView()

        # Set Default Browser URL
        self.browser.setUrl(QUrl("https://google.com"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        # Create A Status Bar
        self.status = QStatusBar()
        # Add status Bar To The Main Window
        self.setStatusBar(self.status)
        # Create QToolBar For Navigation
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        # Back Button
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        # Next Button
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to the next page")

        # Add Action To The Next Button
        # Go Forward
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # Reload Button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # Add Action To The Reload Button
        # Browser Reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        #Home Button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")

        # Add Action To The Home Button
        # Navigate to Home
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        #Separator
        navtb.addSeparator()

        # Line Edit For The URL
        self.urlbar = QLineEdit()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        # Stop Button
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # Show every buttons
        self.show()

    # Update The Title Of The Window
    def update_title(self, *__args):
        title = self.browser.page().title()
        self.setWindowTitle("% s  " % title)

    # Home Action
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    # Line Edit
    def navigate_to_url(self):
        a = QUrl(self.urlbar.text())

        if a.scheme() == "":
            a.setScheme("https")

        self.browser.setUrl(a)

    # Update URL
    def update_urlbar(self, a):
        self.urlbar.setText(a.toString())

        self.urlbar.setCursorPosition(0)

#Create Application
app = QApplication(sys.argv)

#Setting Name to Browser
app.setApplicationName("Browser")

#Create Window Object
window = MainWindow()

#Loop
app.exec_()






