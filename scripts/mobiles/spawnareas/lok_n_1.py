# Spawn Area file created with PSWG Planetary Spawn Tool
import sys
from java.util import Vector

def addSpawnArea(core):
	dynamicGroups = Vector()
	dynamicGroups.add('lok_flit')
	dynamicGroups.add('lok_kusak')
	dynamicGroups.add('lok_perlek')
	core.spawnService.addDynamicSpawnArea(dynamicGroups, 0, 5000, 3500, 'lok')
	return
