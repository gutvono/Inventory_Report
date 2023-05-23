from inventory_report.inventory.product import Product


# Teste da classe Product.
def test_cria_produto():
    id, ndp, nde, ddf, ddv, nds, ida = [
        1,
        "Radeon RX 6650 XT 8GB",
        "Sapphire AMD",
        "10/5/2022",
        "Vitalício",
        "Nitro X",
        "Local seguro"
    ]

    product = Product(id, ndp, nde, ddf, ddv, nds, ida)

    assert product.id == id
    assert product.nome_do_produto == ndp
    assert product.nome_da_empresa == nde
    assert product.data_de_fabricacao == ddf
    assert product.data_de_validade == ddv
    assert product.numero_de_serie == nds
    assert product.instrucoes_de_armazenamento == ida
