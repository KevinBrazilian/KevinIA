from modules.expansion import KevinIAExpansion

expansion = KevinIAExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
