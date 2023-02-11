#Librairies
import streamlit as st

#Fonctions
import functions

st.title("Calculatrice de la capacité d'emprunt")

revenus = st.number_input("Entrez vos revenus mensuels net", value = 2500)
mensualite_max = functions.mensualite_max(revenus)

duree_emprunt = st.number_input("Entrez la durée de l'emprunt (en années)", step = 1, value = 20)
nombre_mensualite = duree_emprunt * 12

taux_credit = st.number_input("Entrez le taux du crédit", step = 0.0001, value = 0.02, format = "%0.4f")
taux_assurance = st.number_input("Entrez le taux d'assurance", step = 0.0001, value = 0.008, format = "%0.4f")

capacite_emprunt = functions.capacite_emprunt(mensualite_max, taux_credit, taux_assurance, nombre_mensualite)
st.write("Votre capacité d'emprunt maximale est de :", capacite_emprunt)

loyers = st.number_input("Entrez les loyers estimés que vous pensez percevoir avec cette capacité d'emprunt", value = 650)
loyers_pris_en_compte = functions.prise_en_compte_loyer(loyers)
mensualite_max_new = functions.mensualite_max(revenus + loyers_pris_en_compte)

capacite_emprunt_new = functions.capacite_emprunt(mensualite_max_new, taux_credit, taux_assurance, nombre_mensualite)
st.write("Votre capacité d'emprunt maximale en prenant en compte ces loyers est de :", capacite_emprunt_new, ". C'est donc un gain de :" , capacite_emprunt_new - capacite_emprunt)
