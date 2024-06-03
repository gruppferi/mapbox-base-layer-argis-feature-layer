# Mapbox with ArcGIS FeatureLayer + Toggles

This is a simple web application that displays a map using Mapbox GL JS and allows users to toggle the visibility of ArcGIS FeatureLayer fill and line layers.

## HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
  <!-- Include Mapbox GL JS stylesheet and script -->
  <link href="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css" rel="stylesheet" />
  <script src="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js"></script>
  <style>
    /* CSS styles for the map and toggles */
  </style>
</head>
<body>
  <!-- Map container -->
  <div id="map"></div>

  <!-- Toggle container -->
  <div class="toggle-container">
    <!-- Checkboxes for toggling fill and line layers -->
  </div>

  <script>
    // JavaScript code for initializing the map and toggling layers
  </script>
</body>
</html>
```

## JavaScript Logic

```javascript
// Initialize Mapbox map
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [2.3522219, 48.856614], // Paris coordinates as an example
  zoom: 12
});

// Fetch ArcGIS FeatureLayer data
async function fetchFeatureLayer() {
  // Fetch data using fetch API
  // Parse the response as GeoJSON
  // Return the GeoJSON data
}

// Add fill and line layers to the map
map.on('load', async () => {
  const featureLayerData = await fetchFeatureLayer();
  // Add layers using map.addLayer()
});

// Event listeners for toggling layer visibility
// Use map.setLayoutProperty() to change layer visibility
```

## Explanation

- The HTML structure consists of a `div` for the map and a separate `div` for toggles.
- The JavaScript logic initializes the Mapbox map, fetches ArcGIS FeatureLayer data, adds fill and line layers to the map, and sets up event listeners for toggling layer visibility.

This simple application allows users to toggle the visibility of ArcGIS FeatureLayer fill and line layers on the map.

## Prerequisite
* python3
* Browser

## Installation
```
pip install flask
```
## Usage
```
python app.py YOUR_API_TOKEN YOUR_ARCGIS_FEATURE_LAYER_URL_PATH
```
