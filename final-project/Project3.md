**Finance 6320, Spring 2014**\
**Project 3 Description**\
This example is taken from Chapter 4 of the book *Implementing
Derivatives Models* by Clewlow and Strickland. In this project you will
price a European fixed strike lookback call option. This option pays the
difference, if positive, between the maximum of a set of observations
(called fixings) of the asset price $S_{t_{i}}$ at dates
$t_{i}; i = 1, \ldots, N$ and the strike price. Thus the payoff at the
maturity date is

$$\max{(0, \max{(S_{t_{i}}; i = 1, \ldots, N)} - K)}$$

We will also assume that the asset price and the variance of the asset
price returns $V = \sigma^{2}$ are governed by the following stochastic
differential equations:

$$\begin{aligned}
dS &=& r S dt + \sigma S dz_{1} \\
dV &=& \alpha (\bar{V} - V) dt + \xi \sqrt{V} dz_{2}
\end{aligned}$$

and that the Wiener processes $dz_{1}$ and $dz_{2}$ are uncorrelated,
though this can easily be generalized.

There is no analytical solution for the price of a European fixed strike
lookback call option with discrete fixings and stochastic volatility.
However, there is a simple analytical formula for the price of a
continuous fixing fixed strike lookback call with constant volatility.

$$\begin{gathered}
C_{FSLBCall} = G + Se^{\delta T} N(x + \sigma \sqrt{T}) - Ke^{-rT}N(x) \\
                                  -\frac{S}{B} \left( e^{-rT} \left(\frac{E}{S} \right)^{B} N(x + (1 - B) \sigma \sqrt{T}) 
                                 -e^{-\delta T} N(x + \sigma \sqrt{T}) \right)
\end{gathered}$$

where

$$\begin{cases} \mbox{if} \quad K \ge M, & \, \mbox{then} \quad E = K, G = 0 \\
              \mbox{if} \quad K <   M, & \, \mbox{then} \quad E = M, G = e^{-rT}(M - K) \end{cases}$$

and

$$\begin{aligned}
B &=& \frac{2(r - \delta)}{\sigma^{2}} \\
x &=& \frac{\ln{\left(\frac{S}{E}\right)} + \left((r-\delta) - \frac{1}{2}\sigma^{2} \right)T}{\sigma \sqrt{T}}
\end{aligned}$$

and $M$ is the current known maximum. We can therefore use the
continuously fixed floating strike lookback call option formula to
compute *delta*, *gamma*, and *vega* hedge control variates. Rather than
differentiate the above equation with respect to the asset price twice
and volatility once which would lead to extremely complex expressions it
is more efficient to use finite difference approximations to the partial
differentials for *gamma* and *vega*.

A measure of the simulation error is the standard deviation of
$\hat{C_{0}}$ which is called the standard error $SE(\: \cdot \:)$ and
can be estimated as the sample standard deviation of $C_{0,j}$ divided
by the square root of the number of samples.

$$SE(\hat{C_{0}}) = \frac{SD(C_{0,j})}{\sqrt{M}}$$

where

$$SD(C_{0,j}) = \sqrt{\frac{1}{M-1} \sum\limits_{j=1}^{M} (C_{0,j} - \hat{C_{0}})^{2}}$$

The deliverable for this project, in addittion to the project source
code, is a table that presents the results of the simulation. For
example, fill in the missing data for the following table:

  -------------------- ------- ---------- -------------
                                Standard   Computation
                        Price    Error        Time
  Simple estimate                         
  Antithetic variate                      
  Control variates                        
  Combined variates                       
  -------------------- ------- ---------- -------------

The parameters for the problem are given in the following table.

  ---------------------------------- --------
  Strike Price                            100
  Time to Maturity                     1 year
  Initial asset price                     100
  Volatility                           $20\%$
  Risk--free rate                       $6\%$
  Continuous Dividend Yield             $3\%$
  Mean reversion rate ($\alpha$)          5.0
  Volatility of Volatility ($\xi$)       0.02
  Number of time steps                     52
  Number of simulations                  1000
  ---------------------------------- --------
