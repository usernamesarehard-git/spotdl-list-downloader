import subprocess as sb

with open("playlist.txt", "r") as txt:
    links = txt.readlines()

i = 0

while i < len(links):
    link = links[i].strip()
    command = "spotdl " + link
    result = sb.run(command)
    
    if result.returncode == 0:
        links.pop(i)
    else:
        i += 1

with open("playlist.txt", "w") as txt:
    txt.writelines(links)