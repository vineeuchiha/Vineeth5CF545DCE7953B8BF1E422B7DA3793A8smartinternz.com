def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index)
  return indices
product= ['sandals','shoes','boot','sandals','loafer','sandals']
target="sandals"
result=linearsearchproduct(product,target)
print(result)