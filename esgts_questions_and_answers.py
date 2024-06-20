from am_logical_helper import LogicalHelper

# _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
print("*"*40)
print("Q2")

q2 = LogicalHelper(
    pListPropositionsNames=["x", "y"]
)

def q2_implies(x, y):
    return (not x) or y
# def q2_imples

def q2_and(x, y):
    return x and y
# def q2_and

def q2_y(x, y):
    return y
# def q2_y

def q2_or(x, y):
    return x or y
# def q2_or

def q2_false(x, y):
    return False
# def q2_false

"""
listResults, strResults = q2.getTruthTableForBoolCall(
    pSomeBoolFunction=q2_implies,
    pStrOptionalLabelForFunction = "x=>y"
)
print(strResults)

listResults, strResults = q2.getTruthTableForBoolCall(
    pSomeBoolFunction=q2_implies,
    pStrOptionalLabelForFunction = "x=>y"
)
print(strResults)

q2.getSpecificModelAsDictResult(
    {"x":True, "y":False}
)
"""
q2.isModelAsDictSatisfiedByBoolFunction(
    pModelAsDict={"x":True, "y":False},
    pSomeBoolFunction=q2_implies,
    pStrOptionalLabelForFunction = "x=>y"
)

q2.isModelAsDictSatisfiedByBoolFunction(
    pModelAsDict={"x":True, "y":False},
    pSomeBoolFunction=q2_and,
    pStrOptionalLabelForFunction = "x and y"
)

q2.isModelAsDictSatisfiedByBoolFunction(
    pModelAsDict={"x":True, "y":False},
    pSomeBoolFunction=q2_y,
    pStrOptionalLabelForFunction = "y"
)

q2.isModelAsDictSatisfiedByBoolFunction(
    pModelAsDict={"x":True, "y":False},
    pSomeBoolFunction=q2_or,
    pStrOptionalLabelForFunction = "x or y"
)

q2.isModelAsDictSatisfiedByBoolFunction(
    pModelAsDict={"x":True, "y":False},
    pSomeBoolFunction=q2_false,
    pStrOptionalLabelForFunction = "False"
)

# _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
print("*"*40)
print("Q3")

q3 = LogicalHelper(
    pListPropositionsNames=["p", "q"]
)

def q3_1(p, q):
    return (p or q) and (not p)
# def q3_1

def q3_q(p, q):
    return q
# def q3_q

def q3_p(p, q):
    return p
# def q3_p

def q3_2(p, q):
    return (p and q)
# def q3_2

def q3_3(p, q):
    return ((not p) or q) and q
# def q3_3

def q3_4(p, q):
    return (p or q)
# def q4_4

def q3_5(p, q):
    return ((not p) or q) and p
# def q3_5

q3.logicalImplicationOrLogicalConsequence(
    pLeftAndsFunction = q3_1,
    pRightFunction = q3_q,
    pLabelForLeft="(p or q) and (not p)",
    pLabelForRight="q",
    pbVerbose=True
)

q3.logicalImplicationOrLogicalConsequence(
    pLeftAndsFunction = q3_2,
    pRightFunction = q3_p,
    pLabelForLeft="p and q",
    pLabelForRight="p",
    pbVerbose=True
)

q3.logicalImplicationOrLogicalConsequence(
    pLeftAndsFunction = q3_3,
    pRightFunction = q3_p,
    pLabelForLeft="(p=>q) and q",
    pLabelForRight="p",
    pbVerbose=True
)

q3.logicalImplicationOrLogicalConsequence(
    pLeftAndsFunction = q3_4,
    pRightFunction = q3_p,
    pLabelForLeft="p or q",
    pLabelForRight="p",
    pbVerbose=True
)

q3.logicalImplicationOrLogicalConsequence(
    pLeftAndsFunction = q3_5,
    pRightFunction = q3_q,
    pLabelForLeft="(p=>q) and p",
    pLabelForRight="q",
    pbVerbose=True
)

# _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
print("*"*40)
print("Q4")

q41 = LogicalHelper(
    pListPropositionsNames=["x", "y"]
)

def q4_1L(x, y):
    return (not x) or (not y)
# def q4_1L

def q4_1R(x, y):
    return not(x or y)
# def q4_1R

def q4_5L(x, y):
    return (not x) and (not y)
# def q4_5L

def q4_5R(x, y):
    return not (x and y)
# def q4_5R

q41.logicalEquivalence(
    pLeftAndsFunction=q4_1L,
    pRightFunction=q4_1R,
    pLabelForLeft="(not x) or (not y)",
    pLabelForRight="not (x or y)"
)

q41.logicalEquivalence(
    pLeftAndsFunction=q4_5L,
    pRightFunction=q4_5R,
    pLabelForLeft="(not x) and (not y)",
    pLabelForRight="not (x and y)"
)

#------------------------------------------------------------------------------------------------------------------------

q42 = LogicalHelper(
    pListPropositionsNames=["u", "v"]
)

def q4_2L(u, v):
    return ((not u) or v)
# def q4_2L

def q4_2R(u, v):
    return not (u and (not v))
# def q4_2R

def q4_3L(u, v):
    return (not u) and v
# def q4_3L

def q4_3R(u, v):
    return not (u or (not v))
# def q4_3R

q42.logicalEquivalence(
    pLeftAndsFunction=q4_2L,
    pRightFunction=q4_2R,
    pLabelForLeft="(not u) or v",
    pLabelForRight="not (u and (not v)"
)

q42.logicalEquivalence(
    pLeftAndsFunction=q4_3L,
    pRightFunction=q4_3R,
    pLabelForLeft="(not u) and v",
    pLabelForRight="not (u or (not v))"
)
#------------------------------------------------------------------------------------------------------------------------

q43 = LogicalHelper(
    pListPropositionsNames=["a", "b", "c"]
)
def q4_4L(a, b, c):
    return a and (b or c)
# def q4_4L

def q4_4R(a, b, c):
    return (a and b) or (a and c)
# def q4_4R

q43.logicalEquivalence(
    pLeftAndsFunction=q4_4L,
    pRightFunction=q4_4R,
    pLabelForLeft="a and (b or c)",
    pLabelForRight="(a and b) or (a and c)"
)

# _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
print("*"*40)
print("Q5")

q5 = LogicalHelper(
    pListPropositionsNames=["p", "q", "r"]
)

def q5_1(p, q, r):
    return (p and (not q)) or (q and (not r))
# def q5_1

def q5_2(p, q, r):
    return (p or q) and ((not p) and (not q))
# def q5_2

def q5_3(p, q, r):
    return p and ((not p) or q)
# def q5_3

def q5_4(p, q, r):
    return (p and (not p)) or (q and (not q))
# def q5_4

def q5_5(p, q, r):
    return (p or (not q)) and (q or (not r))
# def q5_5

q5.canFunctionBeSatisfied(
    pFunction=q5_1,
    pLabelForFunction="(p and (not q)) or (q and (not r))",
    pbVerbose=True
)

q5.canFunctionBeSatisfied(
    pFunction=q5_2,
    pLabelForFunction="(p or q) and ((not p) and (not q))",
    pbVerbose=True
)

q5.canFunctionBeSatisfied(
    pFunction=q5_3,
    pLabelForFunction="p and ((not p) or q)",
    pbVerbose=True
)

q5.canFunctionBeSatisfied(
    pFunction=q5_4,
    pLabelForFunction="(p and (not p)) or (q and (not q))",
    pbVerbose=True
)

q5.canFunctionBeSatisfied(
    pFunction=q5_5,
    pLabelForFunction="(p or (not q)) and (q or (not r))",
    pbVerbose=True
)