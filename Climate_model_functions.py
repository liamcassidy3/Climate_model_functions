# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import xarray as xr
import numpy as np


def lat_lon_indices(lat_specific, lon_specific, lat_array, lon_array):
    """Goal is to extract latitude and longitude indices for a specific area provided the values of latitude and longitude
    
    Inputs:
    lat_specific (float): value of latitude for single location, will require looking at the raw lat and lon arrays
    lon_specific (float): value of longitude for single location, will require looking at the raw lat and lon arrays
    
    Returns:
    lat_index (float): index for requested latitude
    lon_index (float): index for requested longitude
    """
    
    # Latitude Loop init
    lat_index = 1
    lat_eval = 0
    while lat_eval != lat_specific:
        lat_index = lat_index +1
        lat_eval = lat_array[lat_index]
    print("latitude index =:")
    print(lat_index)    
    
    # Longitude Loop init
    lon_index = 1
    lon_eval = 0
    while lon_eval != lon_specific:
        lon_index = lon_index +1
        lon_eval = lon_array[lon_index]
    print("long index =:")
    print(lon_index)
    
    return lon_index, lat_index


def tas_average_area_weight(tas_array, lat_array):
    """Using imported data, apply area weighing for average surface air temperature calculations
    
    Input:
    
    tas_array: array of surface air temperatures (latitude, longitude, over time) for a dataset
    lat_array: array of latitude for a specific dataset
    
    Return:
 
    tas_weighed_mean: average surface temperature over time
    
    """
    
    # Weighing Data
    weights = np.cos(np.deg2rad(lat_array))
    weights.name = "weights"

    tas_weighed = tas_array.weighted(weights) # latitude weighted temperature array
    

    tas_weighed_mean = tas_weighed.mean(("lon", "lat")) # average surface air temperature weighed (over time)
    
    return tas_weighed_mean, tas_weighed

    
def monthly_temp_extractions(tas_array):
    """
    Inputs: 
    tas_array_monthly: Air surface temperature (lat, lon, time) --> Data is not weighed by area
    
    Returns:
    tas_month: Air surface temperature for a specific month over the whole dataset (lat, lon, time)
    """
    
    # Montly temperatures
    tas_january = tas_array.sel(time=tas_array.time.dt.month.isin([1]))
    tas_february = tas_array.sel(time=tas_array.time.dt.month.isin([2]))
    tas_march = tas_array.sel(time=tas_array.time.dt.month.isin([3]))
    tas_april = tas_array.sel(time=tas_array.time.dt.month.isin([4]))
    tas_may = tas_array.sel(time=tas_array.time.dt.month.isin([5]))
    tas_june = tas_array.sel(time=tas_array.time.dt.month.isin([6]))
    tas_july = tas_array.sel(time=tas_array.time.dt.month.isin([7]))
    tas_august = tas_array.sel(time=tas_array.time.dt.month.isin([8]))
    tas_september = tas_array.sel(time=tas_array.time.dt.month.isin([9]))
    tas_october = tas_array.sel(time=tas_array.time.dt.month.isin([10]))
    tas_november = tas_array.sel(time=tas_array.time.dt.month.isin([11]))
    tas_december = tas_array.sel(time=tas_array.time.dt.month.isin([12]))
    
    
    return tas_june, tas_july, tas_august, tas_december, tas_january, tas_february, tas_march, tas_april, tas_may, tas_september, tas_october, tas_november
    









