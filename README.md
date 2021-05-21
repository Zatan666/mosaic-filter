# mosaic-filter

## Developing stage
- [x] get how many picture to use in filtering & change that value to fit in that picture (or have user input the size of image directly)
- [x] calculate size of each grid
- [x] find values of each grid (eg. top-right top-left bottom-right bottom-left pixels)
- [x] calculate mean of RGB values in that grid
> and image that will be paste in
- [ ] paste that grid with another picture with closest RGB values
> open new problem with how to do this

### Image scraping
- [x] get more number of image by selenium webdriver (against infinite scrolling)
- [x] get original image instead of result by google search (maybe by selenium clicking and stuff)
> done with firefox, chrome webdriver

### Method to choosing image to replace in grid
- [ ] sum(abs(rgb difference))
