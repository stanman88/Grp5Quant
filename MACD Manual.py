from Alphas.MacdAlphaModel import MacdAlphaModel
from Execution.ImmediateExecutionModel import ImmediateExecutionModel
from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel

class OptimizedModulatedCoreWave(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 4, 16)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        # self.AddEquity("SPY", Resolution.Minute)
        self.AddAlpha(MacdAlphaModel(12, 26, 9, MovingAverageType.Simple, Resolution.Daily))    #MACD

        self.SetExecution(ImmediateExecutionModel())    #Immediate execution

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())   #equal weight

    
        self.SetRiskManagement(MaximumUnrealizedProfitPercentPerSecurity(0.03)) #max unrealised profit
#Manually add stock counters in here
        symbols = [Symbol.Create("SPY", SecurityType.Equity, Market.USA),  Symbol.Create("AAPL", SecurityType.Equity, Market.USA)]
        self.SetUniverseSelection( ManualUniverseSelectionModel(symbols) )


    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''