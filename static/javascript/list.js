document.addEventListener('DOMContentLoaded', function() {
    //get the name of the list from localStorage
    var buttonName = localStorage.getItem('buttonName')
    //display the name in the heading
    document.getElementById("heading").innerHTML = buttonName + "'s Christmas List"

    //get the name of the user from localStorage
    username = localStorage.getItem('username')
    //check if the username pressed their own button
    //They are only allowed to edit their own list.
    if (username!=buttonName){
        document.getElementById('additem').style.display='none';
        var removeButtons = document.getElementsByClassName('remove');
        for (var i = 0; i < removeButtons.length; i++) {
            removeButtons[i].style.display = 'none'; 
        }
    }
});