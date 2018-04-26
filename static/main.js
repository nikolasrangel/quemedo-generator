const URL   = 'prove/';
const URL_REDIRECT = 'https://www.wikihow.com/Stop-Procrastinating';
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
    .catch(err => console.error(err));
}

var handleResponse = (data) => {
    if(data.flag){
        window.location = URL_REDIRECT;
    }else
        label.innerText = data.data;
    count++;
}

document.addEventListener("DOMContentLoaded", init);