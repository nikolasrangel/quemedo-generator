const URL_TO_FETCH = 'https://como-ousas.herokuapp.com/api/prove/1';

var getData = () => {
    fetch(URL_TO_FETCH)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
}
