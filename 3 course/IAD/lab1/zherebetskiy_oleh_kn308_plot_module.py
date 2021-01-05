import pandas as pnds #імпортуємо бібліотеку pandas для аналізу та заповнення структури DataFrame в pnds
import numpy as nmp   #імпортуємо бібліотеку numpy для зручних математичних перетворень
import plotly.graph_objects as plotlyGraphObject
import plotly
import plotly.express as plotlyExpress
from plotly.subplots import make_subplots

def loop_draw(dataFrame):
    comand = ''

    while comand != 'exit':
        comand = ''
        
        #чекаємо на введення кількості графіків
        #якщо exit то завершуємо виконання функції
        print('\n\n\n\nВведіть кількість графіків (exit - щоб вийти):')
        comand = str(input())
        if comand == 'exit':
            return
        numPlots = int(comand) #переводимо в правильний тип розмірність графіка
        
        
        dimension = []
        typeNum = []
        specs = []
        titles = []
        dataPlot = []
        func = []
        
        
        for num in range(numPlots):
            
            
            #чекаємо на введення розмірності графіка
            #якщо exit то завершуємо виконання функції
            comand = ''
            while comand not in ['1','2','exit']:
                if comand != '':
                    print('ви ввели не коректні дані!!!')
                print('\nВведіть розмірність графіка №'+str(num)+' (1-2) (exit - щоб вийти):')
                comand = str(input())
                if comand == 'exit':
                    return
            dimension.append(int(comand)) #переводимо в правильний тип розмірність графіка


            
            #чекаємо на введення типу графіка
            #якщо exit то завершуємо виконання функції
            comand = ''
            while (comand not in ['1','2','3','4','5','exit']) :
                if comand != '':
                    print('\n\nви ввели не коректні дані!!!\n\n')
                print('\nВведіть тип графіка №'+str(num))
                
                if dimension[num] == 1 :
                    print('1) Box Plot')   
                if dimension[num] == 2 :
                    print('2) Scatter Plot')
                    print('3) Line Plot')
                    print('4) Bar Plot')
                    print('5) Pie Plot')
                
                print('(exit - щоб вийти):')
                comand = str(input())
                if comand == 'exit':
                    return
            typeNum.append(int(comand)) #переводимо в число тип графіка
            
            
            #задаємо title для графіків
            if comand == '1':
                titles.append("Тип графіка Box Plot")
            elif comand == '2':
                titles.append("Тип графіка Scatter Plot")    
            elif comand == '3':
                titles.append("Тип графіка Line Plot")    
            elif comand == '4':
                titles.append("Тип графіка Bar Plot")    
            elif comand == '5':
                titles.append("Тип графіка Pie Plot")    

            
            #для кожного типу свої параметри для specs
            #та різні доступні усереднення
            #наприклад для лінійного немає сенсу виводити дані без усередення
            
            if typeNum[num]==1 :
                func.append('')
                specs.append({})
            elif typeNum[num]==2:
                comand = ''
                while comand not in ['0','1','2','3','4','5']:
                    if comand != '':
                        print('ви ввели не коректні дані!!!')
                    print('\nВведіть (0-5):\n0)all\n1)count\n2)mean\n3)max\n4)min\n5)median')
                    comand = str(input())
                func.append(comand)
                specs.append({'type': 'scatter'})
            elif typeNum[num]==3:
                comand = ''
                while comand not in ['1','2','3','4','5']:
                    if comand != '':
                        print('ви ввели не коректні дані!!!')
                    print('\nВведіть (1-5):\n1)count\n2)mean\n3)max\n4)min\n5)median')
                    comand = str(input())
                func.append(comand)
                specs.append({})
            elif typeNum[num]==4:
                comand = ''
                while comand not in ['0','1','2','3','4','5']:
                    if comand != '':
                        print('ви ввели не коректні дані!!!')
                    print('\nВведіть (0-5):\n0)all\n1)count\n2)mean\n3)max\n4)min\n5)median')
                    comand = str(input())
                func.append(comand)
                specs.append({})
            elif typeNum[num]==5:
                func.append('')
                specs.append({'type': 'domain'})
                
                
            #Збераємо всі дані в структуру dataPlot
            dataPlot.append(dataSelect(dataFrame, dimension[num], typeNum[num], func[num]))
        
        
        
        
        #Усі графіки будуть виводитись в одну стрічку
        numRows = 1
        
        #Створюєм, так би мовити, сітку для графіків
        fig = make_subplots (rows=numRows, cols=numPlots, specs=[specs], subplot_titles=titles)
        
        #Будуємо усі графіки
        for num in range(numPlots):
            buildPlot(typeNum[num], fig, dimension[num], dataFrame, dataPlot[num], func[num], num+1, numRows)
            
        #Додаєм розміри для графіків і title для всього листа
        fig.update_layout(
            title_text='Жеребецький Олег Лаб1',
            height=600,
            width=600*numPlots
        )
        #Будемо показувати легенду
        fig.update_layout(showlegend=True)
        
        #Будемо зберігати і виводити графіки в html для зручності 
        plotly.offline.plot(fig, auto_open=True)

        
        
        
