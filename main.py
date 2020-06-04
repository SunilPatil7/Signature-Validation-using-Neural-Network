from flask import * 
import nn
import os

app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/file_upload_form', methods = ['POST'])
def value():
    if request.method == 'POST':  
        f = request.files['file']
        os.chdir("C:/Users/patol/Desktop/images/")
        f.save(f.filename)
        new =os.path.abspath(f.filename) 
        
        id =request.form.get('id') 
        train_person_id = id
        test_image_path = new 
    #train_person_id = input("Enter person's id : ")
    #test_image_path = input("Enter path of signature image : ") 
        prediction = nn.getvalue(train_person_id,test_image_path)
        if prediction[0][1]>prediction[0][0]:
            return render_template("file_upload_form.html", result="Geniune Image")  
        else:
            return render_template("file_upload_form.html", result="Forged Image")
        

if __name__ == '__main__':  
    app.run()       
  


