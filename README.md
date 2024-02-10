# Validate a South African ID number (625)
For raw project instructions see: http://syllabus.africacode.net/language-agnostic/validate-id-number/


**Author:** Fumani Masingi  
**Author Email:** juniorfumani@gmail.com

# Step 1: Clone the repository

```
git clone https://github.com/Umuzi-org/Fumani-Masingi-625-validate-a-south-african-id-number-python.git
```
then navigate to folder named Fumani-Masingi-625-validate-a-south-african-id-number-python
# Step 2: Create and activate a virtual environment
below are the steps on how to create and activate the virtual environment for both Windows and  macOS/Linux

*windows*
```
  python -m venv venv
  source venv/Scripts/activate
```

*macOS/Linux*
```
  python -m venv venv
  source venv/bin/activate
```

# Step 3: Install required dependencies
install the required dependencies using the command below. 

```
  pip install -r requirements.txt
```

# step 4: Install the package in development mode

```
pip install -e .
```

# Step 5: Run the validate_sa_id application

```
  python validate_sa_id.py
```

# Step 6: Run the tests
use the command below to run all tests

```
  pytest tests
```

# Step 7: Deactivate the virtual environment when done

```
  deactivate
```
