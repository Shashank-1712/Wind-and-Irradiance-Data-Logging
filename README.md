# Wind and Irradiance data logging using arduino and Raspberrypi

## Overview

This project focuses on collecting environmental data from ground-based sensors and comparing it with satellite-derived data to evaluate accuracy.
The system measures solar irradiance and wind speed using sensors and stores the readings in a CSV data log.

The collected ground data can then be used as a test dataset, while satellite datasets can be used as a training or reference dataset.
By comparing both datasets, the project aims to evaluate the accuracy and reliability of satellite-based environmental measurements.

## Objectives

1. Collect realtime data from sennsors
2. Log Measurements in structured CSV format
3. Use satellite data as a reference/training dataset
4. Compare ground measurements with satellite values
5. Evaluate measurement accuracy and possible deviations

## System Architecture

1. Sensors measure environmental parameters:
     a. Pyranometer --> Solar Irradiance
     b. Anemometer  --> Wind Speed
2. Arduino reads sensor signals and sends data through serial communication.
3. Raspberry Pi receives the sensor data and stores it in CSV files for analysis.
4. The logged data can later be compared with satellite environmental datasets to evaluate accuracy. 

  
