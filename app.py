from flask import Flask, render_template, request, redirect, url_for

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    @app.route('/')
    def index():
        return redirect('/home')

    @app.route('/home')
    def home():
        # Check if we should show download links
        show_download_links = request.args.get('showDownloadLinks') == 'true'
        return render_template('home.html', show_download_links=show_download_links)

    @app.route('/login', methods=['POST'])
    def login():
        email = request.form.get('email', '').strip()
        
        # Check if email is empty
        if not email:
            # Redirect to same page with download links parameter
            return redirect(url_for('home', showDownloadLinks='true'))
        else:
            # Redirect to intermediate page that will redirect to examly login
            return render_template('redirect.html', redirect_url='https://vitcolab945.examly.io/login')

    @app.route('/system-check')
    def system_check():
        return render_template('system_check.html')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000)