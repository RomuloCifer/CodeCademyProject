import csv

# ===== 1) Ler CSV como lista de dicionários =====
with open("insurance.csv", "r", newline="") as f:
    rows = list(csv.DictReader(f))

# ===== 2) Tipos por coluna =====
CAST = {
    "age": int,
    "bmi": float,
    "children": int,
    "charges": float,
    "sex": str,
    "smoker": str,
    "region": str,
}

def cast(row, field):
    return CAST[field](row[field])

# ===== 3) Filtros básicos =====
def filtrar_valor(rows, field, op, value):
    """Filtra valores="""
    out = []
    for r in rows:
        a = cast(r, field)
        b = value
        ok = (
            (op == ">"  and a >  b) or
            (op == "<"  and a <  b) or
            (op == ">=" and a >= b) or
            (op == "<=" and a <= b) or
            (op == "==" and a == b)
        )
        if ok:
            out.append(r)
    return out

def filtrar_local(rows, region):
    return [r for r in rows if r["region"] == region]

def filtrar_fumantes(rows, somente="yes"):
    # somente: "yes" (fumantes) / "no" (não fumantes)
    return [r for r in rows if r["smoker"] == somente]

def contar_fumantes(rows):
    s = sum(1 for r in rows if r["smoker"] == "yes")
    ns = len(rows) - s
    return s, ns

# ===== 4) AND de vários critérios =====
# cada critério: {"field":"age","op":">=","value":30}
def filtrar_and(rows, criterios):
    out = []
    for r in rows:
        if all(filtrar_valor([r], c["field"], c["op"], c["value"]) for c in criterios):
            out.append(r)
    return out

# ===== 5) Estatística =====
def media_charges(rows):
    if not rows:
        return 0.0
    return sum(cast(r, "charges") for r in rows) / len(rows)

# ===== 6) Wrappers p/ menu =====
def menu_filtrar_um(rows):
    field = input("Campo (age/bmi/children/charges/sex/smoker/region): ").strip()
    op = input("Operador (>,<,>=,<=,==): ").strip()
    raw = input("Valor: ").strip()
    # converte para o tipo certo
    value = CAST[field](raw)
    result = filtrar_valor(rows, field, op, value)
    print(f"{len(result)} linhas encontradas.")
    return result

def menu_filtrar_varios(rows):
    criterios = []
    while True:
        field = input("age,sex,bmi,children,smoker,region,charges \n Campo (ou ENTER p/ terminar): ").strip()

        if not field:
            break
        if field == "smoker" or field == "region":
            print("Use o filtro específico para essa coluna.")
            continue
        op = input("Operador (>,<,>=,<=,==): ").strip()
        raw = input("Valor: ").strip()
        value = CAST[field](raw)
        criterios.append({"field": field, "op": op, "value": value})
    result = filtrar_and(rows, criterios)
    print(f"{len(result)} linhas encontradas.")
    return result

def menu_filtrar_regiao(rows):
    region = input("Região (northeast/northwest/southeast/southwest): ").strip()
    result = filtrar_local(rows, region)
    print(f"{len(result)} linhas na região {region}.")
    return result

def menu_fumantes(rows):
    escolha = input("Mostrar (yes = fumantes / no = não fumantes): ").strip()
    result = filtrar_fumantes(rows, escolha)
    s, ns = contar_fumantes(rows)
    print(f"No dataset atual: {s} fumantes, {ns} não fumantes.")
    print(f"{len(result)} linhas retornadas no filtro.")
    return result

def menu_media(rows):
    print(f"Média de charges nas {len(rows)} linhas correntes: {media_charges(rows):.2f}")
    return rows  # mantém o conjunto atual

# ===== 7) Menu principal =====
def main():
    atuais = rows[:]  # conjunto corrente que o usuário está trabalhando
    opcoes = {
        "1": ("Filtrar por 1 condição", menu_filtrar_um),
        "2": ("Filtrar por várias (AND)", menu_filtrar_varios),
        "3": ("Filtrar por região", menu_filtrar_regiao),
        "4": ("Filtrar fumantes/não", menu_fumantes),
        "5": ("Média de charges do conjunto atual", menu_media),
        "6": ("Resetar (voltar ao dataset completo)", None),
        "0": ("Sair", None),
    }
    while True:
        print("\n=== MENU ===")
        for k, (nome, _) in opcoes.items():
            print(f"[{k}] {nome}")
        esc = input("> ").strip()
        if esc == "0":
            break
        if esc == "6":
            atuais = rows[:]
            print("Conjunto resetado.")
            continue
        if esc in opcoes and opcoes[esc][1]:
            atuais = opcoes[esc][1](atuais)
        else:
            print("Opção inválida.")
    print("Até mais!")

if __name__ == "__main__":
    main()



        

