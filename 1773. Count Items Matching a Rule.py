# Problem Link https://leetcode.com/problems/count-items-matching-a-rule/

def count_matches(items, rule_key, rule_value):
    keys = {'type': 0, 'color': 1, 'name': 2}

    return sum(item[keys[rule_key]] == rule_value for item in items)


print(count_matches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 'color', 'silver'))
