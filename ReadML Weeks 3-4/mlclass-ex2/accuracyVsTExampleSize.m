%edubs and lvanderlyn
%olin readML
%2/19/2014

%% Looking at accuracy vs # of training examples

% these vectors will hold the data in a plot-friendly way
TE = 10:10:100 ; %each element in here is the # of training examples for that trial
A = zeros(1,10);

for i=1:10 
    datasetindices = randperm(100,TE(i));
    dataset = X(datasetindices);
    %%
end