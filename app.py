from flask import Flask, send_file, render_template, request, redirect, session, send_from_directory
import pickle

app = Flask(__name__)

#initialize currentUser
currentUser = "guest"


#This brings the user to the next
#page if their info is found in the users dictionary
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data for username and password
        username = request.form.get('username')
        password = request.form.get('password')

        # Open the serialized user info file
        f = open("User.info", 'rb')
        UserInfo = pickle.load(f)

        #check if the dictionary contains a key-value
        #pair of this username and password
        if UserInfo[username] == password:
            #change the currentUser variable
            currentUser = username #update currentUser on login
            #if the login info exists, direct the user to lists page
            return render_template('lists.html')
        else:
            print("Login failed!")

    return render_template('login.html')

@app.route('/lists.html')
def lists():
    if request.method == 'POST': 
        #when a list putton is clicked
        #get button name with json
        buttonName = request.json.get('button_name')

        #open list file and find the list for that person
        f = open('Christmas.lists', 'rb')
        Lists = pickle.load(f)
        List = Lists[buttonName]
        f.close()

        #send the list back to 
        return render_template("list.html", ListData=List)


    return render_template('lists.html')

@app.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'POST':
        data=request.get_json()
        username = data.get('username')
        #when a user submits adds a new item
        #bring it back to the server
        newItem = request.form.get('newitem')
        #open the file with all of the gift lists
        with open("Christmas.lists", 'rb') as f:
            ChristmasLists = pickle.load(f)

        #update the dictionary for the correct user
        #false means the gift has not been purchased
        for List in ChristmasLists:
            if List.get(username):
                List[newItem] = 0
        with open("User.info", "wb") as f:
            pickle.dump(ChristmasLists, f)

    return render_template('list.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
