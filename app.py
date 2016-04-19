from jinja2 import Template
import os
import shutil

# Read HTML template and render using Jinja2
file = open('src/index.html', 'r')
template = Template(file.read())
templateRendered = template.render({
    'title': 'Mac Java'
})

# Create out dir if it does not exist
outDir = 'out/'
if not os.path.exists(outDir):
    os.makedirs(outDir)

# Write output file
file = open("out/index.html", "w")
file.write(templateRendered)
file.close()

# Copy assets to out dir
outAssetDir = outDir + 'assets'
if os.path.exists(outAssetDir):
    shutil.rmtree(outAssetDir)
shutil.copytree('src/assets', outAssetDir)