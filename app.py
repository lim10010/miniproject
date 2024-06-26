from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# 임시 데이터베이스 역할을 할 리스트 변수
team_members = []

@app.route('/')
def index():
    return render_template('index.html', team = team_members)


@app.route('/submit-info', methods=['POST'])
def info_storage():
    name = request.form.get('name')
    mbti = request.form.get('mbti')
    class_name = request.form.get('class_name')
    feeling = request.form.get('feeling')
    moto = request.form.get('moto')

    member = {
        'name' : name,
        'mbti' : mbti,
        'class_name' : class_name,
        'feeling' : feeling,
        'moto' : moto
    }
    team_members.append(member)

    return redirect(url_for('index'))

if __name__ == '__main__':  
    app.run(debug=True)