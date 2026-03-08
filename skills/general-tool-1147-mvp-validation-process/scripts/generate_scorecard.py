#!/usr/bin/env python3

def generate_scorecard():
    criteria = [
        ("Frequência/Volume", 1),
        ("Repetitividade", 1),
        ("Regra Clara", 2),
        ("Estabilidade", 2),
        ("Entradas Padronizadas", 1),
        ("Complexidade", 2),
        ("Testabilidade", 2),
        ("Reuso/Portabilidade", 2),
        ("Segurança/Risco", 2)
    ]
    
    print("--- MVP Evaluation Scorecard ---")
    total = 0
    for name, score in criteria:
        print(f"{name:<25}: {score}")
        total += score
    
    print("-" * 30)
    print(f"{'TOTAL':<25}: {total}")
    if total >= 15:
        print("Status: CANDIDATO APROVADO")
    else:
        print("Status: REVISÃO NECESSÁRIA")

if __name__ == "__main__":
    generate_scorecard()
