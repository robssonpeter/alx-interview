#!/usr/bin/python3
""" The module containing the lockboxes function """


def canUnlockAll(boxes):
    length = len(boxes)
    bxes = {0: True}
    """ Loop throught all the boxes"""
    index = 0
    for box in boxes:
        if index == 0:
            index += 1
            continue
        bxes[index] = False
        index += 1

    for box in boxes:
        """ Looop through items of the box """
        """ print(bxes) """
        for item in box:
            if(item <= length - 1 and bxes[item] is False):
                bxes[item] = True
        index += 1
    for boolean in list(bxes.values()):
        if boolean is False:
            return False
    return True
