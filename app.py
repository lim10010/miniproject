from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 데이터베이스 역할을 할 리스트 변수
team_members = []

@app.route('/')
def index():
    return render_template('index.html', team=team_members)


# 여행자 정보 입력
@app.route('/submit-info', methods=['POST'])
def info_storage():
    name = request.form.get('name')
    mbti = request.form.get('mbti')
    class_name = request.form.get('class_name')
    feeling = request.form.get('feeling')
    moto = request.form.get('moto')

    member = {
        'name': name,
        'mbti': mbti,
        'class_name': class_name,
        'feeling': feeling,
        'moto': moto
    }
    team_members.append(member)

    return redirect(url_for('index'))

# 여행자 정보 수정
@app.route('/edit-info', methods=['POST'])
def edit_info():
    name = request.form['editName']
    mbti = request.form['editMbti']
    class_name = request.form['editClass']
    feeling = request.form['editFeeling']
    moto = request.form['editMoto']
    
    # Find the member in the team and update their info
    for member in team_members:
        if member['name'] == name:
            member['mbti'] = mbti
            member['class_name'] = class_name
            member['feeling'] = feeling
            member['moto'] = moto
            break
    
    return redirect(url_for('index'))

# 여행자 정보 삭제
@app.route('/delete-info', methods=['POST'])
def delete_info():
    name = request.form['name']
    
    # Find and remove the member from the team
    global team_members
    team_members = [member for member in team_members if member['name'] != name]
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
