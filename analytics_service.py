class AnalyticsService:
    def generate_summary(self, analysis_results):
        total_transactions = len(analysis_results)
        total_amount = sum(item["transaction"]["amount"] for item in analysis_results)

        high_risk_count = sum(
            1 for item in analysis_results
            if item["risk_analysis"]["risk_level"] == "High Risk"
        )

        medium_risk_count = sum(
            1 for item in analysis_results
            if item["risk_analysis"]["risk_level"] == "Medium Risk"
        )

        low_risk_count = sum(
            1 for item in analysis_results
            if item["risk_analysis"]["risk_level"] == "Low Risk"
        )

        average_transaction_amount = total_amount / total_transactions if total_transactions > 0 else 0

        return {
            "total_transactions": total_transactions,
            "total_amount": total_amount,
            "average_transaction_amount": round(average_transaction_amount, 2),
            "high_risk_count": high_risk_count,
            "medium_risk_count": medium_risk_count,
            "low_risk_count": low_risk_count
        }

    def get_high_risk_transactions(self, analysis_results):
        return [
            item for item in analysis_results
            if item["risk_analysis"]["risk_level"] == "High Risk"
        ]