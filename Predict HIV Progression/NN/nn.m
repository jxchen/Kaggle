%% Initialization
clear ; close all; clc

%% Setup parameters
input_layer_size  = 12455;  % 21 codon categories x 593 sequence length + 2 other features
hidden_layer_size = 30;   % 30 hidden units
num_labels = 1;          % binary output for classification

%% Load data
load('trainingData.mat');
load('testData.mat');

%% Initialize NN parameters
initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

% Unroll parameters
initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

%% Training
options = optimset('MaxIter', 100);
lambda = 1;

costFunction = @(p) nnCostFunction(p, input_layer_size, hidden_layer_size, num_labels, X, y, lambda);

[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));


save('100weights.mat','Theta1','Theta2','-mat');

%%Predict on the Training Set
pred = predict(Theta1, Theta2, X);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);

%%Predict on Test Set

pred = predict(Theta1, Theta2, Xtest);
a = [linspace(1,size(Xtest,1),size(Xtest,1))',pred];
csvwrite('output.csv',a);              
