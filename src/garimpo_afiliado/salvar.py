
import json
from datetime import datetime
from pathlib import Path

def salvar_resultado(resultado, plataforma, pasta="resultados"):
    Path(pasta).mkdir(exist_ok=True)


    agora = datetime.now().strftime("%Y-%m-%d_%H-%M")
    base = Path(pasta) / f"{plataforma}_{agora}"
        
    dados = []

    for saida in resultado.tasks_output:
        if saida.pydantic:
            dados.append(saida.pydantic.model_dump())
        else:
              dados.append({"texto": saida.raw})

    base.with_suffix(".json").write_text(
        json.dumps(dados, ensure_ascii=False, indent=2 ),
        encoding="utf-8"
    )

    textos = [saida.raw for saida in resultado.tasks_output]
    base.with_suffix(".md").write_text(
        "\n\n---\n\n".join(textos),
        encoding="utf-8",
    )

    return base