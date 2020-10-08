# sample 1
testIt = iter([1, 2, 3, 4, 5])
print [x**2 for x in testIt]

#sample 2
def getSimple(state=[]):
  if len(state) < 4:
    state.append(" ")
    return " "

testIt2 = iter(getSimple, None)
print [x for x in testIt2]

#sample 3
print [x for x in enumerate(sorted('avdsdf') )]


#sample 4
class Fibonacci:

# Iterrator Fobbonachi

  def __init__(self, N):
    self.n, self.a, self.b, self.max = 0, 0, 1, N
  def __iter__(self):
    #
     return self
  def next(self):
     if self.n < self.max:
       a, self.n, self.a, self.b = self.a, self.n+1, self.b, self.a+self.b
       return a
     else:
       raise StopIteration
#

