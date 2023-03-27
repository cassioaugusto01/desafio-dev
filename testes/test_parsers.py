from app.parsers import parse_cnab

def test_parse_cnab():
    sample_content = "120220220220000000100000012345678123456789012345000001JOÃO DA SILVA  BAR DO JOÃO        "
    transactions = parse_cnab(sample_content)
    assert len(transactions) == 1
    assert transactions[0]["transaction_type"] == 1
    assert transactions[0]["date"] == "20220220"
    assert transactions[0]["amount"] == 100.0
    assert transactions[0]["cpf"] == "12345678901"
    assert transactions[0]["card"] == "234567890123"
    assert transactions[0]["time"] == "000001"
    assert transactions[0]["owner"] == "JOÃO DA SILVA"
    assert transactions[0]["name"] == "BAR DO JOÃO"