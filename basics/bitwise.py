# bitwise operator: & | ^ >> <<
# binary conversion, only support int

'''
2048 1024 512 256 128 64 32 16 8 4 2 1
   0    0   0   0   0  1  1  0 0 0 1 0  >> 98   >> froyo
   0    0   1   0   0  0  0  0 1 0 0 0  >> 520  >> gingerbread
   0    0   1   0   0  1  1  0 1 0 1 0  >> 618  >> froyo
   0    0   0   0   0  1  1  0 0 0 1 0  >> 98   >> gingerbread
   0    0   1   0   0  0  0  0 1 0 0 0  >> 520  >> froyo
   
   0    0   1   1   0  0  0  1 0 0 1 0  >> 786
   0    0   1   1   0  0  0  1 1 0 1 0  >> 794
   0    0   0   0   0  1  1  0 0 0 1 0  >> 98
   0    0   0   0   0  0  1  0 1 0 0 0  >> 40
   
   0    0   0   0   0  0  1  0 0 0 0 0  >> 32

'''

froyo,gingerbread=98,520

# 1,1 >> 1
print(froyo&40)

# 1,0>>1 
# 1,1>>1
# 0,1>>1
# 0,0>>0
print(gingerbread|786)

# 1,0>>1
# 0,1>>1
print(froyo^gingerbread)



print("froyo is",froyo,"gingerbread is",gingerbread)
# swap using ^

froyo^=gingerbread
gingerbread^=froyo
froyo^=gingerbread

print("froyo is",froyo,"gingerbread is",gingerbread)