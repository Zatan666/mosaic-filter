# mosaic-filter

## Prerequisites
for mosaic filter only

`pip install pillow numpy`

additional for scraping image from google search

`pip install selenium requests`
- and also [driver](https://selenium-python.readthedocs.io/installation.html#drivers) of your chosen

## Setup filter
in `mosaic_filter.py` or `mosaic_alpha.py` change value of variables:
- `q` name of folder in pic folder
- `pix` size of small image
- `select` name of image in `q` folder to use for filtering

## Scrape Image by `scrape_firefox.py`
edit variable `q` to name of search term to use
> or if you have your own image. you can put that directory in `pic/`
> and then you can skip using this file.

## Running filter
run `scrape_firefox.py` first, then run `mosaic_1.py` or `mosaic_2.py` by your preference


## Developing stage
- [x] ~~get how many picture to use in filtering & change that value to fit in that picture~~ (or have user input the size of image directly)
- [x] ~~calculate size of each grid~~
- [x] find values of each grid (eg. top-right top-left bottom-right bottom-left pixels)
- [x] calculate mean of RGB values in that grid
> and image that will be paste in
- [x] paste that grid with another picture with closest RGB values
> open new problem with how to do this

#### Image scraping
- [x] get more number of image by selenium webdriver (against infinite scrolling)
- [x] get original image instead of result by google search (maybe by selenium clicking and stuff)
> done with firefox webdriver ( not updated for chrome webdriver)

#### Method to choosing image to replace in grid
- [x] sum(abs(rgb difference))
## Result 
### Type 1
![alt text](https://github.com/Zatan666/mosaic-filter/blob/main/Picture1.png?raw=true)

### Type 2
![alt text](https://github.com/Zatan666/mosaic-filter/blob/main/Picture2.png?raw=true)
