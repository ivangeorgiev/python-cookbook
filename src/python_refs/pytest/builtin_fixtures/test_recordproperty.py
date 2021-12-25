# Run with pytest --junitxml=report.xml


def test_recordproperty(record_property):
    """Testing record_property fixture"""
    record_property("my_property", "Recorded")
