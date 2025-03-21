# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        # items: list of items at the inn
        self.items = items
        self.day = 0

    def update_quality(self):
        # Update the quality of each item
        for item in self.items:
            item.update_quality()  


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    # normal items decrease in quality by 1 each day or 2 if sell_in is less than 0
    # sell_in decreases by 1 each day
    
    def update_quality(self):
        # update the quality and sell_in value of the item
        if self.quality <= 0:
            self.quality = 0
        elif self.sell_in <= 0:
            self.quality -= 2
        else:
            self.quality -= 1
        self.sell_in -= 1
        

class AgedItem(Item):
    # aged items increase in quality by 1 each day
    # sell_in decreases by 1 each day

    def update_quality(self):
        # update the quality and sell_in value of the item
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1


class ConjuredItem(Item):
    # conjured items decrease in quality by 2 each day or 4 if sell_in is less than 0
    # sell_in decreases by 1 each day

    def update_quality(self):
        # update the quality and sell_in value of the item
        if self.quality <= 0:
            self.quality = 0
        elif self.sell_in <= 0:
            self.quality -= 4
        else:
            self.quality -= 2
        self.sell_in -= 1
        

class LegendaryItem(Item):
    # legendary items do not decrease in quality and never need sold

    def update_quality(self):
        # overide update_quality method to do nothing
        pass


class BackstagePass(Item):
    # backstage passes quality increases by 2 when there are 10 days or less
    # and by 3 when there are 5 days or less but drops to 0 after the concert
    # sell_in decreases by 1 each day

    def update_quality(self):
        # update the quality and sell_in value of the item
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1
        
        self.sell_in -= 1

        if self.quality > 50:
            self.quality = 50
            
