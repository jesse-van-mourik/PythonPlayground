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

application = Blueprint('stats', __name__)


@application.route('/plot.png')
def build_plot():
    y = [1, 2, 3, 4, 5]
    x = [2, 4, 6, 8, 10]

    fig = Figure()
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(x, y)
    img = io.BytesIO()

    FigureCanvasAgg(fig).print_png(img)
    return Response(img.getvalue(), mimetype='image/png')
