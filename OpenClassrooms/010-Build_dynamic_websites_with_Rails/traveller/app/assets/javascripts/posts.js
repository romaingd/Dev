$(function () {
  function initializeMap(data) {
    var posts = $.parseJSON(data);
    var geoJSON = L.geoJSON(posts);
    
    var map = L.map('map');
    var layer = Tangram.leafletLayer({
      scene: 'scene.yaml',
      attribution: '<a href="https://nextzen.org/tangram" target="_blank">Tangram</a> | &copy; OSM contributors | <a href="https://nextzen.org/" target="_blank">Nextzen</a>'
    });

    layer.addTo(map);
    
    // this line adds our posts:
    geoJSON.addTo(map);

    // and this centers the map on the lat/long of our first post:
    map.setView(posts[0].geometry.coordinates.reverse(), 15);
  };

  $.ajax({
    url: '/posts.json',
    dataType: 'text',
    success: initializeMap
  });
});