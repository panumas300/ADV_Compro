from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:SPYatb32373@node1247-rachpython.th.app.ruk-com.cloud:11001/testdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:YKHvca91771@node17329-panumas.app.ruk-com.cloud:11104/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Comments(db.Model):
    __tablename__ = 'comments'
    name = Column(String, primary_key=True)
    comment = Column(String)


@app.route('/')
def index():
    result = Comments.query.all()
    return render_template('index7.html', result=result)


@app.route('/sign')
def sign():
    return render_template('sign7.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)