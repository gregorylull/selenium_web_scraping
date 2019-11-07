## TL;DR:
Take a look at the last example and open up the python file to see more info on how to run it. It will:
1. read in command line arguments to get a range of urls to read.
2. read in a .csv file with urls and create a dataframe.
3. set options to make chrome headless.
4. loop through the dataframe to get a url and scrape that url.
5. save a .png to demonstrate that the code ran correctly.
6. open up multiple terminals to run in parallel.

## The Problem
You need to scrape 36,000 pages, if each page takes 1 second that is 10 hours if you scrape your pages sequentially one after another (36000 pages * 1 second / 60 sec / 60 mins).

You don't want to take 10 hours, you want to take ~1 hour, so instead of scraping sequentially you should try scraping in parallel and run 10 instances of selenium (36000 pages * 1 second / 60 sec / 60 mins / 10 instances)

Warning: remember that webpages typically will limit how often you can visit the page, so add some random sleep times in between ```driver.get(url)```, especially when running instances in parallel.

This code works for macOS 10.14, python 3.7, chrome 78. Remember to activate your environment.

## Examples

### Reading params from the command line
The script ```read_script_parameters.py``` demonstrates how to read parameters from the command line.
1. extracts the filename from the command line.
2. create a dict and save as pickle, use the extracted filename.
3. read the pickle file above
4. use the data from the pickle file to print something

```python
python read_script_parameters.py some_data.pkl

# expected output is:
'hello world'

```

### Scraping a webpage by passing in a parameter
The script ```scrape.py``` demonstrates how to read parameters from the command line and scrape a url.

1. extracts the argument from the command line and check dictionary
2. get the url from the dictionary
3. scrape the url
4. save the screenshot of the page just to demonstrate that work can be done.

```python
python scrape.py url1

# it will save a file called screenshot-url1.png, and the output is
'Finished scrape.py url1'

```

### Scraping a webpage with headless chrome
The script ```scrape_headless.py``` demonstrates how to read parameters from the command line and scrape a url but without a chrome window popping up (headless).

1. extracts the argument from the command line and check dictionary
2. get the url from the dictionary
3. set the options for chrome to be headless
4. scrape the url
5. save the screenshot of the page just to demonstrate that work can be done.

```python
python scrape_headless.py url1

# it will save a file called screenshot-headless-url1.png, and the output is
'Finished scrape_headless.py url1'

```

### Scraping a webpage with headless chrome and in parallel
The script ```scrape_headless_from_files.py``` demonstrates how to read parameters from the command line and use headless chrome. Also demonstrates how you can "split" a file up by giving the code a range to scrape.
Open multiple terminal windows to run in parallel.

1. extracts the arguments from the command line for the file to open, and the start and stop indexes. 
2. read the .csv file and create a dataframe.
3. create a subset of the dataframe given the start and end indexes.
3. loop through each row of the subset and get the url
4. scrape each url
5. save the screenshot of the page just to demonstrate that work can be done.

```python
# It is saying open up the urls.csv file, and scrape urls from index 0 up to and not including index 12.
python scrape_headless_from_files.py urls.csv 0 12

# it will save multiple file called screenshot-headless-files-<page>.png, and the output is
'saved screenshot 0'
'saved screenshot 1'
'...'
'saved screenshot 11'
'Finished scrape_headless_from_files.py urls.csv 0 12'
```

