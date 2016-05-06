input tips
make keys out of tips
    if 2 nodes have no parent:
        join them as new key
    else:
        you have a tree as dict

score with parsimony and store

make a new NNI neighbor (that is not a previous one)
    if score of new is better:
        keep
        ditch already checked list
        put the old best tree in the list
    else:
        ditch - add to "already checked"
        make new NNI neighbor for that tree
    if you've done this ## times in a row and haven't found better NNI:
        break

repeat for 1000 best trees