#вибір функції графіка який будується
def buildPlot(typeNum, fig, dimension, dataFrame, dataPlot, func, col, row):
    {
        1: boxPlot,
        2: scatterPlot,
        3: linePlot,
        4: barPlot,
        5: piePlot
    }[typeNum](fig, dimension, dataFrame, dataPlot, func, col, row)


def inputColumnName(columns, num):
    name = ''
    while name not in columns :
            if name != '':
                print('\n\n\nви ввели не коректні дані!!!\n\n\n')
            print('\nВведіть один з стовпців даних для осі '+str(num)+':')
            print(*columns, sep=" , ")
            name = str(input())
    return name

def removeNotNum(columns):
    columns.remove('Time')
    columns.remove('Wind')
    columns.remove('Condition')
    return columns
    
def addNotNum(columns):
    columns.append('Time')
    columns.append('Wind')
    columns.append('Condition')
    return columns
            
    

#підготовка даних до побудови графіка
def dataSelect(dataFrame, dimension, typeNum, funcNum):
    dataPlot = []
    
    # для count потрібно тільки одну колонку а друга це індекс або час, якщо перша і є індексом 
    if dimension == 2 and funcNum=="1":   
        columns = dataFrame.columns.tolist()
        columns.append('day.month.year')
        name = inputColumnName(columns,1)
        
        if name != 'day.month.year':
            dataPlot.append(dataFrame[name])
            print(dataFrame[name])
            dataPlot.append(dataFrame.index)
        else:
            dataPlot.append(dataFrame.index)
            print(dataFrame['Time'])
            dataPlot.append(dataFrame['Time'])
            
    # для типу pie перше має бути цифровим значенням а друге по чому групувати може бути будь чим        
    elif dimension ==2 and typeNum==5:
        columns = dataFrame.columns.tolist()
        #видаляємо не чисельні значення
        columns = removeNotNum(columns)
        
        name = inputColumnName(columns,1)
        dataPlot.append(dataFrame[name])

        #додаємо назад не чисельні значення
        columns = addNotNum(columns)
        columns.append('day.month.year')

        columns.remove(name)
        
        name = inputColumnName(columns,2)
        
        if name != 'day.month.year':
            dataPlot.append(dataFrame[name])
        else:
            dataPlot.append(dataFrame.index)
            
    #для будь яких графіків з функцією не all або стовпчикова для all
    #для першого можна будьякий тип а для другого треба тільки число
    elif (dimension ==2 and funcNum!="0") or (dimension ==2 and typeNum==4 and funcNum=="0"):
        columns = dataFrame.columns.tolist()
        columns.append('day.month.year')
        
        name = inputColumnName(columns,1)
        
        if name != 'day.month.year':
            dataPlot.append(dataFrame[name])
        else:
            dataPlot.append(dataFrame.index)

        #видаляємо не чисельні значення
        columns = removeNotNum(columns)
        columns.remove('day.month.year')
        
        if name not in ['Time', 'Wind', 'Condition','day.month.year']:
            columns.remove(name)
            
        name = inputColumnName(columns,2)
        
        dataPlot.append(dataFrame[name])
        
    #для всього решта
    else:
        columns = dataFrame.columns.tolist()
        columns.append('day.month.year')
        for num in range(dimension):
            name = inputColumnName(columns,num)
            
            columns.remove(name)
            
            if name != 'day.month.year':
                dataPlot.append(dataFrame[name])
            else:
                dataPlot.append(dataFrame.index)
                
    return dataPlot
      
    
    
    
def scatterPlot (fig, dimension, dataFrame, dataPlot, func, col, row):
        data = pnds.DataFrame({dataPlot[0].name: dataPlot[0], dataPlot[1].name:dataPlot[1]})
        data.reset_index(drop=True, inplace=True)
        
        if func == '0':
            data = data.set_index(dataPlot[0].name)
            df = plotlyExpress.scatter(data)
            df['data'][0].name = dataPlot[1].name+" /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name, row=row, col=col)
        elif func == '1':
            data = data.groupby([dataPlot[0].name]).count()
            df = plotlyExpress.scatter(data)
            df['data'][0].name = "count "+dataPlot[0].name
            fig = fig.update_yaxes(title_text= "count", row=row, col=col)
        elif func == '2':
            data = data.groupby([dataPlot[0].name]).mean()
            df = plotlyExpress.scatter(data)
            df['data'][0].name = dataPlot[1].name+" mean /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" mean", row=row, col=col)
        elif func == '3':
            data = data.groupby([dataPlot[0].name]).max()
            df = plotlyExpress.scatter(data)
            df['data'][0].name = dataPlot[1].name+" max /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" max", row=row, col=col)
        elif func == '4':
            data = data.groupby([dataPlot[0].name]).min()
            df = plotlyExpress.scatter(data)
            df['data'][0].name = dataPlot[1].name+" min /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" min", row=row, col=col)
        elif func == '5':
            data = data.groupby([dataPlot[0].name]).median()
            df = plotlyExpress.scatter(data)
            df['data'][0].name = dataPlot[1].name+" median /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" median", row=row, col=col)
            
        
            
        df['data'][0].showlegend = True
        fig = fig.add_trace(df['data'][0], row=row, col=col)
        fig = fig.update_xaxes(title_text= dataPlot[0].name, row=row, col=col)

        
