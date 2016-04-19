from jinja2 import Template

file = open('src/index.html', 'r')

template = Template(file.read())
print template.render({
    'title': 'Mac Java'
})

# file = open("newfile.txt", "w")
# file.write("test")
# file.close()