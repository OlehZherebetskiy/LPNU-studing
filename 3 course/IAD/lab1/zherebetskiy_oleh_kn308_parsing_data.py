import pandas as pnds #імпортуємо бібліотеку pandas для аналізу та заповнення структури DataFrame в pnds
import numpy as nmp   #імпортуємо бібліотеку numpy для зручних математичних перетворень
import matplotlib.pyplot as matplotlibPyplot #імпортуємо бібліотеку matplotlib а саме pyplot для побудови графіків в matplotlib_pyplot
import zherebetskiy_oleh_kn308_plot_module as plotModule

def parse(dataFrame):
    
    
        
    #додаємо .2019 для повної дати
    #міняємо назву колонки на day.month.year
    #переводимо запис дати в відповідний тип
    if 'day/month' in dataFrame.columns:
        dataFrame['day/month'] = dataFrame['day/month'] + '.2019'
        dataFrame = dataFrame.rename(columns={'day/month': 'day.month.year'})
        dataFrame['day.month.year'] = pnds.to_datetime(dataFrame['day.month.year']).dt.strftime('%d.%b.%Y')

    #робим індексацію по стовпцю дат
    if ('day.month.year' in dataFrame.columns) and (dataFrame.index.name != 'day.month.year'):
        dataFrame = dataFrame.set_index('day.month.year')
     
    #переводимо запис часу в відповідний тип
    if 'Time' in dataFrame.columns:
        dataFrame['Time'] = pnds.to_datetime(dataFrame['Time']).dt.strftime('%H:%M')
        
    dataFrame['Pressure'] = dataFrame['Pressure'].astype(float)
    
    #забираємо одиниці виміру від значень Humidity, Wind Speed, та Wind Gust
    for columnName in ['Humidity', 'Wind Speed', 'Wind Gust']:
        dataFrame[columnName] = dataFrame[columnName].str.extract(r'(\d+)')
    
    #переводимо запис значень Humidity, Wind Speed, та Wind Gust в відповідний тип
    dataFrame[['Humidity', 'Wind Speed', 'Wind Gust']] = dataFrame[['Humidity', 'Wind Speed', 'Wind Gust']].apply(pnds.to_numeric)
    
    #добавляємо одиниці виміру у назви колонок
    dataFrame = dataFrame.rename(columns={'Temperature': 'Temperature(F)', 'Dew Point': 'Dew Point(F)', 'Humidity': 'Humidity(%)', 
                            'Wind Speed': 'Wind Speed(mph)', 'Wind Gust': 'Wind Gust(mph)', 'Pressure': 'Pressure(inHg)',
                            'Precip.': 'Precip(mm)', 'Precip Accum': 'Precip Accum(kg/m2)'
                           })
    
    return dataFrame

dataFrame_weather = pnds.read_csv('DATABASE.csv', sep=';', decimal=',') #зчитуємо дані в структуру DataFrame; sep позначає, що колоки поділені знаком ";" 
dataFrame_weather = parse(dataFrame_weather) #парсимо дані які зчитали


plotModule.loop_draw(dataFrame_weather)#запуск циклічного меню по виводу графіків