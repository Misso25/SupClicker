function call_click() {
    fetch('/backend/call_click', {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        document.getElementById('coins').innerText = data.coins
    }).catch(error => console.log(error))
}
