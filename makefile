# To run from source:
#     $ bash configure
#     $ make run

# Use to run commands in the virtual environment
INVENV = . env/bin/activate ;

Makefile.local:
	echo "You must run the 'configure' script before using make"

include Makefile.local

# Set up and enter virtual environment
env:
	$(PYVENV)  env
	($(INVENV) pip install -r requirements.txt )

# Start server
service:
	echo "Launching gunicorn background process"
	($(INVENV) gunicorn --bind="0.0.0.0:8080" server:app )&

# Start server with debugging enabled
run: env
	($(INVENV) python3 server.py) || true

# Run tests
test: env
	$(INVENV) nosetests

# Create dependency list
dist: env
	$(INVENV) pip freeze >requirements.txt

# Stay tidy
clean:
	rm -f *.pyc
	rm -rf __pycache__

# Will require reinstallation to run again
veryclean:
	make clean
	rm -rf env/
	rm -f Makefile.local
