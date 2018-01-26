$(document).ready(function() {
    isLoggedIn();
    $("#setSensor").submit(function() {
        $.ajax({
            url: "http://192.168.42.69:8080/api/addSensor",
            headers: {Token: sessionStorage.getItem('access-token')},
            data: {id: $('#sensorId').val(), area: $('#area').val()},
            type: 'POST',
            dataType: "json"})
            .done(function(data){
                if(data.auth)
                    alert(data.message);
                else
                    alert(data.error);
            })
            .fail(function(data, status){
                alert("Devi eseguire l'accesso per poter accedere ai dati. Cliccando su 'OK' verrai reindirizzato alla pagina di accesso!");
                window.location.replace("./login.html");
            });
        return false;
    });
});

function isLoggedIn(){
    if(isEmpty(sessionStorage.getItem('access-token'))){
        alert("Devi eseguire l'accesso per poter accedere ai dati. Cliccando su 'OK' verrai reindirizzato alla pagina di accesso!");
        window.location.replace("./login.html");
    }
}

function isEmpty(obj) {
    for (var key in obj) {
        if (hasOwnProperty.call(obj, key)) return false;
    }
    return true;
}

function logout(){
    sessionStorage.removeItem('access-token');
    window.location.replace("./login.html");
}
