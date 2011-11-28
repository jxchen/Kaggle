%% Initialization
clear ; close all; clc

load('covMatrix.mat');
load('knnData.mat');

k = 500;
m = size(X,1);
mtest = size(Xtest,1);

invCovMatrix = pinv(cv);

pred = zeros(m+mtest,1);

dists = zeros(m,1);
Xtemp = zeros(size(X));

#performance on training data
for i = 1:m,
	Xtemp = repmat(X(i,:),m,1) - X;
	[d1,d2] = sort(sum((Xtemp * invCovMatrix) .* Xtemp,2));
	pred(i) = sum(y(d2)(1:k)) / k;
endfor
fprintf('\nAUC: %f\n', SampleError(pred(1:m),y,'AUC'));

#performance on test data
for i = 1:mtest,
	Xtemp = repmat(Xtest(i,:),m,1) - X;
	[d1,d2] = sort(sum((Xtemp * invCovMatrix) .* Xtemp,2));
	pred(i+m) = sum(y(d2)(1:k)) / k;
endfor

save('pred.mat','pred','-mat');

csvwrite('output.csv',[linspace(1,mtest,mtest) , pred(m+1:end)]);
