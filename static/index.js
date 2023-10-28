 function runPythonScript() {
    var xhr = new XMLHttpRequest();
    let city1 = document.getElementById("form").elements['city1'].value, city2 = document.getElementById("form").elements['city2'].value;

    xhr.open('GET', `http://127.0.0.1:5000/city/${city1}/${city2}`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('output').innerText = xhr.responseText;
        }
    };
    xhr.send();
 }
