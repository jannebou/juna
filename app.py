from flask import Flask, render_template, request

app = Flask(__name__)

# define a list to store the train data
train_data = []

@app.route('/')
def index():
    return render_template('mittaukset.html', train_data=train_data)

@app.route('/upload', methods=['POST'])
def upload():
    # get the train number and delay minutes from the form data
    train_number = request.form['train_number']
    delay_minutes = request.form['delay_minutes']
    
    # add the train data to the list
    train_data.append((train_number, delay_minutes))
    
    # render the updated data table
    return render_template('mittaukset.html', train_data=train_data)

if __name__ == "__main__":
    app.run(debug=True)