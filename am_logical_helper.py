class LogicalHelper:

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    But the 1st tools were static, not needing a class at all
    """
    def __init__(
        self,
        pListPropositionsNames:list=[],
        pbStartingValueForModels:bool=True
    ):
        self.mListPropositionsNames = pListPropositionsNames
        self.mbStartingValueForModels = pbStartingValueForModels

        self.mModels = self.getPossibleModelsForPropositions()
    # def __init__

    #_.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    This is the most basic tool in LogicalHelper
    This was the 1st tool in the class
    It receives @param piHowManyValues how many bools it should produce,
    starting with bool value @param pbStartingValue,
    alternating them every @param piAlternateEvery occurrences.
    
    So, it is usefull as an aux for building all the possible combos of bool values for n proposition 
    
    Example call and returns:
    2,1 => [True, False]
    8,1 => [True, False, True, False, True, False, True, False]
    8, 2 => [True, True, False, False, True, True, False, False]
    Note: left-most value is @0 ... right-most value is @len-1
    """
    @staticmethod
    def getListOfAlternatingTrueFalse(
        piHowManyValues:int=2,
        piAlternateEvery:int=1,
        pbStartingValue:bool=True
    ):
        retList:list=list()

        bCurrentValue = pbStartingValue
        while(len(retList)<piHowManyValues):
            retList.append(bCurrentValue)
            bSwitchingTime:bool = len(retList)%piAlternateEvery == 0
            if(bSwitchingTime):
                bCurrentValue = not bCurrentValue
            # if time to swich values
        # while not enough values yet

        return retList
    # def getListOfAlternatingTrueFalse

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07
    This was the 2nd tool in class LogicHelper
    It is static, requires no init of a class object
    It receives a @param piNumberOfPropositions - number of propositions; e.g. 3
    It returns a list of lists, each being composed by 3 bools,
    representing all the 2^piNumberOfPropositions possible different combos of True/False
    """
    @staticmethod
    def getAllPossibleModelsForNPropositions(
        piNumberOfPropositions:int=1,
        pbStartingValue:bool=True
    ):
        listOfListsOfAlternatingTF:list = list()
        for iCurrentProposition in range(piNumberOfPropositions):
            listAltValues = LogicalHelper.getListOfAlternatingTrueFalse(
                piHowManyValues=2 ** piNumberOfPropositions, # 2**1=2, 2**2=4, 2**3=8, 2**4=16 ...
                piAlternateEvery=2 ** iCurrentProposition, # 2**0=1, 2**1=2, 2**2=4, ...
                pbStartingValue=pbStartingValue
            )

            listOfListsOfAlternatingTF.append(listAltValues)
        # for

        """
        2 propos in listOfListsOfAlternatingTF
        @0 => [True, False, True, False]
        @1 => [True, True, False, False]
        
        if one wants "models" from the above lists, it could be something like
        m0 = [t, t] = list@1[0], list@0[0]
        m1 = [t, f] = list@1[1], list@0[1]
        m2 = [f, t] = list@1[2], list@0[2]
        m3 = [f, f] = list@1[3], list@0[3]
        
        so:
        list index in decreasing
        list-element index in increasing
        """

        iHowManyListsOfAltValues = len(listOfListsOfAlternatingTF)
        listModels = list()

        for iValueIndex in range(2**piNumberOfPropositions):
            currentModel = list()
            iCurrentList = iHowManyListsOfAltValues-1

            while(iCurrentList>=0):
                currentList = listOfListsOfAlternatingTF[iCurrentList]
                bCurrentValue = currentList[iValueIndex]
                currentModel.append(bCurrentValue)

                iCurrentList -= 1
            # while iterating over lists of listsOfAltValues

            listModels.append(currentModel)
        # for iterating over values in lists of listsOfAltValues

        """
        [[True, True], [True, False], [False, True], [False, False]]
        """
        return listModels
    # def getAllPossibleModelsForNPropositions

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    The "LogicalHelper" class receives a list of propositions names
    For n propositions, there is 2^n = 2**n diferent combinations of True/False
    Those combinations are the "possible models"
    
    Instead of representing models are mere lists of True/False
    each model is a dict where a proposition indexes, by name, its value
    
    So, this tool is kind of a converter of lists of bools to a list of dicts,
    with propositions' names being the keys and the bools being the values
    """

    def getPossibleModelsForPropositions(self):
        listDictsModels = list()

        listPossibleModels = LogicalHelper.getAllPossibleModelsForNPropositions(
            piNumberOfPropositions=len(self.mListPropositionsNames),
            pbStartingValue=self.mbStartingValueForModels
        )

        for listModel in listPossibleModels:
            dictModel = dict()
            for iValueIndex in range(len(listModel)):
                bCurrentValue = listModel[iValueIndex]
                strCurrentPropositionName = self.mListPropositionsNames[iValueIndex]
                dictModel[strCurrentPropositionName] = bCurrentValue
            # for every value in current model

            listDictsModels.append(dictModel)
        # for every listModel

        return listDictsModels
    # def getPossibleModelsForPropositions

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    def getHeadlineTextForTruthTable(
        self,
        pStrOptionalLabelForResult:str=""
    ):
        strHeadline:str=""
        for propoName in self.mListPropositionsNames:
            strHeadline+=f"{propoName}\t"
        # for
        strHeadline+=f"{pStrOptionalLabelForResult}\n"
        return strHeadline
    # def getHeadlineTextForTruthTable

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    Receives:
    @param pSomeBoolFunction - a Python bool function
    @param pStrOptionalLabelForFunction - optionally, a string, a "readable" version of the function
    Returns:
    listResults - a list of bools, holding the returns of the calls to pSomeBoolFunction, in the same order
    as the class's self.mModels lists, used as unpacked arguments
    strText - a textual representation of the correspondence between models (self.mModels) and their results
    """
    def getTruthTableForBoolCall(
        self,
        pSomeBoolFunction,
        pStrOptionalLabelForFunction:str=""
    ):
        strText = self.getHeadlineTextForTruthTable(
            pStrOptionalLabelForResult=pStrOptionalLabelForFunction
        )

        listResults = list()

        for dictModel in self.mModels:
            listArgs = list()
            for strKey in dictModel:
                value = dictModel[strKey]
                listArgs.append(value)
            # for - forming the list of arguments

            # * to "unpack" the list and use its values as arguments in the function call
            result = pSomeBoolFunction(*listArgs)

            strLine = f"{listArgs}\t{result}\n"
            strText+=strLine

            listResults.append(result)
        # for

        return listResults, strText
    # def getTruthTableForBoolCall

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    Goal: to facilitate checking "logical consequences" between sets of left-expressions and a right expression
    the left-expressions are expected to have been "converted" to logical-ands in the Python bool function that corresponds to them
    When there is "logical consequence" from left to right, it is also said that the left "logically implies" the right
    
    expressions-left |= expression-right
    
    and(expressions-left 1, ... , expressions-left n) will be true in models m1 ... mn
    expressions-right must also be true for m1 ... mn, but can be true for more cases
    """
    def logicalImplicationOrLogicalConsequence(
        self,
        pLeftAndsFunction,
        pRightFunction,
        pLabelForLeft:str="",
        pLabelForRight:str="",
        pbVerbose:bool=True
    ):
        bLeftLogicallyImpliesRight = True
        listComparisonsLeftRightWhenLeftIsTrue = list() # will only hold cases where left is True for a model

        leftResults, leftText = self.getTruthTableForBoolCall(
            pSomeBoolFunction=pLeftAndsFunction,
            pStrOptionalLabelForFunction=pLabelForLeft
        )

        if(pbVerbose):
            print(leftText)

        rightResults, rightText = self.getTruthTableForBoolCall(
            pSomeBoolFunction=pRightFunction,
            pStrOptionalLabelForFunction=pLabelForRight
        )

        if (pbVerbose):
            print(rightText)

        for idxLeftResults in range(len(leftResults)):
            currentLefResult = leftResults[idxLeftResults]
            if (currentLefResult):
                currentRightResult = rightResults[idxLeftResults]
                bMatchForCurrentTrueResult = currentLefResult == currentRightResult

                listComparisonsLeftRightWhenLeftIsTrue.append(bMatchForCurrentTrueResult)

                bLeftLogicallyImpliesRight = bLeftLogicallyImpliesRight and bMatchForCurrentTrueResult
            # if the left (and'ed) expressions are True, check if the right are too (if there is a case where NOT, then NO implication9
        # for every model

        if(pbVerbose):
            strMsg = f"Left \"{pLabelForLeft}\" logically implies Right \"{pLabelForRight}\" is {bLeftLogicallyImpliesRight}\n"
            print(strMsg)
        # if

        return bLeftLogicallyImpliesRight, listComparisonsLeftRightWhenLeftIsTrue
    # def logicalImplicationOrLogicalConsequence

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    Receives a model as a dict: e.g. {"x":True, "y":False}
    returns its index in the list of models
    why? to pinpoint a specific model's result for a specific function
    """
    def getIndexOfSpecificDictModel(
        self,
        pModelAsDict:dict
    ):
        iHowManyModels = len(self.mModels)
        for idxModel in range(iHowManyModels):
            currentModel:dict = self.mModels[idxModel]
            bMatch = pModelAsDict == currentModel
            if (bMatch):
                break
        # for

        if(idxModel>=iHowManyModels):
            return False # no such model!
        else:
            return idxModel
        # if
    # def getIndexOfSpecificDictModel

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    Receives:
    - a model as a dict: e.g. {"x":True, "y":False}
    - a bool function,
    - optionally, a text for the bool function
    Returns True if the function holds True for the Model; False otherwise; or a message if the model does not exist
    """
    def isModelAsDictSatisfiedByBoolFunction(
        self,
        pModelAsDict: dict,
        pSomeBoolFunction,
        pStrOptionalLabelForFunction: str = "",
        pbVerbose:bool=True
    ):
        idxOfModel = self.getIndexOfSpecificDictModel(pModelAsDict)

        if (idxOfModel):
            listResults, textResults =\
                self.getTruthTableForBoolCall(
                    pSomeBoolFunction=pSomeBoolFunction,
                    pStrOptionalLabelForFunction=pStrOptionalLabelForFunction
                )

            resultForSpecificModel = listResults[idxOfModel]

            if(pbVerbose):
                strMsg = f"Function \"{pStrOptionalLabelForFunction}\", for model {str(pModelAsDict)}, is {resultForSpecificModel}\n"
                print(strMsg)
            # if

            return resultForSpecificModel
        # if

        strMsg = f"No such model: {str(pModelAsDict)}"
        return strMsg
    # def isModelAsDictSatisfiedByBoolFunction

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    """
    def logicalEquivalence(
        self,
        pLeftAndsFunction,
        pRightFunction,
        pLabelForLeft: str = "",
        pLabelForRight: str = "",
        pbVerbose: bool = True
    ):
        bLeftLogicallyImpliesRight, listComparisonsLeftRightWhenLeftIsTrue = \
            self.logicalImplicationOrLogicalConsequence(
                pLeftAndsFunction=pLeftAndsFunction,
                pRightFunction=pRightFunction,
                pLabelForLeft=pLabelForLeft,
                pLabelForRight=pLabelForRight,
                pbVerbose=False
            )

        bRightLogicallyImpliesLeft, listOfComparisonsRightLeftWhenRightIsTrue = \
            self.logicalImplicationOrLogicalConsequence(
                pLeftAndsFunction=pRightFunction,
                pRightFunction=pLeftAndsFunction,
                pLabelForLeft=pLabelForRight,
                pLabelForRight=pLabelForLeft,
                pbVerbose=False
            )

        bResult = bLeftLogicallyImpliesRight and bRightLogicallyImpliesLeft

        if(pbVerbose):
            strMsg = f"Left \"{pLabelForLeft}\" logically equivalues to Right \"{pLabelForRight}\" is {bResult}\n"
            print(strMsg)
        # if

        return bResult
    # def logicalEquivalence

    # _.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._.-^-._
    """
    2022-10-07 - Created
    """
    def canFunctionBeSatisfied(
        self,
        pFunction,
        pLabelForFunction:str="",
        pbVerbose:bool=True
    ):

        listResults, strText =\
            self.getTruthTableForBoolCall(
                pSomeBoolFunction=pFunction,
                pStrOptionalLabelForFunction=pLabelForFunction
            )

        bCanBeSatisfied = True in listResults

        strMsg = f"Function \"{pLabelForFunction}\" can be satisfied is {bCanBeSatisfied}\n"

        if(pbVerbose):
            print(strMsg)
        # if

        return bCanBeSatisfied
    # def canFunctionBeSatisfied
# class LogicalHelper
