# Portfolio Optimizer


The portfolio optimizer allows users to generate an efficiency frontier for a given portfolio of assets.
Risk tolerances and other portfolio structure restraints can be added at will.

The portfolio structure that was required for the course was:
 - no more than 20% weight in one asset
 - no short selling

The notebook is programmed to pull two csv files with the following information:
    
    excess returns csv:
        monthly risk free rate for the studied period
        monthly rolling excess returns for each individual security for the studied period
        
    excess returns statistics csv:
        mean excess returns for each security for the studied period
        standard deviations for each security for the studied period

From there the notebook will do the rest, generating the minimum variance and optimal portfolios, 1,000 portfolios on the efficent frontier, 10,000 dummy portfolios to illustrate the efficent frontier, and plotting it all.


## How you can take it further

- The obvious first step is to make it more dynamic, let the user enter an arbitrary list of tickers and go from there, pulling whatever data you need at runtime.

- The more tricky second step would be to allow users to select a set of constraints to optimize for. You could take this in a few different directions.

- Making it prettier could be easily accomplished by developing a better method to generate the dummy portfolios.


## Released under the MIT License

Copyright 2019 MAXIME GOSSELIN

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
