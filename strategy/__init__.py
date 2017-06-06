import pymysql as psql
import GlobalLib.Genv as env
import pandas as pd
import stockstats as ss
import sys,traceback

db = psql.connect("localhost",env.g_dbUser , env.g_dbPWD, env.g_dbName)
try:
    cursor = db.cursor()
    sql = "select date,open_interest,close,high,low,open,volume from future_data  where contract='TX'  "
    df = pd.read_sql_query(sql,db)
    stock = ss.StockDataFrame.from_records(df)
    #stock = ss.StockDataFrame.retype(pd.read_csv('stock.csv'))
    #print(stock)
    stock.get('macd')
    #print(stock)
    stock.get('close_5_sma')
    #print(stock)

    merge = pd.concat([df,stock],axis=1,join='inner')
    #merge =pd.merge(df,stock,how='inner',on=['date','open_interest','close','high','low','open','volume'])
    print(merge)

except Exception as e:
    print(sys.exc_info())

# 关闭数据库连接
db.close()