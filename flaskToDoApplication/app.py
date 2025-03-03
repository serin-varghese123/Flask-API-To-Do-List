from flask import Flask, render_template, request, redirect, url_for

#Create Flask app instance
app = Flask(__name__ , template_folder='templates')

#Task list
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks) 


@app.route('/add', methods=['POST'])
def create_new_task():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({"task":task_text,"done":False})  
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('home'))

@app.route('/complete/<int:index>',methods=['POST'])
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']  # Toggle completion status
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)  

