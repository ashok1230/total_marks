class A:  
    def __init__(self):
	pass
    def math(self,l):
	self.math=l
	print 'marks in math=',self.math
class B:
    def __init__(self):
	pass
    def science(self,s):
	self.science=s
	print 'marks in Science=',self.science
class C:
    def __init__(self):
	pass
    def english(self,m):
	self.english=m
	print 'marks in english=',self.english

class total(A,B,C):
    def __init__(self):	
	pass
    def tot(self,a,b,c):
	math=A.math(self,a)
	sci=B.science(self,b)
	eng=C.english(self,c)
	total=self.math+self.science+self.english
	print 'total=',total

x=total()
x.tot(23,25,24)

	