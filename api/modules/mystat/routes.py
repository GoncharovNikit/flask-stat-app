import pandas as pd
import matplotlib.pyplot as plt
import io
from flask import Response, request

def init_routes(app):
    @app.route('/mystat/json')
    def mystatJson():
        mystat = pd.read_csv(app.root_path + '/data/mystat.csv', index_col="Date")
        print(mystat)

        if request.args.get('addSleepDuration', default=False, type=bool):
            mystat["Got up at"] = pd.to_datetime(mystat.index.to_series().astype(str) + " " + mystat["Got up at"], dayfirst=True)
            mystat["To bed at"] = pd.to_datetime(mystat.index.to_series().astype(str) + " " + mystat["To bed at"], dayfirst=True)
            mystat.loc[mystat["To bed at"] < mystat["Got up at"], "To bed at"] += pd.Timedelta(days=1)
            sDurs =  mystat.iloc[1:]["Got up at"].reset_index(drop=True) - mystat.iloc[:-1]["To bed at"].reset_index(drop=True)
            sDurs.index = mystat.iloc[1:].index
            mystat["Sleep duration"] = sDurs.astype(str).str.replace("^0 days ", "", regex=True)
            mystat["Got up at"] = mystat["Got up at"].dt.strftime("%R")
            mystat["To bed at"] = mystat["To bed at"].dt.strftime("%R")
            
        return mystat.reset_index().to_json(orient='records', index=True, date_format="epoch")

    @app.route('/mystat/expenses/chart.png')
    def expensesPng():
        mystat = pd.read_csv(app.root_path + '/data/mystat.csv', index_col='Date', parse_dates=['Date'], dayfirst=True)

        plt.figure(figsize=(9, 7))
        dates = mystat.index.strftime('%d-%m')
        plt.bar(dates, mystat['Pln total'], color='#8bd3c7', label='In Total')
        plt.bar(dates, mystat['Pln osweets'].replace(0.01, 0), color='#fd7f6f', label='On Sweets')

        plt.xticks(rotation=45)
        plt.ylim([0, 170])
        plt.ylabel('Amount, Pln')
        plt.title('My Expenses')

        plt.legend(loc=2, bbox_to_anchor=(.03, .95))

        for x, y1, y2 in zip(dates, mystat['Pln osweets'].replace(0.01, 0), mystat['Pln total']):
            if not y1 == 0:
                plt.text(x, y1 + 2, y1, ha='center', fontsize=6)
            if not y2 == 0:
                plt.text(x, y2 + 2, y2, ha='center', fontsize=7)

        plt.tight_layout()

        output = io.BytesIO()
        plt.savefig(output, format='png')

        return Response(output.getvalue(), mimetype='image/png')