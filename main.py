#This is the python music review parser that will take a special-formatted review document and convert it for use in various platforms.
#The following platforms are targeted
#-Discord: Includes proper discord markup to correclty format as well as properly format for the maximum character limit.
#-Web: Includes various HTML tagging and classes to use on my blog
#-Written: Just formats the special tagging such that it is acceptable in an essay format to be submitted elsewhere.


#General algorithm
#-Open the .odt file
#-Iterate through the entire file stream until a tag is found
#   -Process and store tag information
#   -Query for replacement if needed (artist/album RYM tags for example)
#   -Add to the final document and continue on
#Finally write output to original filename plus "-{Target}"