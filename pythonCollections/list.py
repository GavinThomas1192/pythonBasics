fav_things = ["Love", "Food", 11, "Video Games", "Programming"]

# add new item to list
fav_things += ["Warm woolen mittens"]

# adds new item to list
fav_things.append("guns")
# adds new item inside another list to original list 
fav_things.append(["beer"])
# adds new item to the list inside original list
fav_things[-1].append("whiskey")
# adds new item/items to the original list
fav_things.extend(["kids", "ponies"])


fav_things.insert(1, "I love beeeer")
# del fav_things[0]
print(fav_things)