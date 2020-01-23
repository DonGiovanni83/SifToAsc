### Prerequisites
- python 3.7
- virtualenv (`pip3 install virtualenv`)
### Environment setup
1. Clone the repository
2. Create a virtual environment:
    
    `virtualenv sif_to_asc_env`
3. Activate the environment:
    
    `source sif_to_asc_env/bin/activate`
4. Install pip dependencies
    `pip install -r requirements.txt`
    
### Usage
` python sif_to_asc_converter.py source/directory output/directory `
### Keeping track of required packages
 `pip freeze > requirements.txt`