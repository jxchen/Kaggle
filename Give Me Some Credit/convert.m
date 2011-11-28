%% Initialization
clear ; close all; clc

M = csvread('scaled-cs-both.csv');

y = M(1:150000,1);
X = M(1:150000,2:end);
Xtest = M(150001:end,2:end);

size(M)
size(y)
size(X)
size(Xtest)

save('knnData.mat','X','y','Xtest','-mat');
