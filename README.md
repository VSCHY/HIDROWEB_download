# BR_HIDROWEB_Dis
Download monthly discharge from HIDROWEB hydrological stations (Brazil) with a python script. (for Linux)

## Getting Started

### Prerequisites

You need to install the following packages for python 3 :

```
- pandas
- selenium
- geckodriver (available from conda-forge)
```

### Installing

Before running the script you have to

```
1) Fill the station.csv with the stations you are interested in. One station per line with the following format:
id,name
The id is the reference code for the station and the name is the exact name (or part of it) of the station. (if the name you write differ from the name in the database it may generate error.

2) Complete the directory in which you want the discharge to download: it's the variable homedir in the "start.py" file.

3) Run the "main.py" file, for example in linux terminal :
> python3 ./main.py

4) Be careful, you will have to resolve a captcha ! 
```

## Running the tests

If you want to test the script, the stations.csv file is already filled with the station Porto Murtinho. You just have to make the step 3 and 4.

## Output

In the directory you defined you will find a new sub-directory named "BR-Porto_Murtinho" for the station Porto Murtinho for example. It will contain the data for the station and the csv / excel file for the monthly discharge.


## Authors

* **Anthony Schrapffer**

## MORE

If you have some suggestions, problems, or some idea to improve this code/project, just contact me ! :)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.md](LICENSE.md) file for details
