#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_assessment_value(value: float) -> float:
    """Return the assessment value (60% of actual property value)."""
    return value * 0.6

def get_tax_assessed(assessment_value: float) -> float:
    """Return the property tax: $0.72 per $100 of assessment value."""
    return assessment_value * 0.0072