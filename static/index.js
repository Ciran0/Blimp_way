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
    console.log(lat, lon);
    var map = L.map('map').setView([lat, lon], 6);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    for(let i = 0;i<3;i++){
    L.marker([51.5, -i*0.01]).addTo(map)
    }
    console.log('load');
}