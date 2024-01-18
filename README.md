# COVID-19-Vaccine-Efficacy-Tracker

## DESCRIPTION

-   forecasting.py - builds an ARIMA model with 80% of data, and produces forecasts for 20% of it.
-   data_cleaning.ipynb - reads original datasets and to clean and restructure them.
-   us_state_vaccinations.csv - (original) daily vaccination count for us states.
-   us-counties.csv - (original) daily case/death count for us counties.
-   us_state_vaccinations_clean.csv - (cleaned) daily case/death count for us counties.
-   us-counties-clean.csv - (cleaned) daily case/death count for us counties.
-   us-states-clean.csv - (cleaned) daily case/death count for us states.
-   us-counties-clean-processed.csv - (manually processed on excel) daily case/death count for us counties.
-   us-counties-forecast.csv - forecasts outputted from forecasting.py
-   index.html - d3 code to present map.
-   us-counties.json - gives us county coordinates to build the d3 map.
-   lib - d3 library

## INSTALLATION

Clone the repository at https://github.com/adussa3/COVID-19-Vaccine-Efficacy-Tracker

OR

Download our team submission and access code at in CODE folder

Steps to setup data cleaning code:

1. Download Spark at https://spark.apache.org/downloads.html
2. Rename the downloaded folder to ‘spark’ and move it to your home directory. For example, /your/home/directory/spark
3. Next, install pyspark using the following command: pip install pyspark
4. Change the execution path for pyspark using the following two commands:
5. export SPARK_HOME="/your/home/directory/spark/python"
6. export PATH="$SPARK_HOME/bin:$PATH"
7. Now, pyspark is successfully installed.

Steps to setup forecasting code:

1. Make sure all the libraries are installed on the computer. Specifically "pmdarima.arima", "pmdarima", "datetime", "csv", "numpy", and "pandas".

## EXECUTION

Steps to run data cleaning code:

1. From our project's code root folder, run the following command: jupyter notebook
2. Go to the notebook in your browser, and run each cell to output the cleaned datasets.

Steps to run forecasting code:

1. To run the code, make sure the "us-counties-clean-forecast.csv" and the "forecasting.py" file are in the same directory.
2. Then in the terminal navigate to that directory and type "python forecasting.py", and the code should run and output a csv file, named "us-counties-forecast.csv" into the local directory which includes the new forecasted values for each county-state.

Steps to run index.html code locally:

1. From our project's code root folder, run the following command: python -m http.server
2. Open following url in your browser: http://localhost:8000/

Steps to access remote webpage:

1. Visit the following url to access the webpage: https://adussa3.github.io/COVID-19-Vaccine-Efficacy-Tracker/
   Note: It may take a few minutes for the webpage to fully load
