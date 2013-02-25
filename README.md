# diaspora-export

Diaspora’s data export function is crap because it doesn’t include your posts (or didn’t for me, at lest). This script, given your profile URL, downloads all of your posts in a minute or so.

## Usage

Download/clone the script. It requires python 2.7.

1. Find your profile URL. This could take one of several forms (e.g. `/u/username` or `/people/guid`), but the easiest way to find it is to log in, and navigate to your profile. Copy the URL in the addressbar.
1. Open up a terminal in the same folder as the script and run this command:
        
        python diaspora-export.py http://your-pod.com/your-username
    (but obviously replace the URL with the one you found)
1. The script will let you know where it’s writing output to (which can be changed with the `-o` option), and print the URL of each page of results as it downloads them.
1. Once it’s finished, you’ll have a JSON file full of your posts. Go now, and do with them what you will :)

Perhaps you could import them into your [indieweb](http://indiewebcamp.com) site so you own your data and aren’t reliant on a donation-supported pod.

## Background

I used D* for ~6 months before becoming disenchanted and searching a more sustainable way to own my identity and content.

Now I’ve found that and have established [my identity](http://waterpigs.co.uk) online, I wanted to import my old D* content. But the tools were broken.

So I made tools which worked. Initial idea and algorithm/URL documentation [here](http://waterpigs.co.uk/notes/997/).
