#!/usr/bin/env bash

# current_weather_curl.sh
# Fetch current weather from MeteoSwiss without python

station=""
list=0

while [[ "$#" -gt 0 ]]; do
  case $1 in
    --station) station="$2"; shift ;;
    --list) list=1 ;;
    *) echo "Unknown parameter: $1"; exit 1 ;;
  esac
  shift
done

if [ "$list" -eq 1 ]; then
  echo "Fetching station list from MeteoSwiss..."
  curl -s "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/info/stations.json" | grep -o '"id":"[^"]*"' | cut -d '"' -f 4
  exit 0
fi

if [ -z "$station" ]; then
  echo "Usage: $0 --station <CODE> | --list"
  exit 1
fi

station=$(echo "$station" | tr '[:lower:]' '[:upper:]')
echo "Fetching current weather for station: $station"

data=$(curl -s "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv" | grep "^$station")

if [ -z "$data" ]; then
  echo "Station $station not found or no data available."
  exit 1
fi

# VQHA80.csv columns: stn, time, tre200s0, ure200s0, rre150z0, sre000z0, gre000z0, pfu100h0, fu3010z0, prestas0, fkl010z0
# 1: Station, 2: Time, 3: Temp, 4: Humidity, 5: Precip, 6: Sun, 7: Rad, 8: Pressure, 9: Wind Speed
IFS=';' read -ra COL <<< "$data"

echo "Station: ${COL[0]}"
echo "Time: ${COL[1]}"
echo "Temperature (°C)........................ ${COL[2]}"
echo "Rel. humidity (%)...................... ${COL[3]}"
echo "Wind speed (km/h)...................... ${COL[8]}"
echo "Precipitation (mm)..................... ${COL[4]}"
