%% Initialization
clear ; close all; clc

load('covMatrix.mat');
load('knnData.mat');

k = 100;
m = size(X,1);
mtest = size(Xtest,1);

invCovMatrix = pinv(cv);

dists = zeros(m,1);
Xtemp = zeros(size(X));

neighbors = zeros(mtest,k);

#performance on test data
for i = 1:mtest,
	Xtemp = repmat(Xtest(i,:),m,1) - X;
	[d1,d2] = sort(sum((Xtemp * invCovMatrix) .* Xtemp,2));
	neighbors(i,:) = d2(1:k)';
	if mod(i,1000) == 0,
		i
		fflush(stdout);
	endif
endfor

save('testNeighbors.mat','neighbors','-mat');
