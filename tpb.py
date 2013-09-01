#!/usr/bin/env python

"""
Unofficial Python API for ThePirateBay.
Currently supports searching, recent torrents and top 100 torrents.

@author Karan Goel
@email karan@goel.im


Copyright (C) 2013  Karan Goel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import re
from urllib2 import urlopen

from bs4 import BeautifulSoup


BASE_URL = 'https://thepiratebay.sx' # could change!!!


class TPB():
    
    def get_soup(self, page=''):
        """
        Returns a bs4 object of the page requested. page can be:
        
        'recent'
        a 'search' page
        a 'top' page
        """
        content = urlopen('%s/%s' % (BASE_URL, page)).read()
        return BeautifulSoup(content)
    
    
    def get_torrents_rows(self, soup):
        """
        Returns all 'tr' tag rows as a list of tuples. Each tuple is for
        a single torrent.
        """
        table = soup.findChildren('table')[0] # the table with all torrent listing
        rows = table.findChildren(['tr'])[1:-1] # get all rows but header and page numbers
        
        return [row for row in rows]
    
    def build_torrent(self, all_rows):
        """
        Builds and returns a list of Torrent objects from
        the passed source.
        """
        all_torrents = [] # list to hold all torrents
        
        for row in all_rows:
            # Scrape, strip and build!!!
            cols = row.findChildren('td') # split the row into it's columns
            
            # this column contains the categories
            cat_col = cols[0].findAll('a')
            [category, sub_category] = [c.string for c in cat_col]
            
            # this column with all important info
            links = cols[1].findAll('a') # get 4 a tags from this columns
            
            title = links[0].string # title of the torrent
            url = '%s/%s' % (BASE_URL, links[0].get('href')) # the url of the torrent
            magnet_link = links[1].get('href') # the magnet download link
            torrent_link = links[2].get('href') # the .torrent download link
            user = links[4].string # uploaded by user
            
            # last 2 columns for seeders and leechers
            seeders = int(cols[2].string)
            leechers = int(cols[3].string)
            
            t = Torrent()
            all_torrents.append(t)
        
        return all_torrents


class Torrent():
    """
    Represents one single torrent on TPB
    """
    
    def __init__(self, title, url, category, sub_category, magnet_link,
                 torrent_link, created, size, user, seeders, leechers):
        self.title = title
        self.url = url
        self.category = category
        self.sub_category = sub_category
        self.magnet_link = magnet_link
        self.torrent_link = torrent_link
        self.created = created
        self.size = size
        self.user = user
        self.seeders = seeders
        self.leechers = leechers
    
    def print_torrent(self):
        """
        Print the details of a torrent
        """
        print 'Title: %s' % self.title
        print 'URL: %s' % self.url
        print 'Category: %s' % self.category
        print 'Sub-Category: %s' % self.sub_category
        print 'Magnet Link: %s' % self.magnet_link
        print 'Torrent Link: %s' % self.torrent_link
        print 'Uploaded: %s' % self.created
        print 'Size: %s' % self.size
        print 'User: %s' % self.user
        print 'Seeders: %d' % self.seeders
        print 'Leechers: %d' % self.leechers
    
    def __repr__(self):
        """
        A string representation of the class object
        """
        return '{0} by {1}'.format(self.title, self.user)