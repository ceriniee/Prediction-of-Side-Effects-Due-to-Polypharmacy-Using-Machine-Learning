# Development Notes: Dec. 2021 ~ June 2022

Project Start Date: December 2021

## December 2021 
* I set up the development environment. 
* There were many trials and errors. 
  * First, I tried to work with my local computer (Mac). 
    * My Mac does not have a vram. 
  * So I also tried to work with a Windows computer that has a GPU (RTX 2070 SUPER) and set up a virtual machine (VM). 
    * The Windows desktop had 6 gigabytes of GPU vram, while we needed at least 8-10 gigabytes of GPU vram. 
  * Then, finally, I decided to work with Google Colab as it provided 12+ gigabytes of GPU vram.


## January 2022
* I read through and studied the paper written on [Tri-graph Information Propagation for Polypharmacy Side Effect Prediction (TIP)](https://grlearning.github.io/papers/94.pdf) by Xu, Sang, and Lu. 

## February ~ March 2022
* I read through and studied the code of the TIP project. 
* There were a couple of problems: 
  * Problem 1: The type did not match. 
    * Solution 1: I had to complete type matching. 
    * Problem 2: There were version errors. 
      * Our version and the code’s version was different. 
        * Solution 2: We downgraded, but it still did not work. 
  * Problem 3: There was no saved model. 
    * We added a saved model. 
* We chose TIP-cat mode. 
  * Problem 4: Inefficient code, when called tip-cat, brought another unnecessary one
    * We adjusted the code to be more efficient. This increased the running speed. 
* We made edits to some parts of the code so that the program is easier to use. 

## April 2022

### April 4, 2022
* We installed the Python module Selenium. 
  * This was because we needed the online database. 
  * Selenium is a fast and easy method for data crawling. 
* I introduced myself to web scrpping through Google searching and research. 
  * I learned web scraping through various websites. 
    * [https://www.scrapingbee.com/blog/selenium-python/](https://www.scrapingbee.com/blog/selenium-python/)
    * [https://www.analyticsvidhya.com/blog/2020/08/web-scraping-selenium-with-python/](https://www.analyticsvidhya.com/blog/2020/08/web-scraping-selenium-with-python/)
* I tested what I learnt through web scraping on [Google](www.google.com) and [PubChem](https://pubchem.ncbi.nlm.nih.gov/)

### April 11, 2022
* What is XPath? 
  * I learned how to use XPath through Google searching. 
    * [https://selenium-python.readthedocs.io/locating-elements.html](https://selenium-python.readthedocs.io/locating-elements.html)
    * [https://wkdtjsgur100.github.io/selenium-xpath/](https://wkdtjsgur100.github.io/selenium-xpath/)
    * [https://www.geeksforgeeks.org/find_element_by_xpath-driver-method-selenium-python/](https://www.geeksforgeeks.org/find_element_by_xpath-driver-method-selenium-python/)

### April 25, 2022
* I tried to search both drugs and medicines from the dataset on PubChem. 
* I got the Chem IDs (CIDs) of the drugs. 

## May 2022

### May 2, 2022
* I encountered a problem: 
  * For some drugs, best matches do not exist. 
    * The id or the XPath of the table and div aren’t the same, so there is a bug. 
* The solution that I thought of was: 
  * Unite the system by going into the name after finding the best match. 
    * I need to know how to find best match and how to click on the name of the best match. 

### May 16, 2022
* I thought of a new method: 
  * Search one drug first, get its CID, then search the second by selecting all and deleting the first drug’s name from the search bar. 
* The issue was that: 
  * 1. The model has to learn the dataset. 
    * I imported dataset using csv pandas. 
  * 2. There needs to be searching. 
    * The actual running of the model and the user inputs are separate. 
    * If they are different, prediction is difficult. 

### May 23, 2022
* Goal: Enable searching with CID number
* The definition of regular expression gave me a hint. 
  * r'(\d+)' is a regex pattern for at least one digits located together. 
  * str.extract(r'(\d+)', expand=False) → extract digits that are located together (separately)
* Separated dataframe by column
* Deleted CID and the zeroes (data cleansing) for column 1 and 2 (about 4000000 rows each)
* United data types
* I searched with CID number. 
  * The numbers had to match and have a side effect in order for the system to successfully find a possible side effect. 

### May 29, 2022
* Problem: I found a bug. 
  * The cid could be found not only in div but in table. 
* Solution: I unified the path to all tables. 
  * I reconnected the XPath and did crawling again. 

## June 2022

### June 5, 2022
* Problem 1: XPath Error
  * Occurred even when we copied XPath directly from inspect
* Solution 1: found that it was because we did not wait
  * The program was unable to locate the element. 
* Problem 2: TimeoutException
* Solution 2: Change element_to_be_clickable to presence_of_element_located
  * Element was never clickable, so waiting for it to be clickable would not make sense. 

### June 12, 2022
* Problem 1: XPath still did not work
* Solution 1: use the most specific div for the first
* Problem 2: The first drug name did not delete before putting in the second drug name
* Solution 2: Find searchbar, send_keys(Keys.COMMAND + ‘a’) and send_keys(Keys.DELETE) 
* I checked if other drug combinations worked. 

### June 19, 2022
* I created an account on Github in order to create a portfolio of my polypharmacy project. 
* Using various sites on Google, I learned markdown languages and how to use Github. 
  * [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  * [https://www.datacamp.com/tutorial/git-push-pull](https://www.datacamp.com/tutorial/git-push-pull)
  * [https://chancoding.tistory.com/76](https://chancoding.tistory.com/76)
  * [https://github.com/git-guides/git-push](https://github.com/git-guides/git-push)

### June 27, 2022
* I uploaded my project on Github. 
* I edited and added details to my development notes. 

### July 3, 2022
* I wrote the README section. 

### July 10, 2022
* I edited the README section. 

### July 17, 2022
* I started uploading my TIP data files onto my Github portfolio. 
* Problem 1: I could not upload files that were larger than 25 mb through the browser. 
  * Solution 1: I had to push the file through terminal. 
  * [https://stackoverflow.com/questions/61040990/upload-file-25-mb-on-github](https://stackoverflow.com/questions/61040990/upload-file-25-mb-on-github)
  * [https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
* Problem 2: The push did not work. 
  * Solution 2: The system could not push the file because the system confused location. I created another folder separate for the files that I was going to push. 
* Problem 3: The push still did not work. 
  * Solution 3: I realized that I did not do git init in terminal, and that was the reason behind the problem. I solved this problem by going back and doing git init. 
