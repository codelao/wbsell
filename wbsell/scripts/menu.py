import webbrowser, requests, json, sys, subprocess, string, pyperclip
from wbsell import PATH, VERSION, FEEDBACK
from wbsell.UI import ui_menu
from wbsell.scripts.tracking import TrackingWindow
from wbsell.scripts.dbase import Database
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QMessageBox
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = Database(PATH+'/Resources/config.db')
        self.UI = ui_menu.Ui_MainWindow()
        self.UI.setupUi(self)
        with open(PATH+'/UI/menu.css', 'r', encoding='utf-8') as f:
            styles = f.read()
        if self.db.check_userdata()[0] == 0:
            self.theme = styles.split('/* DARK */')[0].strip('\n')
            self.setStyleSheet(self.theme)
        else:
            self.theme = styles.split('/* DARK */')[1].strip('\n')
            self.setStyleSheet(self.theme)
        self.UI.nameLabel.setText('wbsell v'+VERSION)
        self.UI.wrongkeyLabel.hide()
        self.UI.connectionLabel.hide()
        self.UI.collapseFrame.hide()
        self.hidden = [self.UI.settingsFrame, self.UI.collapseButton, 
                       self.UI.settingsLabel, self.UI.keyLabel, self.UI.key, self.UI.themeLabel,
                       self.UI.logsLabel, self.UI.theme, self.UI.logsBox, self.UI.dateLabel,
                       self.UI.date]
        for element in self.hidden:
            element.hide()
        self.connections()

    def check_connection(self):
        try:
            requests.get('https://google.com', timeout=1)
            self.UI.connectionLabel.hide()
        except:
            self.UI.trackingButton.setEnabled(False)

    def check_latest_release(self):
        headers = {'Accept': 'application/vnd.github+json'}
        check_latest_release = requests.get('https://api.github.com/repos/codelao/PocketTRC20/releases/latest', headers=headers)
        if check_latest_release.status_code == 200:
            latest_release = json.loads(check_latest_release.text)
            if not latest_release['tag_name'] == 'v'+VERSION:
                return latest_release['tag_name']

    def connections(self):
        self.UI.trackingButton.clicked.connect(self.openTracking)
        self.UI.settingsButton.clicked.connect(self.openSettings)
        self.UI.notificationsButton.clicked.connect(self.notifications)
        self.UI.reloadstatsButton.clicked.connect(self.tabReload) and self.UI.reloadlogsButton.clicked.connect(self.tabReload)
        self.UI.Wiki.triggered.connect(self.windowMenu) and self.UI.report_a_bug.triggered.connect(self.windowMenu) and self.UI.feedback.triggered.connect(self.windowMenu)

    def openTracking(self):
        self.tracking = TrackingWindow(parent=self)
        self.tracking.show()

    def openSettings(self):
        self.settings = SettingsWindow(parent=self)
        self.settings.show()

    def notifications(self):
        popup = QMessageBox(self)
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setWindowTitle('wbsell')
        popup.setText('Функция в разработке...')
        popup.setDetailedText('В скором времени будет добавлена возможность получения уведомлений при появлении бесплатных окон для отгрузки на выбранном складе.')
        popup.addButton(QMessageBox.StandardButton.Ok)
        popup.move(400, 300)
        popup.exec()

    def tabReload(self):
        with open(PATH+'/Resources/logs.json', 'r', encoding='utf-8') as l:
            logs = l.read()
            handle = json.loads(logs)
            for log in range(len(handle)):
                self.UI.logs.setText(self.UI.logs.toPlainText()+handle[log]['date']+'    '+handle[log]['message']+'\n')

    def windowMenu(self):
        if self.sender() == self.UI.Wiki:
            webbrowser.open('https://github.com/codelao/wbsell/wiki')
        elif self.sender() == self.UI.report_a_bug:
            webbrowser.open('https://github.com/codelao/wbsell/issues')
        elif self.sender() == self.UI.feedback:
            pyperclip.copy(FEEDBACK)
            popup = QMessageBox(self)
            popup.setIcon(QMessageBox.Icon.Information)
            popup.setWindowTitle('wbsell')
            popup.setText('Почта для связи скопирована в буфер обмена.')
            popup.addButton(QMessageBox.StandardButton.Ok)
            popup.move(400, 300)
            popup.exec()


class SettingsWindow(QWidget):
    def __init__(self, parent):
        super(SettingsWindow, self).__init__(parent)
        if parent.db.check_userdata()[0] == 0:
            parent.UI.theme.setCurrentIndex(0)
        else:
            parent.UI.theme.setCurrentIndex(1)
        parent.UI.date.setText(parent.db.check_userdata()[4])
        parent.UI.key.setText(parent.db.check_userdata()[3])
        self.allowed = string.ascii_letters+string.digits+'._'
        for element in parent.hidden:
            element.show()
        self.parent = parent
        self.connections()

    def connections(self):
        self.parent.UI.collapseButton.clicked.connect(self.updateSetts)

    def updateSetts(self):
        userdata = self.parent.db.check_userdata()
        theme = self.parent.UI.theme.currentIndex()
        logs = self.parent.UI.logsBox.currentIndex()
        api_key = str(self.parent.UI.key.text())
        if not userdata[3] == api_key:
            for symbol in api_key:
                if not symbol in self.allowed:
                    self.parent.UI.wrongkeyFrame.show()
                    return False
            self.parent.UI.wrongkeyLabel.hide()
        if theme != self.parent.db.check_userdata()[0]:
            self.parent.db.edit_userdata(theme=theme, logs=logs, api_key=api_key)
            QApplication.exit(0)
            subprocess.Popen([sys.executable] + sys.argv)
        else:
            self.parent.db.edit_userdata(theme=theme, logs=logs, api_key=api_key)
            for element in self.parent.hidden:
                element.hide()
