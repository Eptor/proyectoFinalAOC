function setTokenWidth() {
    const inputToken = document.getElementById("token")
    inputToken.style.width = ((inputToken.value.lenght + 1) * 8) + 'px;'
}

function sliderChange(val) {
    document.getElementById('output').innerHTML = val;
}

function getToken() {
    var lenght = document.getElementById("count").value
    const inputToken = document.getElementById("token")
    console.log(lenght)

    const data = {
        "count": lenght
    };

    fetch('/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(
        response => response.json()
    ).then(
        data => {
            console.log(data)
            inputToken.value = data.token
        }

    ).catch(
        error => console.error(error)
    )
}

function copyText() {
    var inputToken = document.getElementById("token");
  
    inputToken.select();
    inputToken.setSelectionRange(0, 99999); // For mobile devices
  
    navigator.clipboard.writeText(inputToken.value);
  
    alert("Se copió el token");
  }