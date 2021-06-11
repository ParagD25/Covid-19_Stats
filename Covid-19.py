import justpy
import pandas
data=pandas.read_csv('covid_19_india.csv',parse_dates=['Date'])

data['Month']=data['Date'].dt.strftime('%Y-%m-%d')
new_data=data[['Month','Confirmed','Deaths','Cured']].groupby('Month').mean()
chart_data="""
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Covid - 19 India Analysis'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: {
            text: 'Date'
        },
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        
    },
    yAxis: {
        title: {
            text: 'Cases'
        }
    },
    tooltip: {
        shared: true,
       
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""
def main_web():
    c19_webpage=justpy.QuasarPage(dark=True)
    heading1=justpy.QDiv(a=c19_webpage,text='Covid-19 India Stats',classes='text-h3 text-center q-pa-md')
    
    para1=justpy.QDiv(a=c19_webpage,text='This Graph Shows Average of Confirmed Cases, Recoveries and Death in a Day',classes='text-h5 text-italic q-pa-lg')
    hc=justpy.HighCharts(a=c19_webpage,options=chart_data)
    #hc.options.series[0].data=list(zip(new_data.index,new_data['thalachh']))
    hc.options.xAxis.categories=list(new_data.index)

    hc_data=[{'name':var1,'data':[var2 for var2 in new_data[var1]]} for var1 in new_data.columns]
    hc.options.series = hc_data
    return c19_webpage

justpy.justpy(main_web)
