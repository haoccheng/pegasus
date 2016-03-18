# find the kth most frequent element in a data stream.

# if approximate.
# I would propose to use min count sketch and maintain min heap for the kth most frequent.
# mincount would overestimate but never underestimate.
# min heap root is the exact kth most frequent item.
