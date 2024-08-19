# **Fetch Automation Assignment**

## **Overview**

This project is an automated solution for the "Find the Fake Gold Bar" problem using Selenium WebDriver. The solution involves interacting with a web page to simulate the process of identifying a fake gold bar among several using a balance scale.

&nbsp;

### **Python and pip Installation**

- **macOS**:
  - Python 3 and pip3 are usually pre-installed. You can download the latest version of Python [here](https://www.python.org/downloads/).
  -  To check if pip is installed, run:             pip3 --version
  - If pip is not installed, you can download it by running:             curl <https://bootstrap.pypa.io/get-pip.py> -o get-pip.py
  - And install it by running
&nbsp;           python3 get-pip.py

- **Windows**:
  - Download and install the latest version of Python [here](https://www.python.org/downloads/).
  - During installation, ensure you check the box that says **Add Python to PATH**.
  - **pip**: pip is installed automatically with Python 3. To verify, open Command Prompt and run:           pip --version If pip is not installed, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

&nbsp;

### **Project Setup**

**1\. Clone the Repository**

git clone <https://github.com/chrisbouy/FetchAutomationAssignment.git>

&nbsp;

**2\. Set Up a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies.

**macOS**:

**Create a virtual environment**

python3 -m venv .venv

**Activate the virtual environment**

source .venv/bin/activate

**Windows**

**Create a virtual environment**

python -m venv .venv

**Activate the virtual environment**

.venv\Scripts\activate

&nbsp;

**3\. Install Project Dependencies**

Once the virtual environment is activated, install the project dependencies using pip:

pip install -r requirements.txt

&nbsp;

**Running the Tests**

To run the tests, ensure your virtual environment is activated, and then use the following command:

pytest -s
