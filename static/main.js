const URL   = 'prove/';
const label = document.getElementById('label');
var count;

var init = () => {

    count = 0;

    label.addEventListener('click', () => getData());

}


var getData = () => {
    fetch(URL + count)
    .then(response => response.json())
    .then(data => handleResponse(data))
    .catch(err => label.innerText = "?");
}

var handleResponse = (data) => {
    data.flag ? window.location = data.data : label.innerText = data.data;
    count++;
}

document.addEventListener("DOMContentLoaded", init);