function getUser() {
    //get the user's name when submit is clicked
    var username = document.getElementById("username").value;
    //store user's name to access it in list.js
    localStorage.setItem('username', username);
}