#!/usr/bin/env python3
""" A Python3 binding for the propa.dll """

# import statements
from ctypes import *
import numpy as np
import inspect
import os
from pathlib import Path

# load DLL using ctypes
BASE_FOLDER = Path(os.path.dirname(os.path.abspath(inspect.stack()[0][1])))  # gets path to the propa directory
BASE_FILE = BASE_FOLDER / 'dll' / 'propa64.dll'  # if file is ./dll/propa64.dll
PROPA_DLL = cdll.LoadLibrary(str(BASE_FILE.resolve()))  # import using ctypes


# DLL FUNCTIONS
def rain_intensity(lat, lon, unavail):
    # grab the C function
    rain_intensity_func = PROPA_DLL.rain_intensity
    # specify argument types
    rain_intensity_func.argtypes = [c_double, c_double, c_double]
    # specify return type
    rain_intensity_func.restype = c_double
    # return value
    return rain_intensity_func(lat, lon, unavail)


def nwet(lat, lon):
    # grab the C function
    nwet_func = PROPA_DLL.NWET
    # specify argument types
    nwet_func.argtypes = [c_double, c_double]
    # specify return type
    nwet_func.restype = c_double
    # return value
    return nwet_func(lat, lon)


def rain_height(lat, lon):
    # grab the C function
    rain_height_func = PROPA_DLL.rain_height
    # specify argument types
    rain_height_func.argtypes = [c_double, c_double]
    # specify return type
    rain_height_func.restype = c_double
    # return value
    return rain_height_func(lat, lon)


def lwcc(lat, lon, unavail):
    # grab the C function
    lwcc_func = PROPA_DLL.LWCC
    # specify argument types
    lwcc_func.argtypes = [c_double, c_double, c_double]
    # specify return type
    lwcc_func.restype = c_double
    # return value
    return lwcc_func(lat, lon, unavail)


def swvd(lat, lon):
    # grab the C function
    swvd_func = PROPA_DLL.SWVD
    # specify argument types
    swvd_func.argtypes = [c_double, c_double]
    # specify return type
    swvd_func.restype = c_double
    # return value
    return swvd_func(lat, lon)


def iwvc(lat, lon, unavail):
    # grab the C function
    iwvc_func = PROPA_DLL.IWVC
    # specify argument types
    iwvc_func.argtypes = [c_double, c_double, c_double]
    # specify return type
    iwvc_func.restype = c_double
    # return value
    return iwvc_func(lat, lon, unavail)


def temperature(lat, lon):
    # grab the C function
    temperature_func = PROPA_DLL.temperature
    # specify argument types
    temperature_func.argtypes = [c_double, c_double]
    # specify return type
    temperature_func.restype = c_double
    # return value
    return temperature_func(lat, lon)


def tmr(surface_temp):
    # grab the C function
    tmr_func = PROPA_DLL.TMR
    # specify argument types
    tmr_func.argtypes = [c_double]
    # specify return type
    tmr_func.restype = c_double
    # return value
    return tmr_func(surface_temp)


def gaseous_attenuation(freq, elev, temp, ro):
    # grab the C function
    gaseous_attenuation_func = PROPA_DLL.gaseous_attenuation
    # specify argument types
    gaseous_attenuation_func.argtypes = [c_double, c_double, c_double, c_double]
    # specify return type
    gaseous_attenuation_func.restype = c_double
    # return value
    return gaseous_attenuation_func(freq, elev, temp, ro)


def gaseous_attenuation_exc(freq, elev, temp, wvc):
    # grab the C function
    gaseous_attenuation_exc_func = PROPA_DLL.gaseous_attenuation_exc
    # specify argument types
    gaseous_attenuation_exc_func.argtypes = [c_double, c_double, c_double, c_double]
    # specify return type
    gaseous_attenuation_exc_func.restype = c_double
    # return value
    return gaseous_attenuation_exc_func(freq, elev, temp, wvc)


def rain_attenuation(lat, freq, elev, unavail, alt, rain_height_val, rain_intensity_val, pol):
    # grab the C function
    rain_attenuation_func = PROPA_DLL.rain_attenuation
    # specify argument types
    rain_attenuation_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
    # specify return type
    rain_attenuation_func.restype = c_double
    # return value
    return rain_attenuation_func(lat, freq, elev, unavail, alt, rain_height_val, rain_intensity_val, pol)


def cloud_attenuation(freq, elev, tcc):
    # grab the C function
    cloud_attenuation_func = PROPA_DLL.cloud_attenuation
    # specify argument types
    cloud_attenuation_func.argtypes = [c_double, c_double, c_double]
    # specify return type
    cloud_attenuation_func.restype = c_double
    # return value
    return cloud_attenuation_func(freq, elev, tcc)


def scintillation(nwet_val, freq, elev, unavail, alt, eff, dia):
    # grab the C function
    scintillation_func = PROPA_DLL.cloud_attenuation
    # specify argument types
    scintillation_func.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double]
    # specify return type
    scintillation_func.restype = c_double
    # return value
    return scintillation_func(nwet_val, freq, elev, unavail, alt, eff, dia)


def xpd(rain_atten, tilt_deg, freq, elev_deg, unavail):
    # grab the C function
    xpd_func = PROPA_DLL.XPD
    # specify argument types
    xpd_func.argtypes = [c_double, c_double, c_double, c_double, c_double]
    # specify return type
    xpd_func.restype = c_double
    # return value
    return xpd_func(rain_atten, tilt_deg, freq, elev_deg, unavail)


def noise_temperature(total_atten_val, tmr_val):
    # grab the C function
    noise_temperature_func = PROPA_DLL.noise_temperature
    # specify argument types
    noise_temperature_func.argtypes = [c_double, c_double]
    # specify return type
    noise_temperature_func.restype = c_double
    # return value
    return noise_temperature_func(total_atten_val, tmr_val)


def efsr(freq1, freq2, rain_atten_freq1):
    # grab the C function
    efsr_func = PROPA_DLL.EFSR
    # specify argument types
    efsr_func.argtypes = [c_double, c_double, c_double]
    # specify return type
    efsr_func.restype = c_double
    # return value
    return efsr_func(freq1, freq2, rain_atten_freq1)


# EXTRA (USEFUL) FUNCTIONS
def total_attenuation(gas_atten, rain_atten, cloud_atten, scint):
    return gas_atten + np.sqrt(np.power((rain_atten + cloud_atten), 2) + np.power(scint, 2))

