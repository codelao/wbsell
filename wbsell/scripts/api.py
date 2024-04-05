import requests, json, datetime
from wbsell import PATH
from wbsell.scripts.dbase import Database
from fake_useragent import UserAgent


db = Database(PATH+'/Resources/config.db')
headers = {'User-Agent':str(UserAgent().random)}
headers['Authorization'] = db.check_userdata()[3]
orders_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/orders'
sales_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/sales'
stock_url = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
questions_url = 'https://feedbacks-api.wildberries.ru/api/v1/questions'
feedbacks_url = 'https://feedbacks-api.wildberries.ru/api/v1/feedbacks'
date = datetime.date.today()
year = date.year
month = date.month
day = date.day
param_date = str(year)+'-'+str(month)+'-'+str(day)
stats_params = {'dateFrom':param_date, 'flag':1}
queandfeedb_params = {
    'isAnswered':False,
    'take':10,
    'skip':0
}

async def orders():
    try:
        orders_response = requests.get(orders_url, headers=headers, params=stats_params)
        stock_response = requests.get(stock_url, headers=headers, params=stats_params)
        if orders_response.status_code == 401:
            return 'Некорректный API-ключ.'
        else:
            loaded_orders_response = json.loads(orders_response.text)
            loaded_stock_response = json.loads(stock_response.text)
            return loaded_orders_response, loaded_stock_response
        '''
        order = loaded_orders_response[user[6]+i]
        income = db.get_order_income(user_id=user[0]) + order['totalPrice']
        db.add_order_income(orders_income=income, user_id=user[0])
        order_date = order['date'].replace('T', ' ')
        bot.send_message(chat_id=user[0], text='_'+order_date+
            '_\n🛒 *Заказ ['+str((user[6]+i+1))+']: '+str(order['totalPrice'])+'*₽'+
            '\n📈 Сегодня: '+str(len(loaded_orders_response))+' на '+str(income)+'₽'+
            '\n🆔 Арт: '+str(order['supplierArticle'])+
            '\n📁 '+order['subject']+
            '\n🏷 '+order['brand']+
            '\n🧳 Комиссия базовая: *'+str(order['totalPrice']*0.23)+'*₽ (23%)'+
            '\n🌐 '+order['warehouseName']+' → '+order['oblast']+': *77*₽'+
            '\n📦 *'+str(loaded_stock_response[-1]['quantity'])+' шт.*', parse_mode='Markdown')
        '''
    except Exception as e:
        return e

async def sales():
    try:
        sales_response = requests.get(sales_url, headers=headers, params=stats_params)
        stock_response = requests.get(stock_url, headers=headers, params=stats_params)
        if sales_response.status_code == 401:
            return 'Некорректный API-ключ.'
        else:
            loaded_sales_response = json.loads(sales_response.text)
            loaded_stock_response = json.loads(stock_response.text)
            return loaded_sales_response, loaded_stock_response
            '''
            sale = loaded_sales_response[user[7]+i]
            income = db.get_sale_income(user_id=user[0]) + sale['totalPrice']
            db.add_sale_income(sales_income=income, user_id=user[0])
            sale_date = sale['date'].replace('T', ' ')
            bot.send_message(chat_id=user[0], text='_'+sale_date+
                '_\n✅ *Выкуп ['+str((user[7]+i+1))+']: '+str(sale['totalPrice'])+'*₽'+
                '\n📈 Сегодня: '+str(len(loaded_sales_response))+' на '+str(income)+'₽'+
                '\n🆔 Арт: '+str(sale['supplierArticle'])+
                '\n📁 '+sale['subject']+
                '\n🏷 '+sale['brand']+
                '\n🧳 Комиссия (базовая): *23%*'+
                '\n🌐 '+sale['warehouseName']+' → '+sale['regionName']+
                '\n🚛 В пути до клиента: '+str(loaded_stock_response[-1]['inWayToClient'])+
                '\n🚚 В пути от клиента: '+str(loaded_stock_response[-1]['inWayFromClient'])+
                '\n📦 *'+str(loaded_stock_response[-1]['quantity'])+' шт.*', parse_mode='Markdown')
            '''
    except Exception as e:
        return e

async def questions():
    try:
        questions_response = requests.get(questions_url, headers=headers, params=queandfeedb_params)
        if questions_response.status_code == 401:
            return 'Некорректный API-ключ.'
        loaded_questions_response = json.loads(questions_response.text)
        return loaded_questions_response
        '''
        question_msg = loaded_questions_response['data']['questions'][q]['text']
        ai_question_response = get_ai_response(msg=question_msg)
        question_id = loaded_questions_response['data']['questions'][q]['id']
        btn.QuestionsReplyMenu = InlineKeyboardMarkup()
        Reply = InlineKeyboardButton(text='Ответить на вопрос', callback_data=question_id)
        btn.QuestionsReplyMenu.add(Reply)
        bot.send_message(chat_id=user[0], text='*Получен новый вопрос:*\n'+question_msg+'\n*Товар:*\n'+loaded_questions_response['data']['questions'][q]['productDetails']['productName']+'\n*Сгенерированный ответ ИИ:*\n`'+ai_question_response+'`', parse_mode='Markdown', reply_markup=btn.QuestionsReplyMenu)
        '''
    except Exception as e:
        return e

async def feedbacks():
    try:
        feedbacks_response = requests.get(feedbacks_url, headers=headers, params=queandfeedb_params)
        loaded_feedbacks_response = json.loads(feedbacks_response.text)
        return loaded_feedbacks_response
        '''
        feedback_msg = loaded_feedbacks_response['data']['feedbacks'][f]['text']
        ai_feedback_response = get_ai_response(msg=feedback_msg)
        feedback_id = loaded_feedbacks_response['data']['feedbacks'][f]['id']
        btn.FeedbacksReplyMenu = InlineKeyboardMarkup()
        Reply = InlineKeyboardButton(text='Ответить на отзыв', callback_data=feedback_id)
        btn.FeedbacksReplyMenu.add(Reply)
        bot.send_message(chat_id=user[0], text='*Получен новый отзыв:*\n'+feedback_msg+'\n*Товар:*\n'+loaded_feedbacks_response['data']['feedbacks'][f]['productDetails']['productName']+'\n*Сгенерированный ответ ИИ:*\n`'+ai_feedback_response+'`', parse_mode='Markdown', reply_markup=btn.FeedbacksReplyMenu)
        await asyncio.sleep(300)
        '''
    except Exception as e:
        return e
