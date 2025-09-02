function P = StopLossV(S0,K,mu,sigma,r,T,Paths)
[NRepl,NSteps] = size(Paths);
NSteps = NSteps - 1;
Cost = zeros(NRepl,1);
CashFlows = zeros(NRepl,NSteps+1);
dt = T/NSteps;
DiscountFactors = exp(-r*(0:1:NSteps)*dt);
OldPrice = [zeros(NRepl,1), Paths(:,1:NSteps)];
UpTimes = find(OldPrice < K & Paths >= K);
DownTimes = find(OldPrice >= K & Paths < K);
CashFlows(UpTimes) = -Paths(UpTimes);
CashFlows(DownTimes) = Paths(DownTimes);
ExPaths = find(Paths(:,NSteps+1) >= K);
CashFlows(ExPaths,NSteps+1) = CashFlows(ExPaths,NSteps+1) + K; 
Cost = -CashFlows*DiscountFactors';
P = mean(Cost);