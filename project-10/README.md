# Blanton Art Reccomender

### Ana Williams and Fronrich Puno

---

## Step One - Fix the Accession Number

Our first approch was to use the algorithm suggested by Issac Hammer:

```python
  for each row where the accession # is/can be a float (we dont care about the others)
    use title + artist name as query (url encoded)
    if only 1 result is returned
        update the accession # for that row as strings
    else if value is one of three that need to be manually fixed (i.e. 2002.1, 2018.16, and the 2016.5 at index 826)
        replace them with their respective fixed values as strings (i.e. 2002.10, 2018.160, and 2016.50)
    else
        replace the value with the string form of the value
```

This however proved to be too time consuming, so we went through the database and fixed the accession numbers according to the algorithm manually.

## Step Two - Filter out Rows Without Digital Images

> Sidenote: the code for this can be found in fixnum.py under the function `filter_images`

A very high-level explanation of our implimentation of step 2 was that we first queryed for pieces within the blanton collection. Then we could web-scrape the html in order to find strings. The string that we were looking for in particular was "This object does not have an image".

As pointed out by Kevin Hao, parsing a page as a JSON and detecting an image based on whether or not the 'Image' feild is populated yeilds false positives. Therefore, we decided to scrap our old approach of parsing through the JSON and used the HTML instead.

## Step Three – Judge Artwork (solo)

We created algorithm which would generate two random datasets for each of us. Within the fixnum.py file, the function name for this algorithm is `create_rand` .

> Sidenote: Each dataset is created with a different random seed
