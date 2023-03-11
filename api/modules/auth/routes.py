from flask import request, jsonify
import jwt, os, psycopg2, re
from hashlib import sha256

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSW')
    )

def init_routes(app):
    @app.route('/auth/register', methods=['POST'])
    def registration():
        SIMPLE_USER_ROLE = 0
        
        request_data = request.get_json()
        if 'email' in request_data and 'password' in request_data and re.match('^[\w\.]+@([\w]+\.)+[\w]+$', request_data['email']):
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO users(email, password, role) VALUES'
                '(%s, %s, %s);'
            , (request_data['email'], sha256(request_data['password'].encode('utf-8')).hexdigest(), SIMPLE_USER_ROLE))
            # print("\n\n", cur.mogrify('SELECT * FROM users WHERE email = %s;', request_data['email']))
            cur.execute('SELECT * FROM users WHERE email = %s;', (request_data['email'],))
            created_user = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()

            return jsonify(created_user), 201
        
        
        return jsonify({ 'error': True, 'message': 'Provide right email and password to create a user' }), 400
