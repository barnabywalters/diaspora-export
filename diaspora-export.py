#!/usr/bin/python

import argparse
import datetime
import json
import time
import urllib2 as http

def datetime_to_timestamp(datetime):
  return int(time.mktime(datetime.timetuple()))

def export_diaspora_posts(inurl):
  userurl = inurl.rstrip("/") + ".json"
  
  allposts = []
  nextmaxtime = None
  
  while True:
    if nextmaxtime == None:
      # do initial request
      print "Fetching " + userurl
      resp = http.urlopen(userurl)
    else:
      # request next page of posts
      pageurl = userurl + "?max_time=" + str(nextmaxtime)
      print "Fetching " + pageurl
      resp = http.urlopen(pageurl)
    
    posts = json.loads(resp.read())
    
    if len(posts) == 0:
      break
    
    allposts.extend(posts)
    
    # compute next max time to use
    last = posts[-1]
    lastdatetime = datetime.datetime.strptime(last['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    nextmaxtime = datetime_to_timestamp(lastdatetime)
  
  return allposts

if __name__ == '__main__':
  # get command line arguments
  parser = argparse.ArgumentParser(description="Export your Diaspora posts")
  
  parser.add_argument("uri", type=str, metavar="Profile URI", help="The URI of the user to export posts for, e.g. http://diasp.org/u/barnaby")
  parser.add_argument("-o", dest="output", type=str, metavar="Outfile", help="The path of the file to output the collected JSON to")
  
  args = parser.parse_args()
  
  if args.output:
    f = open(args.output, 'w+')
  else:
    f = open('diaspora_posts.json', 'w+')
  
  print "Writing output to " + f.name
  f.write(json.dumps(export_diaspora_posts(args.uri)))