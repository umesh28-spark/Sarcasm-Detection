from flask import Flask,render_template,request
import pickle

with open("sarcasm.pkl","rb")as f:
    model=pickle.load(f)

with open("sarcasm_vect.pkl","rb")as f:
    vectorizer=pickle.load(f)
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def new():
    if request.method=='POST':
        headline=request.form['headline']
        user_input=vectorizer.transform([headline])
        predictions=model.predict(user_input)
        if predictions==1:
            prediction="Sarcastic"
        else:
            prediction="Not sarcastic"
        return render_template("index.html",prediction=prediction)
    return render_template("index.html")



    
app.run()