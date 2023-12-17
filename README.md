# TraceVis: Trace Visualization for running logs

This project tries to visually document the training process of my first marathon (Ann Arbor Marathon on October 1st, 2023). I used Nike Running Club (NRC) to record the training for this marathon. 
![Snapshot of 20231111](/Image/Static_20231121.png)

# General Process
1. Gather running data in **.gpx** files
    1. Prepare two testing traces and name them `Data/Test/Test.tcx` and `Data/Test/Test2.tcx`.
    2. All other traces should be in the `Data` folder as `Data/*.tcx`.
2. Register Mapbox for certain map styles
    1. store the Mapbox token in a file named `.mapbox_token`.
3. `StaticVisualization.ipynb` is used to generate a static image with all traces.
4. `AnimatedVisualization.ipynb` is used to generate a .gif image for all traces. 

# Developement Plan and Log
Expected outcome:
Animations of trajectories on a given map in the order of date. Each trajectory is colored by estimated speed.

Required inputs:
1. Running files in `Data/*.gpx`
2. Map image and corresponding coordinate

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
- [ ] Packaging
  - [ ] Clean up code
      - [x] utility functions
      - [x] configuration file
  - [ ] Document write up

## Log
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


## Backlog and wishlist
1. Automated generate `center` and `zoom` for mapbox based on traces. 


# Related Project
[gpx-animator](https://github.com/gpx-animator/gpx-animator)
