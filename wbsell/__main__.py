#    _  _  ____  ____  ____  __    __   
#   / )( \(  _ \/ ___)(  __)(  )  (  )  
#   \ /\ / ) _ (\___ \ ) _) / (_/\/ (_/\
#   (_/\_)(____/(____/(____)\____/\____/
#        Licensed under GNU GPLv3
#                by Lao

#!/usr/bin/env python3

import os, sys, setproctitle
append_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(append_path)


from wbsell import NAME, VERSION, PATH
from wbsell.scripts.menu import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(NAME)
    app.setApplicationVersion(VERSION)
    QFontDatabase.addApplicationFont(PATH+'/Resources/Poppins-Regular.ttf')
    QFontDatabase.addApplicationFont(PATH+'/Resources/Poppins-Bold.ttf')
    setproctitle.setproctitle(NAME)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
