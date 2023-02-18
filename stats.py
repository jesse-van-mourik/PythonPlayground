import base64
import io
import cbsodata
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from flask import Blueprint, Response

# table_id = '85058NED'
# year = 2015
# province = 'PV25  '
#
# ds = cbsodata.get_data(
#       table_id=table_id,
#       filters="Perioden gt '" + str(year) + "JJ00' "
#               "and SoortBewoondeWoonruimten eq 'A050218' "
#               "and RegioS eq '" + province + "'",
#       select='SoortBewoondeWoonruimten, '
#              'Perioden, '
#              'BewoondeWoonruimte_1, '
#              'RegioS'
# )
# print(ds)
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from numpy import NaN

application = Blueprint('stats', __name__)


@application.route('/plot.png')
def build_plot():
    edu = []
    wealth = []
    income = []
    x = ['1st cat', '2nd cat', '3rd cat', '4th cat', '5th cat']

    edu.append(get_visconsumptie_persoonskenmerk(2018710))
    edu.append(get_visconsumptie_persoonskenmerk(2018720))
    edu.append(get_visconsumptie_persoonskenmerk(2018750))
    edu.append(get_visconsumptie_persoonskenmerk(2018800))
    edu.append(get_visconsumptie_persoonskenmerk(2018810))

    wealth.append(get_visconsumptie_persoonskenmerk(1021200))
    wealth.append(get_visconsumptie_persoonskenmerk(1021210))
    wealth.append(get_visconsumptie_persoonskenmerk(1021220))
    wealth.append(get_visconsumptie_persoonskenmerk(1021230))
    wealth.append(get_visconsumptie_persoonskenmerk(1021240))

    income.append(get_visconsumptie_persoonskenmerk(1014752))
    income.append(get_visconsumptie_persoonskenmerk(1014753))
    income.append(get_visconsumptie_persoonskenmerk(1014754))
    income.append(get_visconsumptie_persoonskenmerk(1014755))
    income.append(get_visconsumptie_persoonskenmerk(1014756))

    fig = Figure()
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(x, edu, color='red', label='education')
    plot.plot(x, wealth, color='blue', label='wealth')
    plot.plot(x, income, color='green', label='income')
    plot.legend(loc='upper left')
    img = io.BytesIO()

    FigureCanvasAgg(fig).print_png(img)
    return Response(img.getvalue(), mimetype='image/png')


# 2018710, 2018720, 2018750, 2018800, 2018810 = basis t/m master onderwijs
# 1021200, 1021210, 1021220, 1021230, 1021240 = 1e t/m 5e 20% vermogen
# 1014752, 1014753, 1014754, 1014755, 1014756 = 1e t/m 5e 20% inkomen
def get_visconsumptie_persoonskenmerk(kenmerk, periode=2021):
    table_id = '85457NED'
    ds = cbsodata.get_data(
        table_id=table_id,
        filters="Persoonskenmerken eq '" + str(kenmerk) + "'"
                " and Perioden eq '" + str(periode) + "JJ00'",
        select='Persoonskenmerken,'
               'Perioden,'
               'Minimaal1DagPerWeek_73'
    )

    return ds[0]['Minimaal1DagPerWeek_73']
