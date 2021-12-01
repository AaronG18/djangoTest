function getInfo(){
    var txt = document.getElementById("message").value;

    if (txt) {
        alert("Your messageL "+txt+ ", is sent out");
    } else {
        alert("please leave a message");
    }
}