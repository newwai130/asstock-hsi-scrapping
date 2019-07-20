import configparser
from lib.webHandler.AsstockWebHandler import *
 
config = configparser   .ConfigParser()
config.read('config/Config.ini')

asstockWebHandler = AsstockWebHandler()
firstMonthResponse = asstockWebHandler.getHsiData(config.get('common', 'asstock.hsi.link.month.first'))
secondMonthResponse = asstockWebHandler.getHsiData(config.get('common', 'asstock.hsi.link.month.second'))


with open("output.txt", "a") as text_file:
    text_file.write(firstMonthResponse.toJson() +"\n")
    text_file.write(secondMonthResponse.toJson() +"\n")
    print("write successfully")
