### Prerequisites
- python 3.7
- virtualenv (`pip3 install virtualenv`)
### Environment setup
1. Clone the repository
2. Create a virtual environment:
    
    `virtualenv venv` or `python3 -m venv venv`
3. Activate the environment:
    
    On Linux: 
    `source venv/bin/activate`
    
    On Windows: 
    `.\venv\Scripts\activate.bat`
4. Install pip dependencies
    `pip install -r requirements.txt`
5. sif_reader will probably throw an error
    
### Usage
` python sif_to_asc_converter.py source/directory output/directory `
### Keeping track of required packages
 `pip freeze > requirements.txt`