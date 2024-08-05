# navigate to project directory
Set-Location -Path "C:\Users\Erik\Desktop\Amzn-Price-Tracker"

# activate virtual environment
.\Scripts\activate.ps1

# set FLASK_APP env variable
$env:FLASK_APP = "amznpt_flaskapp/app.py"

# install requirements
pip install -r requirements.txt

# start Flask app
flask run

