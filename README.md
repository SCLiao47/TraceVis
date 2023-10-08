# TraceVis
Trace Visualization for running logs

This project tries to visually document the training process of my first marathon (Ann Arbor Marathon on October 1st, 2023). I used Nike Running Club (NRC) to record the training for this marathon. 

# General Process
1. Gather running data in .gpx files
2. Generate a map image
3. Align coordinates between .gpx files and map image
4. Compute waypoint in map coordinates and estimate speed for each trace
5. Overlap traces on the map

# Developement Plan and Log
Expected outcome:
Animations of trajectories on a given map in the order of date. Each trajectory is colored by estimated speed.

Required inputs:
1. Running files in .gpx
2. Map image and corresponding coordinate

## Plan
- [ ] Gather running data
- [ ] Generate AA map by tools, such as [mapbox](https://www.mapbox.com/)
- [ ] .gpx data parser and translator
- [ ] animation functions and exportation utilities

## Log
### 2023/10/7
1. Initialize the project and the development plan.
2. Figure out how to export data from NRC. Strava provides an easy way for [data exportation]([url](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#h_01GG58HC4F1BGQ9PQZZVANN6WF)), and [NRC provides synchronization to Strava](https://press.strava.com/articles/strava-launches-nike-run-club-and-nike-training-club-integration-available#:~:text=NRC%20and%20NTC%20are%20the,coaching%2C%20inspiration%2C%20and%20community.) starting from September 2023. All new running records can be synced to Strava once the setting is done in the NRC app. However, all history records cannot be synced currently, and NRC can not export the data in its app and requires third-party software. At the moment, [SyncMyTracks](https://play.google.com/store/apps/details?id=com.syncmytracks&hl=en_US&gl=US) on Android does the work.  

## Backlog and wishlists
1. Automated map image generation according to running files


# Related Project
[gpx-animator](https://github.com/gpx-animator/gpx-animator)
