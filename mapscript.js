var ourLocation;
var view;
var map;

function start(){
  ourLocation = ol.proj.fromLonLat([-71.048021,42.351973]);
  view = new ol.View({
      center: ourLocation,
      zoom: 15
  });

  map = new ol.Map({
      target: 'map',
      layers: [
        new ol.layer.Tile({
          preload: 4,
          source: new ol.source.OSM()
        })
      ],
      // Improve user experience by loading tiles while animating. Will make
      // animations stutter on mobile or slow devices.
      loadTilesWhileAnimating: true,
      view: view
    });
}

function moveToHollywood(){
  hollywoodLocation = ol.proj.fromLonLat([-118.321548,34.134115]);
  view.animate({zoom:12},{duration:50000},{center:hollywoodLocation},{easing:"upAndDown"});
}

//this will run the start function
window.onload = start;
