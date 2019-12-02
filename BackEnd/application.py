# Run a test server.
from app import application


application.run(host='0.0.0.0', port=8081, debug=False)
