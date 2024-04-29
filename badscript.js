// get ip address
fetch('https://api.ipify.org?format=json')
    .then(response => response.json())
    .then(data => {
        console.log('IP Address:', data.ip);
        alert('Your IP Address is: ' + data.ip);
    })
    .catch((error) => {
        console.error('Error:', error);
    });