import os
import sys

INCLUDE_BEZEL=False
bez_offset=150 if INCLUDE_BEZEL else 0

cols=3
rows=4
total_w=4875 + 2*bez_offset*cols
total_h=5700 + 2*bez_offset*rows
base_n=200	#100		#29
wall_name='brew_wall'
conf_name='brew_conf'

class tile():
	n=1
	w=1625 	# Pure screen width  (not including bezel)
	h=1425	# Pure screen height (not including bezel)
	x_idx=0
	y_idx=-1

	def __init__(self):
		self.num=base_n+tile.n 
		self.name='pi'+str(self.num)
		if len(sys.argv)>1 and int(sys.argv[1])==tile.n:
			tile_str='[tile]\nid={}'.format(self.name)
			os.system('echo "'+tile_str+'" > .pitile')
		self.cfg_id='pi'+str(tile.n)+'='+self.name+'\n'
		self.width=tile.w
		self.height=tile.h
		horz_mod=tile.x_idx%cols
		self.x_bez=0 
		self.y_bez=0
		if horz_mod==0:  
			tile.y_idx+=1
		else:
			self.x_bez=bez_offset*2
		self.x=tile.w*(horz_mod)+self.x_bez
		tile.x_idx+=1
		vert_mod=tile.y_idx%rows
		if vert_mod>0:
			self.y_bez=bez_offset*2
		self.y=tile.h*(vert_mod)+self.y_bez
		tile.n+=1

	def __repr__(self):
		tile_str = '\n[{}]\n'.format(self.name)
		tile_str += 'wall={}\n'.format(wall_name)
		tile_str += 'width={}\n'.format(self.width)
		tile_str += 'height={}\n'.format(self.height)
		tile_str += 'x={}\ny={}\n'.format(self.x,self.y)
		return tile_str


if __name__=='__main__':
	piwall = '#wall definition\n[{}]\n'.format(wall_name)
	piwall += 'width={}\n'.format(total_w)
	piwall += 'height={}\n'.format(total_h)
	piwall += 'x=0\ny=0\n'
	piwall += '\n\n#tile definitions'
	config = '\n#config\n[{}]\n'.format(conf_name)
	tiles = []
	for r in range(rows):
		for c in range(cols):
			tiles.append(tile())
	for t in tiles:	
		piwall += repr(t)
		config += t.cfg_id
	piwall += '\n'+config
	os.system('echo "'+piwall+'" > .piwall')