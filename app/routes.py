"""from flask import request, jsonify, send_file, render_template
from . import db
from . models import Link, Click
from . utils import generate_short_code
from datetime import datetime
import pandas as pd
from io import StringIO

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/shorten', methods=['POST'])
    def shorten_url():
        data = request.get_json()
        original_url = data.get('url')
        if not original_url:
            return jsonify({'Error': 'URL requerida'}), 400
        
        short_code = generate_short_code()
        new_link = Link(original_url=original_url, short_code=short_code)
        db.session.add(new_link)
        db.session.commit()

        return jsonify({'short_url': f'{request.host_url}{short_code}'}), 201
    


    @app.route('/<short_code>', methods=['GET'])
    def redirect_url(short_code):
        link = Link.query.fiter_by(short_code=short_code).first()
        if Link:
            new_click = Click (# registrar el click
            link_id = link.id,
            ip_address=request.remote_addr,
            user_agent=request.headers.get('User-Agent')

            )
            db.session.add(new_click)
            db.session.commit()

            return jsonify({'original_url' : Link.original_url}), 302
        return jsonify({'error' : 'link no encontrado'}), 404


    @app.route('/metrics/<short_code>', methods=['GET'])
    def export_metrics(short_code):
        link = Link.query.filter_by(short_code=short_code).first()
        if link:
            clicks = Click.query.filter_by(link_id=link.id).all()
            data = [{
                'click_time': click.click_time,
                'ip_address': click.ip_address,
                'user_agent': click.user_agent
            } for click in clicks]

            df = pd.DataFrame(data)
            output = StringIO()
            df.to_csv(output, index=False)
            output.seek(0)

            return send_file(
                output,
                mimetype='text/csv',
                as_attachment=True,
                download_name=f'metrics_{short_code}.csv'
            ) 
        return jsonify({'error': 'link no encontrado'}), 404"""

from flask import request, jsonify, send_file, render_template
from . import db
from .models import Link, Click
from .utils import generate_short_code
from datetime import datetime
import pandas as pd
from io import StringIO

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/shorten', methods=['POST'])
    def shorten_url():
        data = request.get_json()
        original_url = data.get('url')
        if not original_url:
            return jsonify({'Error': 'URL requerida'}), 400
        
        short_code = generate_short_code()
        new_link = Link(original_url=original_url, short_code=short_code)
        db.session.add(new_link)
        db.session.commit()

        return jsonify({'short_url': f'{request.host_url}{short_code}'}), 201

    @app.route('/<short_code>', methods=['GET'])
    def redirect_url(short_code):
        link = Link.query.filter_by(short_code=short_code).first()
        if link:
            new_click = Click(
                link_id=link.id,
                ip_address=request.remote_addr,
                user_agent=request.headers.get('User-Agent')
            )
            db.session.add(new_click)
            db.session.commit()

            return jsonify({'original_url': link.original_url}), 302
        return jsonify({'error': 'link no encontrado'}), 404

    @app.route('/metrics/<short_code>', methods=['GET'])
    def export_metrics(short_code):
        link = Link.query.filter_by(short_code=short_code).first()
        if link:
            clicks = Click.query.filter_by(link_id=link.id).all()
            data = [{
                'click_time': click.click_time,
                'ip_address': click.ip_address,
                'user_agent': click.user_agent
            } for click in clicks]

            df = pd.DataFrame(data)
            output = StringIO()
            df.to_csv(output, index=False)
            output.seek(0)

            return send_file(
                output,
                mimetype='text/csv',
                as_attachment=True,
                download_name=f'metrics_{short_code}.csv'
            )
        return jsonify({'error': 'link no encontrado'}), 404