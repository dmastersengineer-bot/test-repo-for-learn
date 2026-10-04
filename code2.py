# Find duplicate elements in a list
servers = [101, 102, 103, 102, 104, 101, 105]

seen = set()
duplicates = set()

for server in servers:
    if server in seen:
        duplicates.add(server)
    else:
        seen.add(server)

print(duplicates)