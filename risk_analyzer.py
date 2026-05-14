class RiskAnalyzer:
    def calculate_risk_score(self, transaction, customer):
        risk_score = 0
        risk_reasons = []

        if transaction.amount > 50000:
            risk_score += 40
            risk_reasons.append("High-value transaction")

        if transaction.location.lower() != customer.city.lower():
            risk_score += 30
            risk_reasons.append("Transaction location is different from customer city")

        if transaction.category.lower() in ["crypto", "gambling", "unknown"]:
            risk_score += 30
            risk_reasons.append("High-risk transaction category")

        if risk_score >= 70:
            risk_level = "High Risk"
        elif risk_score >= 40:
            risk_level = "Medium Risk"
        else:
            risk_level = "Low Risk"

        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "risk_reasons": risk_reasons
        }
       
        