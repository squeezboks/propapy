#!/usr/bin/env python3
""" A Python3 binding for the propa.dll """
import numpy as np

from propa import propa

# set WARNINGS to false to suppress warnings
WARNINGS = True

def demo():
    # redo calculation from demoprop.xlsx file

    print(" << RUNNING DEMO >> ")

    print("> Assigning inputs...")

    # station
    station = {'lat': 44.17, 'lon': -80.9, 'alt': 0, 'elv': 90}

    # antenna
    antenna = {'dia': 1, 'eff': 50}

    # link
    link = {'freq1': 20, 'freq2': 30, 'pol': 45, 'unavail': 0.01}

    if link['unavail'] < 1:
        if WARNINGS: print(" - WARNING: 'unavail' less than 1%, calculating 'iwvc' at 1%")
        if WARNINGS: print(" - WARNING: 'unavail' less than 1%, calculating 'lwcc' at 1%")

    print("> Calculating climatic parameters...")

    # climatic parameters
    climate = dict()
    climate['rain_intensity'] = propa.rain_intensity(station['lat'], station['lon'], 0.01)
    climate['Nwet'] = propa.nwet(station['lat'], station['lon'])
    climate['rain_height'] = propa.rain_height(station['lat'], station['lon'])
    climate['total_columnar_content'] = propa.lwcc(station['lat'], station['lon'], link['unavail'] if link['unavail'] < 1 else 1)
    climate['surface_water_vapour_density'] = propa.swvd(station['lat'], station['lon'])
    climate['integrated_water_vapour_content'] = propa.iwvc(station['lat'], station['lon'], link['unavail'] if link['unavail'] < 1 else 1)
    climate['temperature'] = propa.temperature(station['lat'], station['lon'])
    climate['mean_radiating_temperature'] = propa.tmr(climate['temperature'])

    # attenuation by direct calculation (frequency 1)
    attenuation = dict()
    attenuation['atm_gas_atten'] = propa.gaseous_attenuation(link['freq1'], np.deg2rad(station['elv']), climate['temperature'], climate['surface_water_vapour_density'])
    attenuation['exc_atm_gas_atten'] = propa.gaseous_attenuation_exc(link['freq1'], np.deg2rad(station['elv']), climate['temperature'], climate['integrated_water_vapour_content'])
    attenuation['rain_atten'] = propa.rain_attenuation(station['lat'], link['freq1'], np.deg2rad(station['elv']), link['unavail'], station['alt'], climate['rain_height'], climate['rain_intensity'], link['pol'])
    attenuation['cloud_atten'] = propa.cloud_attenuation(link['freq1'], np.deg2rad(station['elv']), climate['total_columnar_content'])
    attenuation['scintillation'] = propa.scintillation(climate['Nwet'], link['freq1'], np.deg2rad(station['elv']), link['unavail'], station['alt'], antenna['eff'] / 100, antenna['dia'])
    attenuation['XPD'] = propa.xpd(attenuation['rain_atten'], link['pol'], link['freq1'], station['elv'], link['unavail'])
    attenuation['total_atten_wo_XPD_method1'] = propa.total_attenuation(attenuation['atm_gas_atten'], attenuation['rain_atten'], attenuation['cloud_atten'], attenuation['scintillation'])
    attenuation['total_atten_wo_XPD_method2'] = propa.total_attenuation(attenuation['exc_atm_gas_atten'], attenuation['rain_atten'], attenuation['cloud_atten'], attenuation['scintillation'])
    attenuation['sky_noise_temp'] = propa.noise_temperature((attenuation['exc_atm_gas_atten'] + attenuation['rain_atten'] + attenuation['cloud_atten']), climate['mean_radiating_temperature'])  # different than calling total_atten function!

    # attenuation by scaling (frequency 2)
    long_term_rain_atten2 = propa.efsr(link['freq1'], link['freq2'], attenuation['rain_atten'])

    # print results

    print(" << RESULTS >> ")
    print(" ------------------------------------------- ")
    print("> Station")
    for key, value in station.items():
        print(" - " + str(key) + " : " + str(value))

    print(" ------------------------------------------- ")
    print("> Antenna")
    for key, value in antenna.items():
        print(" - " + str(key) + " : " + str(value))

    print(" ------------------------------------------- ")
    print("> Link")
    for key, value in link.items():
        print(" - " + str(key) + " : " + str(value))

    print(" ------------------------------------------- ")
    print("> Climatic Parameters")
    for key, value in climate.items():
        print(" - " + str(key) + " : " + str(value))

    print(" ------------------------------------------- ")
    print("> Attenuation - Frequency 1")
    for key, value in attenuation.items():
        print(" - " + str(key) + " : " + str(value))

    print(" ------------------------------------------- ")
    print("> Attenuation - Frequency 2")
    print(" - long_term_rain_atten_freq2_scaling : " + str(long_term_rain_atten2))


if __name__ == '__main__':
    demo()