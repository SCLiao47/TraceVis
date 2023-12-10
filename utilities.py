
import numpy as np
import plotly.express as px
import tcxparser
import datetime

def get_discrete_colormap(Ntrace, colormap='sunset', order='reverse'):
    '''    
    create discrete color map as line_mapbox don't handle continuous color map

    [Some Color options]
    mabpox_style = "dark", colormap = 'thermal', forward
    mabpox_style = "dark", colormap = 'sunset', reverse
    mabpox_style = "light", colormap = 'agsunset', forward

    [Reference]
    * solution from https://stackoverflow.com/questions/68575172/how-to-correctly-use-colormaps-for-plotly-express-line-mapbox
    * discr_map: https://plotly.com/python-api-reference/generated/plotly.express.line_mapbox.html#plotly.express.line_mapbox
    * Plotly build-in continuous color: https://plotly.com/python/builtin-colorscales/
    '''

    discr_map = {}
    for i in range(0, Ntrace):
        if order == 'reverse':
            color_rgb = px.colors.sample_colorscale(colormap, 1 - float(i)/Ntrace)      # reverse-order
        else:
            color_rgb = px.colors.sample_colorscale(colormap, float(i)/Ntrace)      # normal-order

        # formatting color_rgb
        color_rgb = color_rgb[0].replace('rgb(', '').replace(')', '').split(',')

        # the value is in CSS-color format
        discr_map.update({i: '#%02x%02x%02x' % (int(color_rgb[0]), int(color_rgb[1]), int(color_rgb[2]))})

    return discr_map


def processTCX(tcx_file):
    '''
    To access datas
    - get positions: tcx.position_values()
    - get duration (seconds): tcx.duration
    - get distance: tcx.root.Activities.Activity.Lap[0].DistanceMeters
    - get pace (second/km): pace = tcx.duration / (tcx.root.Activities.Activity.Lap[0].DistanceMeters / 1000)
    '''

    # [Load the data into a tcxparser object]
    tcx = tcxparser.TCXParser(tcx_file)
    
    # [Process the data]
    # get position into latitudes and longitudes
    position = np.array(tcx.position_values())
    lats = position[:, 0]
    lons = position[:, 1]

    # turn utc time into seconds
    time_utc = tcx.time_values()
    time_seconds = []
    for t in time_utc:
        utc_datetime = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
        second = utc_datetime.timestamp()
        time_seconds = np.append(time_seconds, second)

    # [Output]
    data = dict(lat=lats, 
                lon=lons, 
                time=time_seconds)
    
    return data

def plotly_animation_button():
    '''
    get buttons for animation {play, Pause}
    '''
    updatemenus = [dict(
            buttons = [
                dict(
                    args = [None, {"frame": {"duration": 200, "redraw": True},
                                    "fromcurrent": True}],
                    label = "Play",
                    method = "animate"
                    ),
                dict(
                    args = [[None], {"frame": {"duration": 0, "redraw": False},
                                    "mode": "immediate",
                                    "transition": {"duration": 0}}],
                    label = "Pause",
                    method = "animate"
                    )
            ],
            direction = "left",
            pad = {"r": 10, "t": 10},
            showactive = False,
            type = "buttons",
            x = 0.1,
            xanchor = "right",
            y = 0,
            yanchor = "top"
        )] 
    
    return updatemenus