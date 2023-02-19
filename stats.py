import io
import cbsodata
from matplotlib.backends.backend_agg import FigureCanvasAgg
from flask import Blueprint, Response
from scipy.stats import pearsonr
from matplotlib.figure import Figure

application = Blueprint('stats', __name__)


@application.route('/plot/<year>', methods=('POST', 'GET'))
def build_plot(year):

    x = ['1st cat', '2nd cat', '3rd cat', '4th cat', '5th cat']

    y_value_arrays = get_y_value_arrays(year)
    best_r = get_best_pearsonr(y_value_arrays)

    fig = Figure()
    plot = fig.add_subplot(1, 1, 1)

    if best_r == 'education':
        plot.plot(x, y_value_arrays[0], color='red', label='education')
    else:
        plot.plot(x, y_value_arrays[0], color='grey', label='education')

    if best_r == 'wealth':
        plot.plot(x, y_value_arrays[1], color='red', label='wealth')
    else:
        plot.plot(x, y_value_arrays[1], color='grey', label='wealth', dashes=[4, 2])

    if best_r == 'income':
        plot.plot(x, y_value_arrays[2], color='red', label='income')
    else:
        plot.plot(x, y_value_arrays[2], color='grey', label='income', dashes=[8, 2])

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


def get_y_value_arrays(periode):
    edu = []
    wealth = []
    income = []

    edu.append(get_visconsumptie_persoonskenmerk(2018710, periode))
    edu.append(get_visconsumptie_persoonskenmerk(2018720, periode))
    edu.append(get_visconsumptie_persoonskenmerk(2018750, periode))
    edu.append(get_visconsumptie_persoonskenmerk(2018800, periode))
    edu.append(get_visconsumptie_persoonskenmerk(2018810, periode))

    wealth.append(get_visconsumptie_persoonskenmerk(1021200, periode))
    wealth.append(get_visconsumptie_persoonskenmerk(1021210, periode))
    wealth.append(get_visconsumptie_persoonskenmerk(1021220, periode))
    wealth.append(get_visconsumptie_persoonskenmerk(1021230, periode))
    wealth.append(get_visconsumptie_persoonskenmerk(1021240, periode))

    income.append(get_visconsumptie_persoonskenmerk(1014752, periode))
    income.append(get_visconsumptie_persoonskenmerk(1014753, periode))
    income.append(get_visconsumptie_persoonskenmerk(1014754, periode))
    income.append(get_visconsumptie_persoonskenmerk(1014755, periode))
    income.append(get_visconsumptie_persoonskenmerk(1014756, periode))

    return [edu, wealth, income]


def get_best_pearsonr(y_value_arrays):
    x = [1, 2, 3, 4, 5]
    # education, wealth, income
    r_values = [pearsonr(x, y_value_arrays[0]), pearsonr(x, y_value_arrays[1]), pearsonr(x, y_value_arrays[2])]
    max_idx = r_values.index(max(r_values))

    if max_idx == 0:
        return 'education'
    if max_idx == 1:
        return 'wealth'
    if max_idx == 2:
        return 'income'

    return ''
