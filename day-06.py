with open("input-06.txt") as f:
    direct_branches = {tuple(orbit[:-1].split(')')) for orbit in f}

direct_branches = {leaf : node for node, leaf in direct_branches}


def get_parent_nodes(leaf, direct_branches):    
        if leaf in direct_branches:
            parent = direct_branches[leaf]
            return [parent] + get_parent_nodes(parent, direct_branches)
        return []

# Part 1

parent_nodes = {leaf : get_parent_nodes(leaf, direct_branches) for leaf in direct_branches}
print(sum(len(orbit) for orbit in parent_nodes.values()))

# Part 2

you_parents = get_parent_nodes('YOU', direct_branches)
san_parents = get_parent_nodes('SAN', direct_branches)

common_parents = [node for node in you_parents if node in san_parents]

nearest_common_parent = common_parents[0]

distance = you_parents.index(nearest_common_parent) + san_parents.index(nearest_common_parent)

print(distance)





