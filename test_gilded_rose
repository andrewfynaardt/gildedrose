# -*- coding: utf-8 -*-
import unittest

from gilded_rose import NormalItem, AgedItem, ConjuredItem, LegendaryItem, BackstagePass, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_item_pre_sell_by(self):
        """Test that the quality of the normal item decreases by 1 before sell in date"""
        items = [NormalItem("Wooden Sword", 7, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((6,10), (items[0].sell_in, items[0].quality))
    
    def test_normal_item_post_sell_by(self):
        """Test that the quality of the normal item decreases by 2 past sell in date"""
        items = [NormalItem("Wooden Sword", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((-1,9), (items[0].sell_in, items[0].quality))

    def test_aged_item(self):
        """Test that the quality of the aged item increases by 1 each day"""
        items = [AgedItem("Aged Brie", 10, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((9,13), (items[0].sell_in, items[0].quality))

    def test_conjured_item_pre_sell_by(self):
        """Test that the quality of the conjured item decreases by 2 before sell in date"""
        items = [ConjuredItem("Conjured Tome", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((4,8), (items[0].sell_in, items[0].quality))

    def test_conjured_item_pre_sell_by(self):
        """Test that the quality of the conjured item decreases by 4 past sell in date"""
        items = [ConjuredItem("Conjured Tome", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((-1,1), (items[0].sell_in, items[0].quality))

    def test_backstage_pass_normal(self):
        """Test that the quality of the backstage pass increases by 1 when sell_in is greater than 10"""
        items = [BackstagePass("backstage pass", 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((14,11), (items[0].sell_in, items[0].quality))

    def test_backstage_pass_under_ten(self):
        """Test that the quality of the backstage pass increases by 3 when sell_in is less or equal to 5"""
        items = [BackstagePass("backstage pass", 9, 10), BackstagePass("backstage pass", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((8,12,9,12), (items[0].sell_in, items[0].quality, items[1].sell_in, items[1].quality))

    def test_backstage_pass_under_five(self):
        """Test that the quality of the backstage pass increases by 3 when sell_in is less or equal to 5"""
        items = [BackstagePass("backstage pass", 4, 10), BackstagePass("backstage pass", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((3,13,4,13), (items[0].sell_in, items[0].quality, items[1].sell_in, items[1].quality))

    def test_legendary_item(self):
        """Test that the legendary item does not change in quality or sell_in"""
        items = [LegendaryItem("sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual((0,80), (items[0].sell_in, items[0].quality))
        
if __name__ == '__main__':
    unittest.main()
