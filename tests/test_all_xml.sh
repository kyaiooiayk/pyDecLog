cp ../pyDecLog.py .
python -m coverage run -m unittest
python -m coverage report
python -m coverage xml
rm ./pyDecLog.py
