%% Initialization
clear ; close all; clc

load('knnData.mat');

cv = cov([X;Xtest]);

cv

save('covMatrix.mat','cv','-mat')
