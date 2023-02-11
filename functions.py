def mensualite_max(revenu) :
    return 0.35 * revenu

def capacite_emprunt(mensualite_max, taux_credit, taux_assurance, nombre_mensualite) :
    taux_eq_credit = (1 + taux_credit) ** (1/12) - 1
    taux_eq_assurance = taux_assurance / 12
    return mensualite_max / ((taux_eq_credit / (1 - (1 + taux_eq_credit) ** (-nombre_mensualite))) + taux_eq_assurance)

def prise_en_compte_loyer(loyers) :
    return 0.7 * loyers