def linePlot (fig, dimension, dataFrame, dataPlot, func, col, row):
        data = pnds.DataFrame({dataPlot[0].name: dataPlot[0], dataPlot[1].name:dataPlot[1]})
        data.reset_index(drop=True, inplace=True)
        
        if func == '1':
            data = data.groupby([dataPlot[0].name]).count()
            df = plotlyExpress.line(data)
            df['data'][0].name = "count "+dataPlot[0].name
            fig = fig.update_yaxes(title_text= "count", row=row, col=col)
        elif func == '2':
            data = data.groupby([dataPlot[0].name]).mean()
            df = plotlyExpress.line(data)
            df['data'][0].name = dataPlot[1].name+" mean /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" mean", row=row, col=col)
        elif func == '3':
            data = data.groupby([dataPlot[0].name]).max()
            df = plotlyExpress.line(data)
            df['data'][0].name = dataPlot[1].name+" max /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" max", row=row, col=col)
        elif func == '4':
            data = data.groupby([dataPlot[0].name]).mean()
            df = plotlyExpress.line(data)
            df['data'][0].name = dataPlot[1].name+" min /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" min", row=row, col=col)
        elif func == '5':
            data = data.groupby([dataPlot[0].name]).median()
            df = plotlyExpress.line(data)
            df['data'][0].name = dataPlot[1].name+" median /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" median", row=row, col=col)
            
        df['data'][0].showlegend = True
        fig = fig.add_trace(df['data'][0], row=row, col=col)
        fig = fig.update_xaxes(title_text= dataPlot[0].name, row=row, col=col)
        
def barPlot (fig, dimension, dataFrame, dataPlot, func, col, row):
    
        data = pnds.DataFrame({dataPlot[0].name: dataPlot[0], dataPlot[1].name:dataPlot[1]})
        data.reset_index(drop=True, inplace=True)
        
        if func == '0':
            data = data.set_index(dataPlot[0].name)
            df = plotlyExpress.bar(data)
            df['data'][0].name = dataPlot[1].name+" /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name, row=row, col=col)
        elif func == '1':
            data = data.groupby([dataPlot[0].name]).count()
            df = plotlyExpress.bar(data)
            df['data'][0].name = "count "+dataPlot[0].name
            fig = fig.update_yaxes(title_text= "count", row=row, col=col)
        elif func == '2':
            data = data.groupby([dataPlot[0].name]).mean()
            df = plotlyExpress.bar(data)
            df['data'][0].name = dataPlot[1].name+" mean /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" mean", row=row, col=col)
        elif func == '3':
            data = data.groupby([dataPlot[0].name]).max()
            df = plotlyExpress.bar(data)
            df['data'][0].name = dataPlot[1].name+" max /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" max", row=row, col=col)
        elif func == '4':
            data = data.groupby([dataPlot[0].name]).min()
            df = plotlyExpress.bar(data)
            df['data'][0].name = dataPlot[1].name+" min /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" min", row=row, col=col)
        elif func == '5':
            data = data.groupby([dataPlot[0].name]).median()
            df = plotlyExpress.bar(data)
            df['data'][0].name = dataPlot[1].name+" median /"+dataPlot[0].name
            fig = fig.update_yaxes(title_text= dataPlot[1].name+" median", row=row, col=col)
            
        df['data'][0].showlegend = True
        fig = fig.add_trace(df['data'][0], row=row, col=col)
        fig = fig.update_xaxes(title_text= dataPlot[0].name, row=row, col=col)
        
def piePlot (fig, dimension, dataFrame, dataPlot, func, col, row):
        data = pnds.DataFrame({dataPlot[0].name: dataPlot[0], dataPlot[1].name:dataPlot[1]})
        data.reset_index(drop=True, inplace=True)
        df = plotlyExpress.pie(data,
                 values=dataPlot[0], names=dataPlot[1], labels={'values':dataPlot[0].name, 'names':dataPlot[1].name}).update_traces(textposition='inside', textinfo='percent+label')
            
        df['data'][0].name = dataPlot[1].name+" / "+dataPlot[0].name
        df['data'][0].showlegend = True
        fig = fig.add_trace(df['data'][0], row=row, col=col)
        
        
    
def boxPlot (fig, dimension, dataFrame, dataPlot, func, col, row):
    fig.add_trace(plotlyExpress.box(pnds.DataFrame({dataPlot[0].name:dataPlot[0]}))['data'][0], row=row, col=col)
    fig = fig.update_yaxes(title_text= dataPlot[0].name, row=row, col=col)