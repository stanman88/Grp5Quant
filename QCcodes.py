
/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using QuantConnect.Data;
using QuantConnect.Data.Consolidators;
using QuantConnect.Data.Market;
using QuantConnect.Indicators;
using System;
using System.Collections.Generic;
using System.Linq;
using QuantConnect.Util;
using static QuantConnect.StringExtensions;

namespace QuantConnect.Algorithm
{
    public partial class QCAlgorithm
    {
        private bool _isWarmUpIndicatorWarningSent = false;

        /// <summary>
        /// Gets whether or not WarmUpIndicator is allowed to warm up indicators/>
        /// </summary>
        public bool EnableAutomaticIndicatorWarmUp { get; set; } = false;
        
        
        /// <summary>
        /// Creates a new BollingerBands indicator which will compute the MiddleBand, UpperBand, LowerBand, and StandardDeviation
        /// </summary>
        /// <param name="symbol">The symbol whose BollingerBands we seek</param>
        /// <param name="period">The period of the standard deviation and moving average (middle band)</param>
        /// <param name="k">The number of standard deviations specifying the distance between the middle band and upper or lower bands</param>
        /// <param name="movingAverageType">The type of moving average to be used</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>A BollingerBands configured with the specified period</returns>
        public BollingerBands BB(Symbol symbol, int period, decimal k, MovingAverageType movingAverageType = MovingAverageType.Simple, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"BB({period},{k})", resolution);
            var bollingerBands = new BollingerBands(name, period, k, movingAverageType);
            RegisterIndicator(symbol, bollingerBands, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, bollingerBands, resolution);
            }

            return bollingerBands;
        }
        
        /// <summary>
        /// Creates a new DoubleExponentialMovingAverage indicator.
        /// </summary>
        /// <param name="symbol">The symbol whose DEMA we want</param>
        /// <param name="period">The period over which to compute the DEMA</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The DoubleExponentialMovingAverage indicator for the requested symbol over the specified period</returns>
        public DoubleExponentialMovingAverage DEMA(Symbol symbol, int period, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"DEMA({period})", resolution);
            var doubleExponentialMovingAverage = new DoubleExponentialMovingAverage(name, period);
            RegisterIndicator(symbol, doubleExponentialMovingAverage, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, doubleExponentialMovingAverage, resolution);
            }

            return doubleExponentialMovingAverage;
        }

