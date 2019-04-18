#!/bin/bash

# Define the HTML wrapper
html_beginning='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" >
   <head>
       <title>Ma galerie</title>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       <style type="text/css">
       a img { border:0; }
       </style>
   </head>
   <body>
      <p>
'

html_end='      </p>
   </body>
</html>'


# Retrieve the name of the HTML file to generate
if [ ! -z $1 ]
then
    html_file=$1
else
    html_file='gallery.html'
fi


# Define a function that will handle a picture file name
handlePicture () {
    local image_file=$1
    local thumbnail_file="thumbnails/$1"

    # Convert the picture to a thumbnail
    convert -thumbnail 200 $image_file $thumbnail_file
    
    # Add a line to integrate the thumbnail in the HTML file
    html_of_pictures="$html_of_pictures <a href=\"$image_file\"><img src=\"$thumbnail_file\" alt="" /></a>"
}


# Run the function on all .png file
html_of_pictures=""
for image_file in `ls *.png`
do
    handlePicture $image_file
done


# Generate the final html
echo "$html_beginning $html_of_pictures $html_end" > $html_file