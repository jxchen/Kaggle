function Error = AUC(Predicted, Actual, nTarget, nBackground);
	Error = (sum(tiedrank(Predicted)(Actual == 1)) - (nTarget^2 + nTarget)/2) / (nTarget * nBackground);
end
