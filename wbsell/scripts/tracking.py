import requests, json, datetime
from fake_useragent import UserAgent
from wbsell import PATH
from wbsell.UI import ui_tracking
from PyQt6.QtWidgets import QDialog, QButtonGroup
from PyQt6.QtGui import QMovie


class TrackingWindow(QDialog):
    def __init__(self, parent):
        super(TrackingWindow, self).__init__(parent)
        self.UI = ui_tracking.Ui_Tracking()
        self.UI.setupUi(self)
        with open(PATH+'/UI/tracking.css', 'r', encoding='utf-8') as f:
            styles = f.read()
        if parent.db.check_userdata()[0] == 0:
            self.theme = styles.split('/* DARK */')[0].strip('\n')
            self.setStyleSheet(self.theme)
        else:
            self.theme = styles.split('/* DARK */')[1].strip('\n')
            self.setStyleSheet(self.theme)
        self.loading = QMovie(PATH+'Resources/images/loading.gif')
        self.UI.loadingLabel.setMovie(self.loading)
        self.loading.start()
        self.group = QButtonGroup(self)
        self.group.addButton(self.UI.ordersButton)
        self.group.addButton(self.UI.salesButton)
        self.group.addButton(self.UI.questionsButton)
        self.group.addButton(self.UI.feedbacksButton)
        self.headers = {'User-Agent':str(UserAgent().random)}
        self.headers['Authorization'] = parent.db.check_userdata()[3]
        self.stats_params = {'dateFrom':datetime.date.today(), 'flag':1}
        self.queandfeedb_params = {
            'isAnswered':False,
            'take':10,
            'skip':0
        }
        self.parent = parent
        self.connections()

    def connections(self):
        self.UI.beginButton.clicked.connect(self.track)

    def track(self):
        selectedButton = self.group.checkedId()
        if selectedButton == -2:
            self.track_orders()
        elif selectedButton == -3:
            self.track_sales()
        elif selectedButton == -4:
            self.track_questions()
        elif selectedButton == -5:
            self.track_feedbacks()

    def track_orders(self):
        self.loading.start()
        try:
            orders_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/orders'
            stock_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
            orders_response = requests.get(orders_url, headers=self.headers, params=self.stats_params)
            stock_response = requests.get(stock_url, headers=self.headers, params=self.stats_params)
            if orders_response.status_code == 401:
                self.UI.output.setText('Некорректный API-ключ.')
                return False
            else:
                loaded_orders_response = json.loads(orders_response.text)
                loaded_stock_response = json.loads(stock_response.text)
                self.UI.output.setText(str(loaded_orders_response), str(loaded_stock_response))
                return True
        except Exception as e:
            self.UI.output.setText(str(e))
            return False

    def track_sales(self):
        try:
            sales_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/sales'
            stock_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
            sales_response = requests.get(sales_url, headers=self.headers, params=self.stats_params)
            stock_response = requests.get(stock_url, headers=self.headers, params=self.stats_params)
            if sales_response.status_code == 401:
                self.UI.output.setText('Некорректный API-ключ.')
                return False
            else:
                loaded_sales_response = json.loads(sales_response.text)
                loaded_stock_response = json.loads(stock_response.text)
                self.UI.output.setText(str(loaded_sales_response), str(loaded_stock_response))
                return True
        except Exception as e:
            self.UI.output.setText(str(e))
            return False

    def track_questions(self):
        try:
            questions_url = 'https://feedbacks-api.wildberries.ru/api/v1/questions'
            questions_response = requests.get(questions_url, headers=self.headers, params=self.queandfeedb_params)
            if questions_response.status_code == 401:
                self.UI.output.setText('Некорректный API-ключ.')
                return False
            else:
                loaded_questions_response = json.loads(questions_response.text)
                self.UI.output.setText(str(loaded_questions_response))
                return True
        except Exception as e:
            self.UI.output.setText(str(e))
            return False

    def track_feedbacks(self):
        try:
            feedbacks_url = 'https://feedbacks-api.wildberries.ru/api/v1/feedbacks'
            feedbacks_response = requests.get(feedbacks_url, headers=self.headers, params=self.queandfeedb_params)
            if feedbacks_response.status_code == 401:
                self.UI.output.setText('Некорректный API-ключ.')
                return False
            else:
                loaded_feedbacks_response = json.loads(feedbacks_response.text)
                self.UI.output.setText(str(loaded_feedbacks_response))
                return True
        except Exception as e:
            self.UI.output.setText(str(e))
            return False
