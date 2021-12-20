cd libraries/resource-generator

echo // Installing Resource Generator Dependencies
$1/bin/pip install -r ./requirements.txt

echo // Building Resources
$1/bin/python index.py ../recognizers-choice/resource-definitions.json
$1/bin/python index.py ../recognizers-number/resource-definitions.json
$1/bin/python index.py ../recognizers-number-with-unit/resource-definitions.json
$1/bin/python index.py ../recognizers-date-time/resource-definitions.json
$1/bin/python index.py ../recognizers-sequence/resource-definitions.json

cd ../..
echo // Installing recognizers-text
$1/bin/python -m pip install -e ./libraries/recognizers-text/

echo // Installing recognizers-number
$1/bin/python -m pip install -e ./libraries/recognizers-number/

echo // Installing recognizers-number-with-unit
$1/bin/python -m pip install -e ./libraries/recognizers-number-with-unit/

echo // Installing datatypes-timex-expression
$1/bin/python -m pip install -e ./libraries/datatypes-timex-expression/

echo // Installing recognizers-date-time
$1/bin/python -m pip install -e ./libraries/recognizers-date-time/

echo // Installing recognizers-sequence
$1/bin/python -m pip install -e ./libraries/recognizers-sequence/

echo // Installing recognizers-choice
$1/bin/python -m pip install -e ./libraries/recognizers-choice/

echo // Installing recognizers-suite
$1/bin/python -m pip install -e ./libraries/recognizers-suite/

echo // Installing Test Dependencies
$1/bin/pip install -r ./tests/requirements.txt

echo // Running tests
$1/bin/pytest --tb=line
