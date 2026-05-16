import ugit

ugit.wificonnect()
changes = ugit.check_for_updates(isconnected=True)
print(changes)
# {'new': ['/newfile.py'], 'changed': ['/boot.py'], 'deleted': []}

if changes["new"] or changes["changed"]:
    ugit.pull_all(isconnected=True)
