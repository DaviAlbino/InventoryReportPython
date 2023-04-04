from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
                        1,
                        'Playstation 5',
                        'Sony',
                        '20/10/2020',
                        '20/10/2030',
                        'NP54',
                        'Ao abrido de luz solar'
                    )
    assert product.id == 1
    assert product.nome_do_produto == 'Playstation 5'
    assert product.nome_da_empresa == 'Sony'
    assert product.data_de_fabricacao == '20/10/2020'
    assert product.data_de_validade == '20/10/2030'
    assert product.numero_de_serie == 'NP54'
    assert product.instrucoes_de_armazenamento == 'Ao abrido de luz solar'
