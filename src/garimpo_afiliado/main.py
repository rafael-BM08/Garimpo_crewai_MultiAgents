from dotenv import load_dotenv

load_dotenv()

from garimpo_afiliado.crew import GarimpoAfiliado
from garimpo_afiliado.salvar import salvar_resultado

PLATAFORMAS_VALIDAS = ["shopee", "amazon", "mercado livre"]


def pedir_plataforma() -> str:
    while True:
        plataforma = input("Plataforma (shopee / amazon / mercado livre): ").strip().lower()
        if plataforma in PLATAFORMAS_VALIDAS:
            return plataforma
        print("Opção inválida. Digite shopee, amazon ou mercado livre.\n")


def run():
    print("=== GARIMPO AFILIADOS ===\n")

    plataforma = pedir_plataforma()
    categoria = input("Categoria (ex: casa, beleza) [Enter = geral]: ").strip() or "geral"

    inputs = {
        "plataforma": plataforma,
        "categoria": categoria,
    }

    try:
        resultado = GarimpoAfiliado().crew().kickoff(inputs=inputs)
        caminho = salvar_resultado(resultado, plataforma)
        print(f"\nResultado salvo em: {caminho}")
    except Exception as erro:
        print(f"Erro ao executar a crew: {erro}")


if __name__ == "__main__":
    run()