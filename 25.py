from Alphas.MacdAlphaModel import MacdAlphaModel
from Execution.ImmediateExecutionModel import ImmediateExecutionModel
from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel

class TachyonParticleAtmosphericScrubbers(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 4, 16)  # Set Start Date
        self.SetEndDate(2020, 4, 16)    # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        # self.AddEquity("SPY", Resolution.Minute)
        self.AddAlpha(MacdAlphaModel(12, 26, 9, MovingAverageType.Simple, Resolution.Daily))

        self.SetExecution(ImmediateExecutionModel())

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())

    
        self.SetRiskManagement(MaximumUnrealizedProfitPercentPerSecurity(0.03))

#Add Counters here
        symbols = [Symbol.Create("GOOG", SecurityType.Equity, Market.USA),  
        Symbol.Create("AAPL", SecurityType.Equity, Market.USA),
        Symbol.Create("NFLX", SecurityType.Equity, Market.USA),
        Symbol.Create("MSFT", SecurityType.Equity, Market.USA),
        Symbol.Create("EBAY", SecurityType.Equity, Market.USA),
        Symbol.Create("JPM", SecurityType.Equity, Market.USA),
        Symbol.Create("V", SecurityType.Equity, Market.USA),
        Symbol.Create("BAC", SecurityType.Equity, Market.USA), 
        Symbol.Create("WMT", SecurityType.Equity, Market.USA),
        Symbol.Create("SBUX", SecurityType.Equity, Market.USA),
        Symbol.Create("MCD", SecurityType.Equity, Market.USA),
        Symbol.Create("KHC", SecurityType.Equity, Market.USA),
        Symbol.Create("LLY", SecurityType.Equity, Market.USA),
        Symbol.Create("CHGG", SecurityType.Equity, Market.USA),
        Symbol.Create("FDX", SecurityType.Equity, Market.USA),
        Symbol.Create("ETSY", SecurityType.Equity, Market.USA),
        Symbol.Create("JMIA", SecurityType.Equity, Market.USA),
        Symbol.Create("SBSW", SecurityType.Equity, Market.USA),
        Symbol.Create("GS", SecurityType.Equity, Market.USA),
        Symbol.Create("HD", SecurityType.Equity, Market.USA),
        Symbol.Create("AZN", SecurityType.Equity, Market.USA),
        Symbol.Create("GSK", SecurityType.Equity, Market.USA),
        Symbol.Create("BLK", SecurityType.Equity, Market.USA),
        Symbol.Create("BABA", SecurityType.Equity, Market.USA),
        Symbol.Create("SPOT", SecurityType.Equity, Market.USA)]
        self.SetUniverseSelection( ManualUniverseSelectionModel(symbols) )


    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''

        # if not self.Portfolio.Invested:
        #    self.SetHoldings("SPY", 1)
