function initMap() {
        var myLatlng = {lat: -11.363, lng: 80.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: myLatlng
        });
        var temp=[0];
      google.maps.event.addListener(map, 'click', function(event) {
        console.log(temp);
        if(temp[1]==0)
        {
          temp=[temp[0]];
          console.log(temp)
        }
        if(temp.length==1)
        {
          temp.push(1)
          temp=placeMarker(event.latLng,temp);
        }
        console.log(temp)
});
function placeMarker(location,temp) {
    if(temp[1]==1 && temp.length==2)
    {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });

    google.maps.event.addListener(marker,'click',function() {
      marker.setMap(null);
      temp[1]=0;
      console.log(temp);
    });
    var infowindow = new google.maps.InfoWindow({
      content: 'Latitude: ' + location.lat() +
      '<br>Longitude: ' + location.lng()

    });
    infowindow.open(map,marker);
  }
  console.log(temp)
  return temp;
}
}
