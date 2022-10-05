# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        
        return item

    def get_by_category(self, a_category):
        items = []
        for item in self.inventory:
            if item.category == a_category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:    
            self.remove(my_item)
            friend.add(my_item)
            
            friend.remove(their_item)
            self.add(their_item)
            return True

    def swap_first_item(self, friend):
        if len(self.inventory) != 0 and len(friend.inventory) != 0:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])
    
    def get_best_by_category(self, category):
#COULD COME BACK AND TRY USING A MAX FXN AND LAMBDA EXPRESSION
        # best_condition = None
        # if len(self.inventory) == 0:
        #     return None
        # else:
        best_condition = max(self.get_by_category(category), default=None,\
        key=lambda item: item.condition)

        return best_condition


# #If there are no items in the inventory that match the category, it returns None
#         best_condition = None
#         best_condition_val = 0
# #Loop through the items of the correct category
#         for item in self.get_by_category(category):
# #If the condition of the item is more than the current best condition of all items
#             if item.condition > best_condition_val:
# #Update the best_condition_val with the current highest condition
#                 best_condition_val = item.condition
# #Update the value of best_condition with the item with the current highest condition
#                 best_condition = item 

#         return best_condition


    def swap_best_by_category(self, other, my_priority, their_priority):
        they_want = self.get_best_by_category(their_priority)
        i_want = other.get_best_by_category(my_priority)
        
        return self.swap_items(other, they_want, i_want)

    # def find_newest_item(self):
    #     newest_item = min(self.inventory, default=None,\
    #     key=lambda item: item.age)

    #     return newest_item

    # def swap_by_newest(self, friend):
    #     if len(self.inventory) != 0 and len(friend.inventory) != 0:
    #         return self.swap_items(friend, self.find_newest_item,\
    #             friend.find_newest_item)
