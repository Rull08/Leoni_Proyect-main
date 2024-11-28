from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from routes.routes import route_bp
from config import get_connection

app = Flask(__name__)
socketio = SocketIO(app)

app.register_blueprint(route_bp)

@socketio.on('execute_procedure')
def handle_execute_procedure(data):
    
    procedure_name = data.get('procedure_name')
    params = data.get('params', [])
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(f"CALL {procedure_name}({', '.join(['%s'] * len(params))});", tuple(params))
        conn.commit()
        
        emit('procedure_executed', {'status': 'success', 'message': f'Procedimiento {procedure_name} ejecutado correctamente'})
    except Exception as e:
        emit('procedure_executed', {'status': 'error', 'message': str(e)})
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    socketio.run(app, debug=True)