/// <summary>
        /// Creates an ExponentialMovingAverage indicator for the symbol. The indicator will be automatically
        /// updated on the given resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose EMA we want</param>
        /// <param name="period">The period of the EMA</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The ExponentialMovingAverage for the given parameters</returns>
        public ExponentialMovingAverage EMA(Symbol symbol, int period, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            return EMA(symbol, period, ExponentialMovingAverage.SmoothingFactorDefault(period), resolution, selector);
        }


  /// <summary>
        /// Creates an ExponentialMovingAverage indicator for the symbol. The indicator will be automatically
        /// updated on the given resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose EMA we want</param>
        /// <param name="period">The period of the EMA</param>
        /// <param name="smoothingFactor">The percentage of data from the previous value to be carried into the next value</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The ExponentialMovingAverage for the given parameters</returns>
        public ExponentialMovingAverage EMA(Symbol symbol, int period, decimal smoothingFactor, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"EMA({period})", resolution);
            var exponentialMovingAverage = new ExponentialMovingAverage(name, period, smoothingFactor);
            RegisterIndicator(symbol, exponentialMovingAverage, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, exponentialMovingAverage, resolution);
            }

            return exponentialMovingAverage;
        }
        
        /// <summary>
        /// Creates a new HullMovingAverage indicator. The Hull moving average is a series of nested weighted moving averages, is fast and smooth.
        /// </summary>
        /// <param name="symbol">The symbol whose Hull moving average we want</param>
        /// <param name="period">The period over which to compute the Hull moving average</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns></returns>
        public HullMovingAverage HMA(Symbol symbol, int period, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"HMA({period})", resolution);
            var hullMovingAverage = new HullMovingAverage(name, period);
            RegisterIndicator(symbol, hullMovingAverage, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, hullMovingAverage, resolution);
            }

            return hullMovingAverage;
        }

        /// <summary>
        /// Creates a new IchimokuKinkoHyo indicator for the symbol. The indicator will be automatically
        /// updated on the given resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose ICHIMOKU we want</param>
        /// <param name="tenkanPeriod">The period to calculate the Tenkan-sen period</param>
        /// <param name="kijunPeriod">The period to calculate the Kijun-sen period</param>
        /// <param name="senkouAPeriod">The period to calculate the Tenkan-sen period</param>
        /// <param name="senkouBPeriod">The period to calculate the Tenkan-sen period</param>
        /// <param name="senkouADelayPeriod">The period to calculate the Tenkan-sen period</param>
        /// <param name="senkouBDelayPeriod">The period to calculate the Tenkan-sen period</param>
        /// <param name="resolution">The resolution</param>
        /// <returns>A new IchimokuKinkoHyo indicator with the specified periods and delays</returns>
        public IchimokuKinkoHyo ICHIMOKU(Symbol symbol, int tenkanPeriod, int kijunPeriod, int senkouAPeriod, int senkouBPeriod, int senkouADelayPeriod, int senkouBDelayPeriod, Resolution? resolution = null)
        {
            var name = CreateIndicatorName(symbol, $"ICHIMOKU({tenkanPeriod},{kijunPeriod},{senkouAPeriod},{senkouBPeriod},{senkouADelayPeriod},{senkouBDelayPeriod})", resolution);
            var ichimokuKinkoHyo = new IchimokuKinkoHyo(name, tenkanPeriod, kijunPeriod, senkouAPeriod, senkouBPeriod, senkouADelayPeriod, senkouBDelayPeriod);
            RegisterIndicator(symbol, ichimokuKinkoHyo, resolution);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, ichimokuKinkoHyo, resolution);
            }

            return ichimokuKinkoHyo;
        }
        
        /// <summary>
        /// Creates a new KaufmanAdaptiveMovingAverage indicator.
        /// </summary>
        /// <param name="symbol">The symbol whose KAMA we want</param>
        /// <param name="period">The period of the Efficiency Ratio (ER)</param>
        /// <param name="fastEmaPeriod">The period of the fast EMA used to calculate the Smoothing Constant (SC)</param>
        /// <param name="slowEmaPeriod">The period of the slow EMA used to calculate the Smoothing Constant (SC)</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The KaufmanAdaptiveMovingAverage indicator for the requested symbol over the specified period</returns>
        public KaufmanAdaptiveMovingAverage KAMA(Symbol symbol, int period, int fastEmaPeriod, int slowEmaPeriod, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"KAMA({period},{fastEmaPeriod},{slowEmaPeriod})", resolution);
            var kaufmanAdaptiveMovingAverage = new KaufmanAdaptiveMovingAverage(name, period, fastEmaPeriod, slowEmaPeriod);
            RegisterIndicator(symbol, kaufmanAdaptiveMovingAverage, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, kaufmanAdaptiveMovingAverage, resolution);
            }

            return kaufmanAdaptiveMovingAverage;
        }
        
        /// <summary>
        /// Creates a MACD indicator for the symbol. The indicator will be automatically updated on the given resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose MACD we want</param>
        /// <param name="fastPeriod">The period for the fast moving average</param>
        /// <param name="slowPeriod">The period for the slow moving average</param>
        /// <param name="signalPeriod">The period for the signal moving average</param>
        /// <param name="type">The type of moving average to use for the MACD</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The moving average convergence divergence between the fast and slow averages</returns>
        public MovingAverageConvergenceDivergence MACD(Symbol symbol, int fastPeriod, int slowPeriod, int signalPeriod, MovingAverageType type = MovingAverageType.Exponential, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"MACD({fastPeriod},{slowPeriod},{signalPeriod})", resolution);
            var movingAverageConvergenceDivergence = new MovingAverageConvergenceDivergence(name, fastPeriod, slowPeriod, signalPeriod, type);
            RegisterIndicator(symbol, movingAverageConvergenceDivergence, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, movingAverageConvergenceDivergence, resolution);
            }

            return movingAverageConvergenceDivergence;
        }
        
        /// <summary>
        /// Creates a new RelativeStrengthIndex indicator. This will produce an oscillator that ranges from 0 to 100 based
        /// on the ratio of average gains to average losses over the specified period.
        /// </summary>
        /// <param name="symbol">The symbol whose RSI we want</param>
        /// <param name="period">The period over which to compute the RSI</param>
        /// <param name="movingAverageType">The type of moving average to use in computing the average gain/loss values</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The RelativeStrengthIndex indicator for the requested symbol over the specified period</returns>
        public RelativeStrengthIndex RSI(Symbol symbol, int period, MovingAverageType movingAverageType = MovingAverageType.Wilders, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"RSI({period},{movingAverageType})", resolution);
            var relativeStrengthIndex = new RelativeStrengthIndex(name, period, movingAverageType);
            RegisterIndicator(symbol, relativeStrengthIndex, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, relativeStrengthIndex, resolution);
            }

            return relativeStrengthIndex;
        }
        
        /// <summary>
        /// Creates an SimpleMovingAverage indicator for the symbol. The indicator will be automatically
        /// updated on the given resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose SMA we want</param>
        /// <param name="period">The period of the SMA</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The SimpleMovingAverage for the given parameters</returns>
        public SimpleMovingAverage SMA(Symbol symbol, int period, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"SMA({period})", resolution);
            var simpleMovingAverage = new SimpleMovingAverage(name, period);
            RegisterIndicator(symbol, simpleMovingAverage, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, simpleMovingAverage, resolution);
            }

            return simpleMovingAverage;
        }
        
        /// <summary>
        /// Creates a new Stochastic indicator.
        /// </summary>
        /// <param name="symbol">The symbol whose stochastic we seek</param>
        /// <param name="resolution">The resolution.</param>
        /// <param name="period">The period of the stochastic. Normally 14</param>
        /// <param name="kPeriod">The sum period of the stochastic. Normally 14</param>
        /// <param name="dPeriod">The sum period of the stochastic. Normally 3</param>
        /// <returns>Stochastic indicator for the requested symbol.</returns>
        public Stochastic STO(Symbol symbol, int period, int kPeriod, int dPeriod, Resolution? resolution = null)
        {
            var name = CreateIndicatorName(symbol, $"STO({period},{kPeriod},{dPeriod})", resolution);
            var stochastic = new Stochastic(name, period, kPeriod, dPeriod);
            RegisterIndicator(symbol, stochastic, resolution);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, stochastic, resolution);
            }

            return stochastic;
            
            /// <summary>
        /// Creates an VolumeWeightedAveragePrice (VWAP) indicator for the symbol. The indicator will be automatically
        /// updated on the given resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose VWAP we want</param>
        /// <param name="period">The period of the VWAP</param>
        /// <param name="resolution">The resolution</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        /// <returns>The VolumeWeightedAveragePrice for the given parameters</returns>
        public VolumeWeightedAveragePriceIndicator VWAP(Symbol symbol, int period, Resolution? resolution = null, Func<IBaseData, TradeBar> selector = null)
        {
            var name = CreateIndicatorName(symbol, $"VWAP({period})", resolution);
            var volumeWeightedAveragePriceIndicator = new VolumeWeightedAveragePriceIndicator(name, period);
            RegisterIndicator(symbol, volumeWeightedAveragePriceIndicator, resolution, selector);

            if (EnableAutomaticIndicatorWarmUp)
            {
                WarmUpIndicator(symbol, volumeWeightedAveragePriceIndicator, resolution);
            }

            return volumeWeightedAveragePriceIndicator;
        }

        /// <summary>
        /// Creates the canonical VWAP indicator that resets each day. The indicator will be automatically
        /// updated on the security's configured resolution.
        /// </summary>
        /// <param name="symbol">The symbol whose VWAP we want</param>
        /// <returns>The IntradayVWAP for the specified symbol</returns>
        public IntradayVwap VWAP(Symbol symbol)
        {
            var name = CreateIndicatorName(symbol, "VWAP", null);
            var intradayVwap = new IntradayVwap(name);
            RegisterIndicator(symbol, intradayVwap);
            return intradayVwap;
        }


