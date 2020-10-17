from Alphas.MacdAlphaModel import MacdAlphaModel
from Execution.ImmediateExecutionModel import ImmediateExecutionModel
from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel

class TachyonParticleAtmosphericScrubbers(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 4, 16)  # Set Start Date
        self.SetEndDate(2020, 4, 16)    # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        # self.AddEquity("SPY", Resolution.Minute)
        self.AddAlpha(MacdAlphaModel(12, 26, 9, MovingAverageType.Simple, Resolution.Daily))

        self.SetExecution(ImmediateExecutionModel())

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())

    
        self.SetRiskManagement(MaximumUnrealizedProfitPercentPerSecurity(0.01))
#Add Counters here
        symbols = [Symbol.Create("GOOG", SecurityType.Equity, Market.USA),  
        Symbol.Create("AAPL", SecurityType.Equity, Market.USA),
        Symbol.Create("BABA", SecurityType.Equity, Market.USA),
        Symbol.Create("V", SecurityType.Equity, Market.USA),
        Symbol.Create("GS", SecurityType.Equity, Market.USA),
        Symbol.Create("GSK", SecurityType.Equity, Market.USA),
        Symbol.Create("LLY", SecurityType.Equity, Market.USA),
        Symbol.Create("KHC", SecurityType.Equity, Market.USA),
        Symbol.Create("FDX", SecurityType.Equity, Market.USA),
        Symbol.Create("KMB", SecurityType.Equity, Market.USA)]
        self.SetUniverseSelection( ManualUniverseSelectionModel(symbols) )


    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''

        # if not self.Portfolio.Invested:
        #    self.SetHoldings("SPY", 1)
