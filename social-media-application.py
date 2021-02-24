from flask import flask, render_template, request
from flask_cors import CORS

    app = flask(__name__)

    CORS(app)

    @app.route('/', methods= ['GET','POST'])
    def index():
        if request.method == 'GET':
            pass

        if request.method == 'POST':
            name = request.form.get('name')
            post = request.form.get('post')  
            create_post(name, post)


        posts = get_posts()

    
        return render_template('social-media-app.html', posts=posts)

if __name__ =='__main__':
    app.run(debug=True)