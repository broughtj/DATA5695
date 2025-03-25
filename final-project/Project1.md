---
title: Risk-Neutral Monte Carlo Project
subtitle: "DATA 5695: Computational Methods in FinTech"
---

# Introduction 

This example is taken from Chapter 4 of the book *Implementing Derivatives Models* by Clewlow and Strickland. In this project you will price a European arithmetic Asian call option. This option pays the difference (if positive) between the arithmetic average of the asset price $A_{T}$ and the strike price $K$ at the maturity date $T$. The arithmetic average is taken on a set of observations (called fixings) of the asset price $S_{t_{i}}$ (which we assume follows geometric Brownian motion) at dates $t_{i}; i = 1 \ldots N$.

$$
A_{T} = \frac{1}{N} \sum\limits_{i=1}^{N} S_{t_{i}}
$$

There is no analytical solution for the price of an arithmetic Asian option; however, there is a simple analytical formula for the price of a geometric Asian option. A geometric Asian call option pays the difference (again, only if positive) between the geometric average of the asset price $G_{T}$ and the strike price $K$ at the maturity date $T$. The geometric average is defined as

$$
G_{T} = \left( \prod\limits_{i=1}^{N} S_{t_{i}} \right) ^{1/N}
$$

Since the geometric average is essentially the product of lognormally distributed variables then it is also lognormally distributed. Therefore the price of the geometric Asian call option is given by a modified Black--Scholes formula:

$$
C_{GA} = exp(-rT) \left(exp(a + \frac{1}{2}b) N(x) - K N(x - \sqrt{b}) \right)
$$

where

$$\begin{aligned}
a        &=& \ln{(G_{t})} + \frac{N - m}{N} \left( \ln{(S)} + \nu (t_{m+1} - t) + \frac{1}{2} \nu (T - t_{m+1}) \right) \\
b        &=& \frac{(N - m)^{2}}{N^{2}} \sigma^{2}(t_{m+1} - t) + \frac{\sigma^{2} (T - t_{m+1})}{6 N^{2}} (N - m) (2(N - m) - 1)  \\
\nu &=& r - \delta - \frac{1}{2} \sigma^{2} \\
x        &=& \frac{a - \ln{(K)} + b}{\sqrt{b}}
\end{aligned}$$

where $G_{t}$ is the current geometric average and $m$ is the last known fixing. The geometric Asian option makes a good static hedge style control variate for the arithmetic Asian option. To implement the Monte Carlo method we simulate the difference between the arithmetic and geometric Asian options or a hedged portfolio which is long one arithmetic Asian and short one geometric Asian option. This is much faster than using the delta of the geometric Asian option to generate a delta hedge control variate because we do not have to compute the delta at every time step and it is equivalent to a continuous delta hedge.

For this project we will price a $1$--year maturity, European Asian call option with a strike price of $\$100$, a current asset price at $\$100$ and a volatility of $20\%$. The continuously compounded interest rate is assumed to be $6\%$ per annum, the asset pays a continuous dividend yield of $3\%$ per annum, and their are $10$ equally spaced fixing dates. The simulation has $10$ time steps and $10,000$ simulations; $K = \$100$, $T = 1$ year, $S = \$100$, $\sigma = 0.2$, $r = 0.06$, $\delta = 0.03$, $N = 10$, $M = 10000$.

The model for asset price dynamics at each time step is Geometric Brownian Motion, as follows

$$
S_{t} = S_{t-1} \times \exp{(nudt + sigsdt  \times \varepsilon)}
$$


where $\varepsilon$ is drawn from a standard normal distribution.

A good idea is to precompute the constants as follows:

$$\begin{aligned}
dt        &=& \Delta t  = \frac{T}{N} = \frac{1}{10} = 0.1 \\
nudt     &=& (r - \delta - \frac{1}{2} \sigma^{2}) \Delta t = (0.06 - 0.03 - 0.5 \times 0.2^{2}) \times 0.1 = 0.001 \\
sigsdt   &=& \sigma \sqrt{\Delta t} = 0.2 \sqrt{0.1} = 0.0632
\end{aligned}$$

Then for each simulation $j = 1$ to $M$ where $M = 10,000$, $S_{t}$ is initialised to $S = 100$, $sumSt = 0$ and $productSt = 1$. Then for each time step $i = 1$ to $N$, where $N = 10$, $S_{t}$ is simulated and the sum and product of the asset prices at the fixing times are accumulated.

The estimate of the option price is

$$\hat{C_{0}} = \frac{1}{M} \sum\limits_{i=1}^{M} C_{0,j}$$

where

$$C_{0,j} = \exp{(-rT)} C_{T,j}$$

and

$$C_{T,j} = \max{(0, A_{T} - K)}.$$

A measure of the simulation error is the standard deviation of $\hat{C_{0}}$ which is called the standard error $SE(\: \cdot \:)$ and can be estimated as the sample standard deviation of $C_{0,j}$ divided by the square root of the number of samples.

$$SE(\hat{C_{0}}) = \frac{SD(C_{0,j})}{\sqrt{M}}$$

where

$$SD(C_{0,j}) = \sqrt{\frac{1}{M-1} \sum\limits_{j=1}^{M} (C_{0,j} - \hat{C_{0}})^{2}}$$

The deliverable for this project, in addittion to the project source code, is a table that presents the results of the simulation. In the table present the price, standard error, and relative computation time for the following:

-   Simple Monte Carlo

-   Antithetic sampling

-   Control variate

-   Antithetic and control variate

Finally, give a brief statement about your conclusion regarding the trade--off between computation time and variance reduction costs.
