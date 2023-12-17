## Plan
- [x] Gather running data from the NRC app. 
- [x] Generate map style on [mapbox](https://www.mapbox.com/)
- [x] Basic visualization pipeline
  - [x] Test visualization process of plotly with mapbox
  - [x] Decide how to handle data (preprocess and save to one big dataframe)
  - [x] Setup scripts for static visualization 
  - [x] format mapbox to have a better view
  - [x] Generate static image for the whole training trace
- [x] animation
  - [x] Test animation process of plotly. It turned out unsuitable in this use case as there are too many frames. 
  - [x] Generating each frame of the animation by plotly and save them as .png.
  - [x] Create .gif from .png images of animation frames. 
- [x] Packaging
  - [x] Clean up code
      - [x] utility functions
      - [x] configuration file
  - [x] Document write up

## Backlog and wishlist
1. Option to color Each trajectory is by estimated speed

##  Log

### 2023/10/7
1. Initialize the project and the development plan.
2. Figure out how to export data from NRC. Strava provides an easy way for [data exportation]([url](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#h_01GG58HC4F1BGQ9PQZZVANN6WF)), and [NRC provides synchronization to Strava](https://press.strava.com/articles/strava-launches-nike-run-club-and-nike-training-club-integration-available#:~:text=NRC%20and%20NTC%20are%20the,coaching%2C%20inspiration%2C%20and%20community.) starting from September 2023. All new running records can be synced to Strava once the setting is done in the NRC app. However, all history records cannot be synced currently, and NRC can not export the data in its app and requires third-party software. At the moment, [SyncMyTracks](https://play.google.com/store/apps/details?id=com.syncmytracks&hl=en_US&gl=US) on Android does the work.

### 2023/10/25
1. Decide the following:
   1. implementation framework: Python.
   2. Graphing Libraries: [plotly](https://plotly.com/python/). It can interface with [mapbox directly](https://plotly.com/python/scattermapbox/) (with a token) and has [built-in animation functionality](https://plotly.com/python/animations/).
   3. TCX data process: [pyworkout-toolkit](https://github.com/triskadecaepyon/pyworkout-toolkit) can parse .TCX files to Pandas DataFrame.
2. Update Development Plan

### 2023/11/04
1. Start implementing the pipeline in the script `StaticVisualization.ipynb`
2. Realize **pyworkout-toolkit** does not parse each data point. Switch to [python-tcxparser](https://github.com/vkurup/python-tcxparser) for reading the .tcx files. 
3. Progress: read one .tcx file and plot the trace on Mapbox map. 

### 2023/11/11
1. Read all files in the Data folder and store them into big numpy arrays
2. Plot traces on Mapbox and color each trace by the index of data
3. The color is handled by a `dict` structure for discrete colormap as `px.line_mapbox` does not support continuous colormap.

### 2023/11/21
1. Formatting Mapbox plot for better visualization, include {height, width, zoom}
2. Try out different coloring styles. Settle on 'dark' map with reversed 'sunset' colormap
3. Put numpy data in to Pandas dataframe

### 2023/12/01 - 12/04
1. Found that plotly is not suitable for directly animating such large amount of frames. Switch to separated approach: save each frame as .png and make .gif afterward.
2. To output plotly as image file, need `kaleido` package. However, [it somehow needs to be downgraded](https://stackoverflow.com/a/72614865/13624201).
3. Turns out, plotly output image with `orca` is more efficient in this case. 
4. Implemented pngs to gif via `PIM` and get the [**animation.gif**](/Image/animation.gif)

### 2023/12/10
1. Start cleaning up by creating utilities.py to streamline the process.

### 2023/12/16
1. Move the settings in scripts to `config.yaml` file.
2. Clean up readme file and write up documents.
3. Found another python-based (tcxreader)[https://github.com/alenrajsp/tcxreader]
