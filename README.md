					       ____       _       ____  _ _       
					      |  _ \ __ _| |_ ___| __ )(_) |_ ___ 
					      | |_) / _` | __/ _ \  _ \| | __/ _ \
					      |  _ < (_| | ||  __/ |_) | | ||  __/
					      |_| \_\__,_|\__\___|____/|_|\__\___|
								
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
					⠀⠀⠀⠀⠀⠀⠀       ⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀


# :chart_with_upwards_trend: **RateBite**: Your Ultimate CLI for Exchange Rate Management :chart_with_downwards_trend:  :dollar: :euro: :yen: :pound: :moneybag:


Welcome to RateBite, a powerful and flexible CLI tool designed to streamline your exchange rate data workflows. Whether you're a developer, data scientist, or finance professional, RateBite provides an intuitive interface for downloading, validating, transforming, and managing exchange rate data.

## Introduction
In today's fast-paced world, where users, investors, scientists, and various professionals need to stay informed and make quick decisions, real-time data monitoring has become indispensable. Whether it's tracking market trends, analyzing investment opportunities, or conducting research, having up-to-date information at your fingertips is crucial.

One area where real-time data monitoring is particularly critical is in currency exchange rates. Fluctuations in exchange rates can have significant impacts on various aspects of our lives, from travel expenses to international trade deals. That's where RateBite comes in.

RateBite is your ultimate CLI tool for exchange rate management. With its powerful features and intuitive interface, RateBite simplifies the process of monitoring and managing exchange rate data. By downloading exchange rate data from online sources and injecting them into a database, RateBite makes real-time monitoring a piece of cake.


## :computer: Projet Structure

Project has the below structure:

   ```
	.
	└── ratebite:.
		├── │   enviroment.yml                    # Environment configuration file
		├── │   LICENCE                           # License file
		├── │   README.md                         # Project README
		├── │   requirements.txt                  # Python dependencies file
		├── |
		├── +---src                               # Source code directory
		├── |   |   main.py                       # Main Python script
		├── |   |   __init__.py                   # Python package initializer
		├── |   |
		├── |   +---config                        # Configuration directory
		├── |   |   |   db_config.py              # Database configuration module
		├── |   |   |   __init__.py               # Configuration package initializer
		├── |   |
		├── |   +---cron                          # Cron job directory
		├── |   |       cronjob.md                # Cron job markdown file
		├── |   |
		├── |   +---data                          # Data directory, in case needed
		├── |   |
		├── |   +---db_connections                # Database connections directory
		├── |   |   |   base_db.py                # Base database module
		├── |   |   |   load_data.py              # Data loading module
		├── |   |   |   mariadb_db.py             # MariaDB database module
		├── |   |   |   postgres_db.py            # PostgreSQL database module
		├── |   |   |   sqlite_db.py              # SQLite database module
		├── |   |   |   __init__.py               # Database connections package initializer
		├── |   |
		├── |   +---DDL                           # Data Definition Language directory
		├── |   |       database_entities.sql     # Database entities DDL script
		├── |   |
		├── |   +---features                      # Feature modules directory
		├── |   |   |   data_class.py             # Data class module
		├── |   |   |   fetch_data_class.py       # Data fetching class module
		├── |   |   |   transform_data_class.py   # Data transformation class module
		├── |   |   |   __init__.py               # Features package initializer
		├── |   |
		├── |   +---ratebite                      # Ratebite package directory
		├── |   |   |   cli.py                    # Command-line interface module
		├── |   |   |   __init__.py               # Ratebite package initializer
		├── |   |   |   __main__.py               # Main module
		├── |   |
		├── |   +---texts                         # Text files directory
		├── |   |       intro.txt                 # Introduction text file
		├── |
		└── \---tests                             # Test directory
			├── |   test_cli_arguments.py         # CLI arguments test module
			└── |   __init__.py                   # Test package initializer
   ```

## :fire: Getting Started

The below are clear instructions for both `pip` and `conda` users on how to install necessary Python packages for the project.

### Installation Using pip

1. Clone the GitHub repository:

   ```
   git clone https://github.com/anasmpit/ratebite.git
   ```

2. Navigate to the repository directory:

   ```
   cd repository
   ```
  
3. Install the packages using pip:
   
   ```
   pip install -r requirements.txt
   ```
   
### Installation Using conda

1. Clone the GitHub repository:

   ```
   git clone https://github.com/anasmpit/ratebite.git
   ```
   
2. Navigate to the repository directory:

   ```
   cd repository
   ```
   
3. Create a conda environment (optional but recommended):

   ```
   conda create --name myenv python
   conda activate myenv
   ```
   
4. Install the packages via conda environment.yml

   ```
   conda env create -f environment.yml
   conda activate myenv
   ```

### Configuration
RateBite downloads data and stores them to a RDBMS. Here is a (up to date) list of supported systems:
* PostgreSQL
* MariaDB
* SQLite

Make sure to have already installed one of the above with specific credentials. Then pass them to 
[db_config](https://github.com/anasmpit/ratebite/blob/main/src/config/db_config.py) file.

Most of online resources need an API key for downloading data. Make sure to get one and use it.

### Executing the Code
After installing the necessary packages, open a command prompt (CMD) window. Navigate to the root directory of the project by using the "cd" command. Once you're in the root directory, type the following command:

   ```
   python -m src.ratebite --description
   ```
	
Hit enter, and voila! RateBite is up and running, ready to serve you.

#### Help
You can always search of help by typing:

   ```
   python -m src.ratebite --help
   ```
 
where you get a list of available flags.

#### Keep in mind

Here are some basic instructions:

* The default CLI command imports data only for the current date without any arguments:

   ```
   python -m src.ratebite
   ```
	
* The CLI command can also accept two arguments, start_date and end_date, for backfilling or re-importing specific dates. Use the flags --start-date or -s and --end-date or -e. Ensure that dates are strictly in the format %Y-%m-%d:

	```
	python -m src.ratebite --start-date 2024-05-27 --end-date 2024-05-27
	```

* The --start-date flag can be used alone to download all data from the given date to the current date:

	```
	python -m src.ratebite --start-date 2024-05-27
	```

* The --end-date flag cannot be used alone; it must be used in conjunction with --start-date.

#### Example
Let's try to download exchange rates for period from 2024-05-25 to 2024-05-28.

	python -m src.ratebite --start-date 2024-05-25 --end-date 2024-05-28
 
then the CLI informs us about fetching the data and converting them

	----- RageBite Initialize -----


	Fetching online exchange rates at: 2024-05-29.


	Fetching data for 2024-05-25 from historical.json.
	Fetching data for 2024-05-26 from historical.json.
	Fetching data for 2024-05-27 from historical.json.
	Fetching data for 2024-05-28 from historical.json.
	Exchange rates for USD to EUR, for each date.
	
Then, the connections with the Database are established via a connector

	Connections established.
	Loading data by connector.
	
CLI informs us that any existing dates in database overlapping with fetched are replaced

	Overwriting existing records for dates: {'2024-05-27', '2024-05-28', '2024-05-24', '2024-05-25', '2024-05-29', '2024-05-26'}.
	The above are being replaced by the new ones.
	
Next is a table of today's rates

	---- Today's rates.
	+-----------------+-------------------+-----------------+
	| Currency date   | Currency symbol   |   Currency rate |
	|-----------------+-------------------+-----------------|
	| 2024-05-29      | KES               |     0.00707841  |
	| 2024-05-29      | KGS               |     0.0105197   |
	| 2024-05-29      | KHR               |     0.000226122 |
	| 2024-05-29      | KMF               |     0.00204192  |
	| 2024-05-29      | KPW               |     0.00102743  |
	| 2024-05-29      | KRW               |     0.000674879 |
	| 2024-05-29      | KWD               |     3.01288     |
	| 2024-05-29      | ZAR               |     0.0502364   |
	| 2024-05-29      | ZMW               |     0.0342564   |
	| 2024-05-29      | ZWL               |     0.00287169  |
	| 2024-05-29      | GGP               |     1.17575     |
	| 2024-05-29      | GHS               |     0.0630553   |
	| 2024-05-29      | GIP               |     1.17575     |
	|     ...         | ...               |     ...         |
	+-----------------+-------------------+-----------------+
	
And finally, statistics per month for all dates in database

	---- Some rate statistics per month.
	+------------+-------------+------------+--------------+
	|   Min Rate |    Max Rate |   Avg Rate | Month/Year   |
	|------------+-------------+------------+--------------|
	|    63882.9 | 1.02803e-05 |    398.555 | May 2024     |
	+------------+-------------+------------+--------------+
	
At the end, cursors and connections close.

	Cursor closed.
	Connection closed.

:no_entry_sign: In case any error occurs, then there is a rollback and transactions are never commited!