//////////////////////////////

/// <summary>
        /// Creates and registers a new consolidator to receive automatic updates at the specified resolution as well as configures
        /// the indicator to receive updates from the consolidator.
        /// </summary>
        /// <param name="symbol">The symbol to register against</param>
        /// <param name="indicator">The indicator to receive data from the consolidator</param>
        /// <param name="resolution">The resolution at which to send data to the indicator, null to use the same resolution as the subscription</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        public void RegisterIndicator(Symbol symbol, IndicatorBase<IndicatorDataPoint> indicator, Resolution? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            RegisterIndicator(symbol, indicator, ResolveConsolidator(symbol, resolution), selector ?? (x => x.Value));
        }

        /// <summary>
        /// Creates and registers a new consolidator to receive automatic updates at the specified resolution as well as configures
        /// the indicator to receive updates from the consolidator.
        /// </summary>
        /// <param name="symbol">The symbol to register against</param>
        /// <param name="indicator">The indicator to receive data from the consolidator</param>
        /// <param name="resolution">The resolution at which to send data to the indicator, null to use the same resolution as the subscription</param>
        /// <param name="selector">Selects a value from the BaseData to send into the indicator, if null defaults to the Value property of BaseData (x => x.Value)</param>
        public void RegisterIndicator(Symbol symbol, IndicatorBase<IndicatorDataPoint> indicator, TimeSpan? resolution = null, Func<IBaseData, decimal> selector = null)
        {
            RegisterIndicator(symbol, indicator, ResolveConsolidator(symbol, resolution), selector ?? (x => x.Value));
        }
}
}
