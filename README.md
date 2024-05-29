#   ____       _       ____  _ _       
#  |  _ \ __ _| |_ ___| __ )(_) |_ ___ 
#  | |_) / _` | __/ _ \  _ \| | __/ _ \
#  |  _ < (_| | ||  __/ |_) | | ||  __/
#  |_| \_\__,_|\__\___|____/|_|\__\___|
#                                      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀

# RateBite
:dollar: :euro: :yen: :pound: :moneybag:

A simple project

## Structure

Project has the below structure:
    ```sh
    C:.
    |   enviroment.yml
    |   README.md
    |   requirements.txt
    |
    +---ratebite_project
    |   |   main.py
    |   |   postgres.sql
    |   |   __init__.py
    |   |
    |   +---config
    |   |   |   db_config.py
    |   |   |   __init__.py
    |   |
    |   +---db_connections
    |   |   |   base_db.py
    |   |   |   load_data.py
    |   |   |   mariadb_db.py
    |   |   |   postgres_db.py
    |   |   |   sqlite_db.py
    |   |   |   __init__.py
    |   |
    |   +---features
    |   |   |   data_class.py
    |   |   |   fetch_data.py
    |   |   |   fetch_data_class.py
    |   |   |   transform_data.py
    |   |   |   transform_data_class.py
    |   |   |   __init__.py
    |   |
    |   +---ratebite
    |   |   |   cli.py
    |   |   |   __init__.py
    |   |   |   __main__.py
    |   |
    |   +---texts
    |   |       intro.txt
    |
    \---tests
        |   test_download_rates.py
        |   __init__.py


## Installation

The below are clear instructions for both `pip` and `conda` users on how to install necessary Python packages for the project.

### Using pip

1. Clone the GitHub repository:
   ```sh
   git clone https://github.com/username/repository.git

2. Navigate to the repository directory:
   ```sh
   cd repository
  
3. Install the packages using pip:
   ```sh
   pip install -r requirements.txt
   
### Using conda

1. Clone the GitHub repository:
   ```sh
   git clone https://github.com/username/repository.git
   
2. Navigate to the repository directory:
   ```sh
   cd repository
   
3. Create a conda environment (optional but recommended):
   ```sh
   conda create --name myenv python
   conda activate myenv
   
4. Install the packages via conda environment.yml
   ```sh
   conda env create -f environment.yml
   conda activate myenv
