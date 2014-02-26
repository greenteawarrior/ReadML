function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.


% % non matrix-multiplication way
% for it = 1:m;
%     SumDiff(1) = 0;
%     H(it) = theta(1) + theta(2) * X(it);
%     SumDiff(it+1) = SumDiff(it) + (H(it)-y(it))^2;
% end
% 
% J = 1/(2*m) * SumDiff(end);    


% it works with less code: 

%the hypothesis
H = X * theta; % matrix multiplication
J = ( 1/(2*m) ) * (sum( (H-y).^2 ));


% =========================================================================

end
