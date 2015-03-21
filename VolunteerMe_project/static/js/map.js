var latitude;
var longitude;

function setLatLng(lat, lng) {

    latitude = lat;
    longitude = lng;
}

function initialize() {
    var mapOptions = {
        center: { lat: latitude, lng: longitude},
        zoom: 20
    };
    var map = new google.maps.Map(document.getElementById('map-canvas'),
    mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);