 function runPythonScript() {
    var xhr = new XMLHttpRequest();
    let city1 = document.getElementById("form").elements['city1'].value, city2 = document.getElementById("form").elements['city2'].value;

    xhr.open('GET', `http://127.0.0.1:5000/city/${city1}/${city2}`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            loadMap(xhr.responseText);
        }
    };
    xhr.send();

 }


function loadMap(points){
    points = JSON.parse(points);
    console.log(points);
    let lon = (points[0][1]+points[1][1]+points[2][1]+points[3][1])/4;
    let lat = (points[0][0]+points[1][0]+points[2][0]+points[3][0])/4;
    //console.log(lat, lon);
    var map = L.map('map').setView([lat, lon], 6);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    for(let i = 0;i<=4;i++){
    //L.marker([points[i][0], points[i][1]]).addTo(map)

    var circle = L.circle([points[i][0], points[i][1]], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 5000
    }).addTo(map);

    /*var polygon = L.polygon([
    [points[i][0], points[i][1]-0.25],
    [points[i][0], points[i][1]+0.5-0.25],
    [points[i][0]+points[i][2]*0.1, points[i][1]+0.25-0.25]
    ]).addTo(map);*/
    addArrowMarker(points[i][0], points[i][1], points[i][2], points[i][3])

    }
    console.log('map load');


    function addArrowMarker(latitude, longitude, speed, angle) {
            var arrowIcon = L.icon({
                iconUrl: "static/images/arrow-icon.png",
                iconSize: [speed*10, 15],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34]
            });

            L.rotatedMarker([latitude, longitude], {
            rotationAngle: angle+180,
            draggable: false,
            icon: arrowIcon,
            }).addTo(map);

    }
}




