import wiki

content="The Moon is an astronomical body orbiting Earth and is the planet's only natural satellite. It is the fifth-largest satellite in the Solar System, and by far[13] the largest among planetary satellites relative to the size of the planet that it orbits.[f] The Moon is, after Jupiter's satellite Io, the second-densest satellite in the Solar System among those whose densities are known. "
title="Moon"

wiki.save_page(title, content)

output= wiki.load_page('Moon')

print(output)

pages=wiki.list_topics()
print(pages)
