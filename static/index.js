 function runPythonScript() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/city/bx/ba', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById('output').innerText = xhr.responseText;
        }
    };
    xhr.send();
 }
 
console.log('test');