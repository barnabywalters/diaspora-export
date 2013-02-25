# diaspora-export

Diaspora’s data export function is crap because it doesn’t include your posts (or didn’t for me, at lest). This script, given your profile URL, downloads all of your posts in a minute or so.

## Usage

Download/clone the script. It requires python 2.7.

Find your profile URL. This could take one of several forms (e.g. `/u/username` or `/people/guid`), but the easiest way to find it is to log in, and navigate to your profile. Copy the URL in the addressbar.

Open up a terminal in the same folder as the script and run this command:

    python diaspora-export.py http://your-pod.com/your-username

(but obviously replace the URL with the one you found)

The script will let you know where it’s writing output to (which can be changed with the `-o` option), and print the URL of each page of results as it downloads them.

Once it’s finished, you’ll have a JSON file full of your posts. Go now, and do with them what you will :)

Perhaps you could import them into your [indieweb](http://indiewebcamp.com) site so you own your data and aren’t reliant on a donation-supported pod.