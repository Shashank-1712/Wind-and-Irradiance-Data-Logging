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

## Hardware used

1. Pyranometer(Solar Irradiance Measurement)
2. Anemometer(Wind Speed)
3. Arduino MEGA 2560
4. RaspBerrypi Module 5
5. Signal Conditioning Module( DPA-053/AD-620)
6. AC 220v to DC 24v Convertor
7. Jumper Wires

## Software and Tools

1. Arduino IDE
2. Python (for data logging)
3. Raspberry pi OS
4. Raspberry pi imager(for setting up SSH)

## Data Comparision Concept

The collected ground data can be compared with satellite-derived measurements to:

1. analyze differences between ground and satellite data
2. calculate measurement error
3. evaluate the accuracy of satellite models

Such comparisons help improve the reliability of remote sensing data.










  
